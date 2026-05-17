import os

TEMPOUTPUT_FOLDER = ".tmp"
OUTPUT_FOLDER = "outputImage"
CONF_FILE = "configuration.txt"

# Read file safely even if used by lua script
def safeReadFile(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception:
        return None


# Write file safely even if used by OBS
def safeWriteFile(image, fileName):

    # Save final image in .tmp folder to avoid OBS reading partially written image
    tempOutputPath = os.path.join(TEMPOUTPUT_FOLDER, f"{fileName.lower()}.png")
    outputPath = os.path.join(OUTPUT_FOLDER, f"{fileName.lower()}.png")
    image.save(tempOutputPath, "PNG")
    image.close()

    # Swap temp image and output image
    try:
        os.replace(tempOutputPath, outputPath)

    # PermissionError errors might occur because OBS is reading the image, don't print those
    except PermissionError:
        pass


# Read configuration.txt and convert user preferences into boolean
def readConfFile():
    configuration = {}
    configurationFile = safeReadFile(CONF_FILE)

    for line in configurationFile.splitlines():
        if (line.count("=") == 1):
            configurationSplit = line.split("=")
            configuration[configurationSplit[0]] = int(configurationSplit[1]) if configurationSplit[1].isnumeric() else configurationSplit[1]

    return configuration