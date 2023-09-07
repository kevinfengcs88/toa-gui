# Tombs of Amascut Invocation GUI

Graphical user interface built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) to simulate [Old School RuneScape's](https://oldschool.runescape.com/a=97/) [Tombs of Amascut's](https://oldschool.runescape.wiki/w/Tombs_of_Amascut) invocation system. 

### TODO

- Add images to each invocation for easier category identification
- Add ability to save presets
- Show a rewards window corresponding to the rare drops that players could receive at that raid level
- Prevent user from breaking invocation rules after "following them"
    - eg. Turning Overclocked so that Overclocked 2 can be turned on, and then turning Overclocked off
- Set up a GitHub Actions CI/CD pipeline for dockerizing the app, running automated tests, etc.
- Allow user to change an invocation category without manually turning off the already active one (will also require invocationchange.mp3 sound effect)

### Requirements
```
pip install CTkToolTip
pip install customtkinter
pip install pygame
```