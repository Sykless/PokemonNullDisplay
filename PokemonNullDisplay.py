import os
import sys
import file
import time
import subprocess
from PIL import Image
from file import TEMPOUTPUT_FOLDER, OUTPUT_FOLDER

INPUT_FILE = "pokemonData.txt"
SPRITE_FOLDER = "sprites"
POKEMONSPRITE_FOLDER = SPRITE_FOLDER + "/pokemon"
ITEMSPRITE_FOLDER = SPRITE_FOLDER + "/items"

DISPLAY_SPRITE_ITEMS = "DISPLAY_SPRITE_ITEMS"
DISPLAY_MULTIPLE_BOXES = "DISPLAY_MULTIPLE_BOXES"
BOX_DISPLAY_TIME = "BOX_DISPLAY_TIME"
DEAD_BOX_SIZE = "DEAD_BOX_SIZE"

POKEMON_SPRITE_WIDTH = 80
POKEMON_SPRITE_HEIGHT = 60
ITEMS_SPRITE_SIZE = 32
LEVEL_UP_SPRITE_SIZE = 18

ITEM_X_POSITION = 42
ITEM_Y_POSITION = 28

LEVELUP_X_POSITION = 49
LEVELUP_Y_POSITION = 4

SPACING_X = -30
SPACING_Y = -10

class PokemonData:
    def __init__(self, pokedexId, level, itemId):
        self.pokedexId = pokedexId
        self.level = int(level)
        self.itemId = itemId

    def __str__(self):
        return self.pokedexId + " - " + str(self.level) + " - " + self.itemId
    
    def __repr__(self):
        return str(self)


# Create env variable for pokemonData.txt file so lua script can know its path
def ensureSetup():

    # Read from .exe script
    if getattr(sys, 'frozen', False):
        ownPath = os.path.dirname(sys.executable)

    # Read from python script
    else:
        ownPath = os.path.dirname(os.path.abspath(__file__))
        
    # Set path as global env variable
    confFilePath = os.path.join(ownPath, INPUT_FILE)
    os.system(f'setx POKEMONNULLREADER_CONFFILE "{confFilePath}"')


# Parse PARTY|1¤10¤1|2¤25¤2|3¤3¤0 style lines into Pokémon data
def parseLine(line):
    parsedLine = []
    pokemonList = line.split("|")[1:]

    for pokemonData in pokemonList:

        # No Pokémon
        if not pokemonData:
            parsedLine.append(None)

        # No "¤" in line : raw data, add it directly
        elif ("¤" not in pokemonData):
            parsedLine.append(pokemonData)

        # Multiple info, store them in PokemonData object
        else:
            parsedLine.append(PokemonData(*pokemonData.split("¤")))

    return parsedLine


