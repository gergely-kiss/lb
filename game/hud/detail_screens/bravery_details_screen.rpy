screen  bravery_details_screen():
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
        text "Bravery"
    frame:
        background "#00000000"
        xalign 0.5
        yalign 0.25
        xsize 600
        yminimum 100
        text f"{img_btn_path}clock{idle_img_btn}"