# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    mc_base_path="images/mc_base.png"
    mc_images = {
        "mc_base":mc_base_path
    }

    def setImageVariables():
        global mc_base_path

    def get_mc_image(st, at):
        return mc_base, 0  # Returns the correct image name as a tuple

    renpy.image("mc_base", DynamicDisplayable(get_mc_image))


# The game starts here.

label start:
    call update_bravery(10)
    call update_money(-10)
    call update_lust(9)
    call update_mood("hunger", 1)
    call update_mood("resting", 2)
    call update_mood("hygenic", 3)
    call update_mood("emotional", 4) 
    call update_mhd(0, 0, 0)
    call update_beauty("allure", 3)
    call update_beauty("clothing",4)
    call update_beauty("makeup", 5)
    window hide
    $ quick_menu = False
    $ config.rollback_enabled = False
    $ in_screen = True
    #show screen status_bar_screen
    show screen natic
    pause
