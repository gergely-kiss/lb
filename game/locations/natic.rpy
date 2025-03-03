define pref_loc = "/images/locations/" 
screen natic():
    default this_loc=natic
    default tooltip_text_room = ""
    default target_loc1 = nhallway_l3
    default target_loc1_label = nhallway_l3_label
    default target_loc2 = nroof_terrace
    default target_loc2_label = nroof_terrace_label
    modal True

    imagemap:
        ground Transform(f"{pref_loc}{this_loc}_ground{suf_jpg}")
        hover Transform(f"{pref_loc}{this_loc}_hover{suf_jpg}")
        hotspot (700, 380, 80, 320) action [Show("boudoir_screen")]
        hotspot (872, 663, 662, 240) action [Show("go_to_sleep"), Hide("status_bar_screen")]

    frame:
        background "#00000000"
        xpos 20
        ypos config.screen_height - int(config.screen_height / 5.25)

        #spacing 15
        imagebutton xpos 20:
            idle Frame(f"{pref_loc}frame{suf_png}", xsize=140, ysize=140) 
            hover Frame(f"{pref_loc}frame{suf_png}", xsize=140, ysize=140) 
            foreground Transform(f"{pref_loc}{target_loc1}_ground{suf_jpg}", size=(135, 130),align=(0.6, 0.5), alpha=nav_ibtn_alpha_idle)
            hover_foreground Transform(f"{pref_loc}{target_loc1}_ground{suf_jpg}", size=(135, 130), align=(0.6, 0.5), alpha=nav_ibtn_alpha_hover)
            action [
                Hide(f"{this_loc}", transition = Dissolve(1)),
                With(Dissolve(5)),
                Show(f"{target_loc1}", transition = Dissolve(1)),
                Jump("go_update_mhd_twominutes")
            ]
            hovered [SetScreenVariable("tooltip_text_room", target_loc1_label)]
            unhovered [SetScreenVariable("tooltip_text_room", "")]

        imagebutton xpos 20+195:
            idle Frame(f"{pref_loc}frame{suf_png}", xsize=140, ysize=140) 
            hover Frame(f"{pref_loc}frame{suf_png}", xsize=140, ysize=140) 
            foreground Transform(f"{pref_loc}{target_loc2}_ground{suf_jpg}", size=(135, 130),align=(0.6, 0.5), alpha=nav_ibtn_alpha_idle)
            hover_foreground Transform(f"{pref_loc}{target_loc2}_ground{suf_jpg}", size=(135, 130), align=(0.6, 0.5), alpha=nav_ibtn_alpha_hover)
            action [
                Hide(f"{this_loc}", transition = Dissolve(1)),
                Show(f"{target_loc2}", transition = Dissolve(1)),
                Jump("go_update_mhd_twominutes")
            ]
            hovered [SetScreenVariable("tooltip_text_room", target_loc2_label)]
            unhovered [SetScreenVariable("tooltip_text_room", "")]
     
    if not can_change_outfit:
        timer 0.01 action [SetVariable("can_change_outfit", True)]    
    add mc_images["mc_base"] at zoom_and_position_mc_right
    use status_bar_screen

    if tooltip_text_room != "":
        frame:
            background "#0000007b"
            xalign 0.5
            yalign 0.075
            xsize 300
            padding (10, 5)
            text tooltip_text_room style "gothic_styl_text":
                xalign 0.5