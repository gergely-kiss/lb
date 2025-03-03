screen  beauty_details_screen():
    frame:
        background "#000000cc"
        xsize config.screen_width/3
        ysize config.screen_height/3
    frame:
        background "#00000000"
        xalign 0.5
        yalign 0.2
        xsize 600
        yminimum 100
        text "Beauty"
    frame:
        background "#00000000"
        xalign 0.5
        yalign 0.26
        xsize 600
        yminimum 100
        text "How desired the character is in the eye of others." 
    frame:
        background "#00000000"
        xalign 0.5
        yalign 0.40
        xsize 600
        yminimum 50
        text "Beauty modifiers"

    frame:
        background "#00000000"
        xalign 0.5
        yalign 0.45
        xsize 600
        yminimum 50
        text "Allure: [beauty_allure]"
    frame:
        background "#00000000"
        xalign 0.5
        yalign 0.50
        xsize 600
        yminimum 50
        text "Clothing: [beauty_clothing]"
    frame:
        background "#00000000"
        xalign 0.5
        yalign 0.55
        xsize 600
        yminimum 50
        text "Makeup: [beauty_makeup]" 
    frame:
        background "#00000000"
        xalign 0.5
        yalign 0.60
        xsize 600
        yminimum 50
        text "Lust: [beauty_lust]" 