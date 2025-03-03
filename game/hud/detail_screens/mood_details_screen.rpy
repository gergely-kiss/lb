screen  mood_details_screen:
    frame:
        background "#000000cc"
        xsize config.screen_width/3
        ysize config.screen_height/3
    frame:
        background "#00000000"
        xalign 0.5
        yalign 0.22
        xsize 600
        yminimum 100
        text "Mood of the character"
    frame:
        background "#00000000"
        xalign 0.5
        yalign 0.51
        xsize 600
        yminimum 50
        text "Mood modifiers"

    frame:
        background "#00000000"
        xalign 0.5
        yalign 0.56
        xsize 600
        yminimum 50
        text "Hunger: [mood_hunger_text]"
    frame:
        background "#00000000"
        xalign 0.5
        yalign 0.61
        xsize 600
        yminimum 50
        text "Rested: [mood_resting_text]"
    frame:
        background "#00000000"
        xalign 0.5
        yalign 0.66
        xsize 600
        yminimum 50
        text "Hygiene: [mood_hygenic_text]"
    frame:
        background "#00000000"
        xalign 0.5
        yalign 0.76
        xsize 600
        yminimum 50
        text "Emotional: [mood_emotional_text]"