# Create images from Pokémon sprites
def generatePlayerPartyImage(label, pokemonList, columnNumber, rowNumber, customSize = None):

    # Retrieve conf file content to check user preferences
    configuration = file.readConfFile()

    # Remove None Pokemon for custom sizes
    if (customSize):
        pokemonList = [pokemonData for pokemonData in pokemonList if pokemonData]

    # Initialise transparent image
    imageWidth = POKEMON_SPRITE_WIDTH * columnNumber + SPACING_X * (columnNumber - 1)
    imageHeight = POKEMON_SPRITE_HEIGHT * rowNumber + SPACING_Y * (rowNumber - 1)
    outputImage = Image.new("RGBA", (imageWidth, imageHeight), (0,0,0,0))

    # Iterate on each non-None Pokémon
    for i, pokemonData in enumerate(pokemonList):
        if pokemonData is None:
            continue

        # Retrieve Pokémon sprite (default sprite : Pokéball)
        pokemonSpritePath = os.path.join(POKEMONSPRITE_FOLDER, f"{pokemonData.pokedexId}.png")
        if not os.path.exists(pokemonSpritePath):
            pokemonSpritePath = os.path.join(POKEMONSPRITE_FOLDER, "0.png")

        # Retrieve and resize Pokémon sprite to 80x60 so items can appear small without sizing them down
        pokemonSprite = Image.open(pokemonSpritePath).convert("RGBA").resize((POKEMON_SPRITE_WIDTH, POKEMON_SPRITE_HEIGHT), Image.NEAREST)

        # Compute Pokémon sprite position with spacing (sligh overlap between sprites so they appear closer)
        x = (i % columnNumber) * (POKEMON_SPRITE_WIDTH + SPACING_X)
        y = (i // columnNumber) * (POKEMON_SPRITE_HEIGHT + SPACING_Y)

        # Display Pokémon sprite
        outputImage.paste(pokemonSprite, (x, y), pokemonSprite)

        # Display held item
        if (configuration[DISPLAY_SPRITE_ITEMS] and int(pokemonData.itemId)):

            # Retrieve item sprite (default sprite : blank item)
            itemPath = os.path.join(ITEMSPRITE_FOLDER, f"{pokemonData.itemId}.png")
            if not os.path.exists(itemPath):
                itemPath = os.path.join(ITEMSPRITE_FOLDER, "0.png")

            # Display item sprite
            itemSprite = Image.open(itemPath).convert("RGBA").resize((ITEMS_SPRITE_SIZE, ITEMS_SPRITE_SIZE), Image.NEAREST)
            outputImage.paste(itemSprite, (x + ITEM_X_POSITION, y + ITEM_Y_POSITION), itemSprite)

    # Save final image in output folder
    file.safeWriteFile(outputImage, label)



# Main loop
def mainLoop():
    os.makedirs(OUTPUT_FOLDER, exist_ok = True) # Create outputImage folder is not exists
    os.makedirs(TEMPOUTPUT_FOLDER, exist_ok = True) # Create .tmp folder is not exists
    subprocess.run(["attrib", "+h", TEMPOUTPUT_FOLDER], shell = True)
    print("Pokémon Null Display en cours d'exécution...") # Notify user when ready to use

    boxClock = 0 # Alternate between every box every 5 seconds
    boxDisplayTime = 5 # Default : 5 seconds
    boxNumber = 0 # Track which box we're currently displaying

    while True:
        try:
            # Retrieve data written by lua scipt
            emulatorData = file.safeReadFile(INPUT_FILE)

            if emulatorData:
                lines = emulatorData.splitlines()

                # Retrieve conf file content to check user preferences
                configuration = file.readConfFile()
                displayMultipleBoxes = configuration[DISPLAY_MULTIPLE_BOXES]
                boxDisplayTime = configuration[BOX_DISPLAY_TIME]
                deadBoxSize = str(configuration[DEAD_BOX_SIZE])

                # Setup dead box custom size
                if ("X" in deadBoxSize.upper()):
                    columnNumber, rowNumber = deadBoxSize.upper().split("X")
                    columnNumber, rowNumber = (int(columnNumber), int(rowNumber)) if columnNumber.isnumeric() and rowNumber.isnumeric() else (6,5)
                else:
                    columnNumber, rowNumber = (6,5)

                # Retrieve each line and parse its data
                for line in lines:
                    if line.startswith("BOX"):
                        fullBox = parseLine(line)
                        numberOfBoxes = int(len(fullBox) / 30) if fullBox else 1

                        # 5th second : display next box
                        if (boxClock == boxDisplayTime - 1):
                            boxNumber = (boxNumber + 1) % numberOfBoxes if displayMultipleBoxes else 0

                        # Take the 30 Pokémon from the provided box
                        boxLine = fullBox[30*boxNumber : 30*(boxNumber + 1)]
                        
                    elif line.startswith("DEAD"):
                        deadLine = parseLine(line)

                    elif line.startswith("PARTY"):
                        partyLine = parseLine(line)

                # Create png images from parsed data
                generatePlayerPartyImage("party", partyLine, 6, 1)
                generatePlayerPartyImage("box", boxLine, 6, 5)
                generatePlayerPartyImage("dead", deadLine, columnNumber, rowNumber, customSize = True)

            # Check file every second
            time.sleep(1)
            boxClock = (boxClock + 1) % boxDisplayTime # Every 5 seconds by default, customizable
        
        # Don't stop script if an error occurs, just print it in the logs
        except Exception as e:
            print("An error occurred :", e)


# Start script
if __name__ == "__main__":
    ensureSetup()
    mainLoop()