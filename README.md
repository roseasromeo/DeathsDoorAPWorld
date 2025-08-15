# DeathsDoorArchipelago: APWorld for Death's Door
Death's Door is a game about being a crow whose job it is to collect souls, who then accidentally stumbles into a grand conspiracy about the nature of life and death. Also, you hit things with weapons.

This project is an [Archipelago](https://archipelago.gg/) apworld for [Death's Door](https://store.steampowered.com/app/894020/Deaths_Door/) that works with a [mod](https://github.com/Chris-Is-Awesome/DDArchipelagoRandomizer/). Together, they will take the things your character would pick up throughout the game and randomize them, potentially between multiple games. If you are not familiar with Archipelago, we recommend reading Archipelago's introduction documents starting with the [FAQ](https://archipelago.gg/faq/en/).

## Instructions
1. Setup the [Death's Door Archipelago Mod mod](https://github.com/Chris-Is-Awesome/DDArchipelagoRandomizer/) as described in its README.
2. Install [Archipelago 0.6.3+](https://github.com/ArchipelagoMW/Archipelago/releases/) (or follow their instructions to run from source)
3. Download the latest apworld provided on the [releases page](https://github.com/roseasromeo/DeathsDoorAPWorld/releases/latest)
    - Check to make sure the name of your download does not have any artifacts (i.e. no (1) or other browser added names). The apworld should be named "deaths_door.apworld"
    - To create the apworld from scratch: download this repo's source code and zip the whole folder into a file named deaths_door.apworld. The zip/apworld file should contain a `deaths_door` folder at the top level 
4. On Windows, double-click the apworld &mdash; it should be "installed" (copied) into the `custom_worlds` folder in your Archipelago installation folder. (On Linux and Mac, manually copy the apworld into the `custom_worlds` folder)
5. Set your options in a .yaml file [as described below](#creating-your-yaml), and put that yaml file and yamls for any other players/games in the `Players` folder in your Archipelago installation folder (note that you will need to run the Archipelago Launcher and click on "Generate template options" to create this folder)
    - Make sure you remove any yamls for people who are not playing this time! If you're planning to play one "world" of Death's Door, there should only be one yaml
    - The "name" at top of the yamls needs to be unique for each player in the game (sorry, not everyone can be "CAAAAAAW")
6. Push the Generate button in the Launcher.
7. Host the generated game locally either by hitting Host Game and selecting the AP_{numbers}.zip in the `output` folder (in your Archipelago installation folder) or host it through [archipelago.gg](https://archipelago.gg) by uploading that zip to https://archipelago.gg/uploads

### Recommendations for Better Play Experiences
- Download [Universal Tracker](https://github.com/FarisTheAncient/Archipelago/releases) and use it to track which locations are in logic.
- Use the text client (which you can also open from the Archipelago Launcher) alongside your game. Using the text client will allow you to see what items you are sending and receiving in more detail.

## Creating your yaml
Start by installing the apworld (Steps 2-4 in [Instructions](#instructions)). Open the Archipelago Launcher and click `Generate Template Options`. On Windows, a File Explorer should open to the newly generated folder of template yamls (on other OSs, you will need to navigate to your Archipelago installation, then to `Players/Templates`). Within that file, you'll see all of the options available in Death's Door (Death's Door specific options are described [below](#deaths-door-specific-options)) If you would like to experiment with other options not listed here, you can check the [advanced yaml instructions](https://archipelago.gg/tutorial/Archipelago/advanced_settings/en) provided by Archipelago.

### yaml Recommendations
- In small multiworlds, under current options available, we highly recommend that you leave `early_important_item` set to `early` or change it to `local_early`. This option reduces the likelihood that the fill algorithm will back itself into a corner.

### Death's Door Specific Options
- Start Day or Night
    - Choose whether to start with daytime or nighttime. Must access Rusty Belltower Bell in game to toggle using the Rusty Belltower Key (or a glitch).
- Early Important Item
    - Choose whether one random important item will be placed early in the multiworld ("early"), early and in your world ("local_early"), or be allowed to be randomly placed ("random_placement").
    - If random placement, generation is more likely to fail.
    - Important items are all non-boss doors, Hookshot, Bomb, and Fire since these unlock access to more early game checks.
- Starting Weapon
    - Choose which weapon you would like to start with (others will be shuffled into the itempool as useful items).
    - Note: Umbrella is a much worse weapon than the other 4. Choose at your own risk.