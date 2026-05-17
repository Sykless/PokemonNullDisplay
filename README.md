
# Description <img src="https://upload.wikimedia.org/wikipedia/en/c/c3/Flag_of_France.svg" height="20"> &nbsp;/&nbsp; <img src="https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg" height="20">

- [Utilisation](#utilisation-) - [Installation](#installation-) - [Configuration](#configuration-) &nbsp;<img src="https://upload.wikimedia.org/wikipedia/en/c/c3/Flag_of_France.svg" height="15">
- [Usage](#usage-) - [Installation](#installation--1) - [Configuration](#configuration--1) &nbsp;<img src="https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg" height="15">
- [Contact](#contact)

<img src="https://upload.wikimedia.org/wikipedia/en/c/c3/Flag_of_France.svg" height="15">&nbsp; PokemonNullDisplay est un programme développé pour la Rom Hack Pokémon Null générant des images des Pokémons capturés en jeu. Ces images s'actualisent en temps réel et peuvent être ajoutées dans OBS pour afficher l'état du jeu en direct. Le programme génère trois images : <br />

<img src="https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg" height="15">&nbsp; PokemonNullDisplay is a program developed for the Rom Hack Pokémon Null that generates images of in-game caught Pokémon. Those images refresh in real time and can be added to OBS to display the current state of the game. Three images are generated : <br />
<br />

| Party     | Box      | Dead       |
| :-------- | :------- | :--------- |
| <img width="500" alt="party" src="https://github.com/user-attachments/assets/2e442ec5-9e35-467f-be30-e74d88ba5226" /> | <img width="500" alt="box" src="https://github.com/user-attachments/assets/cbdfe4e3-2b13-4d9a-8ef3-fd50d2cd4d41" /> | <img width="500" alt="dead" src="https://github.com/user-attachments/assets/3bc9e2eb-fdd7-477b-8c69-3b90ee61a7cf" />

<br />

# Utilisation <img src="https://upload.wikimedia.org/wikipedia/en/c/c3/Flag_of_France.svg" height="20">

Une fois [l'installation](#installation-) réalisée, à chaque utilisation :
- Lancer le programme **PokemonNullDisplay.exe**
- Attacher le script **PokemonNullDisplay.lua** à mGBA (voir [Étape 2 de l'installation](#%EF%B8%8F-étape-2--ajout-du-script-lua-à-lémulateur)) <br />
<br />

# Installation <img src="https://upload.wikimedia.org/wikipedia/en/c/c3/Flag_of_France.svg" height="20">

## ➡️ Étape 1 : Initialisation du programme

Fermer l'émulateur mGBA s'il est en cours d'exécution. Télécharger puis unzipper la [dernière version du programme](https://github.com/Sykless/PokemonNullDisplay/releases) dans le dossier de votre choix (_éviter les dossier protégés comme C:\Program Files_). Lancer ensuite le programme PokemonNullDisplay.exe : le message "**Pokémon Null Display en cours d'exécution...**" devrait apparaître. <br />

## ➡️ Étape 2 : Ajout du script lua à l'émulateur

Ajouter ensuite le script "PokemonNullDisplay.lua" à mGBA : aller dans "Outils" -> "Scripting", puis dans la fenêtre qui s'ouvre, aller dans "File" -> "Load script" et sélectionner le script "PokemonNullDisplay.lua" : le message "**Pokémon Null Display en cours d'exécution...**" devrait apparaître. Lancer ensuite la ROM et vérifiez que les trois images ont été générées dans le dossier **outputImage**. <br />

## ➡️ Étape 3 : Ajout des images dans OBS

Dans OBS, ajouter une source de type "Image" et choisir une des trois images générées dans le dossier **outputImage**. Une fois l'image affichée, clic droit sur l'image, "Filtre de mise à l'échelle" -> "Point" pour obtenir image plus nette. L'image devrait maintenant s'actualiser à chaque mise à jour en jeu. <br />
<br />

# Configuration <img src="https://upload.wikimedia.org/wikipedia/en/c/c3/Flag_of_France.svg" height="20">

Le fichier **configuration.txt** permet d'activer ou désactiver certaines options en passant les variables suivantes à 1 pour activer ou 0 pour désactiver : 

| Variable             | Description                                                                |
| ----------------- | ------------------------------------------------------------------ |
| **DISPLAY_SPRITE_ITEMS** | Affiche ou non les objets tenus par les Pokémons du PC et de l'équipe |
| **DISPLAY_MULTIPLE_BOXES** | Affiche ou non les Pokémons des autres boîtes que la Boîte 1 |
| **BOX_DISPLAY_TIME** | Durée d'affichage de chaque boîte si l'option précédente est activée |

<br />

# Usage <img src="https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg" height="20">

After [installation](#installation--1) is done, whenever you use it :
- Execute program **PokemonNullDisplay.exe**
- Attach script **PokemonNullDisplay.lua** to mGBA (see [Installation Step 2](#%EF%B8%8F-step-2--add-lua-script-to-emulator)) <br />
<br />

# Installation <img src="https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg" height="20">&nbsp;

## ➡️ Step 1 : Setup program

Close mGBA emulator if running. Download then unzip the [latest program version](https://github.com/Sykless/PokemonNullDisplay/releases) in the folder of your choice (_avoid protected folders like C:\Program Files_). Then, run PokemonNullDisplay.exe : the message "**Pokémon Null Display en cours d'exécution...**" should appear. <br />

## ➡️ Step 2 : Add lua script to emulator

Add "PokemonNullDisplay.lua" script to mGBA : go to "Tools" -> "Scripting", then in the next window, go to "File" -> "Load script" and select "PokemonNullDisplay.lua" script : the message "**Pokémon Null Display en cours d'exécution...**" should appear. Launch the ROM and make sure the three images have been generated in the folder **outputImage**. <br />

## ➡️ Step 3 : Add images to OBS

In OBS, add a new "Image" source, and select one of the three generated images in the folder **outputImage**. When the image is displayed, right click on it, "Scale Filtering" -> "Point" for a better image quality. The image should now update after any in-game modification. <br />
<br />

# Configuration <img src="https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg" height="20">

The **configuration.txt** file allows to enable or disable certain options by setting those variables to 1 to enable or 0 to disable

| Variable             | Description                                                                |
| ----------------- | ------------------------------------------------------------------ |
| **DISPLAY_SPRITE_ITEMS** | Display or not the items held by Pokémon in the PC or in the team |
| **DISPLAY_MULTIPLE_BOXES** | Display or not the Pokémon in the other boxes than Box 1 |
| **BOX_DISPLAY_TIME** | Display time of each box if the previous option is enabled |

<br />

# Contact
- Discord : [@Sykless](https://discordapp.com/users/Sykless#2124)
- Twitch : [@TristanPelleteuse](https://www.twitch.tv/tristanpelleteuse)

# Contributeur
- Projet commandé par @pseudoless2, merci à lui !