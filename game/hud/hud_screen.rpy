default img_prefix = "images/" 
default img_btn_path = f"{img_prefix}hud/"
default suf_jpg = ".jpg"
default suf_png = ".png"
default idle_img_btn = suf_png
default hover_img_btn = suf_png

default hud_gui_img_btn_sufix="_hud"
default hud_screen_img_btn_sufix="_screen"

default hud_ibtn_zoom_idle = 0.045
default hud_ibtn_zoom_hover = 0.05
default hud_ibtn_alpha_idle = 0.5
default hud_ibtn_alpha_backpack_idle = 0.7
default hud_ibtn_alpha_hover = 1
default hud_ibtn_alpha_idle_screen = hud_ibtn_alpha_idle + 1

default hud_ibtn_sidebar_zoom_idle = 0.06
default hud_ibtn_sidebar_zoom_hover = 0.0605

default eye_ibtn_sidebar_zoom_idle = 0.1
default eye_ibtn_sidebar_zoom_hover = 0.1005

default nav_ibtn_zoom_idle = 0.3
default nav_ibtn_zoom_hover = 0.305
default nav_ibtn_alpha_idle = 0.45
default nav_ibtn_alpha_hover = nav_ibtn_alpha_idle + 1

screen status_bar_screen():
    zorder 94 
    default tooltip_text = ""
    frame:
        background "#000000e9"
        xsize config.screen_width
        ysize int(config.screen_height / 16)
        xpos 0
        ypos 0
        
        hbox:
            spacing 25
            xalign 0.0
            yalign 0.5

            frame:
                background None
                hbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 10
                    imagebutton:
                        idle Transform(f"{img_btn_path}clock{idle_img_btn}", zoom=hud_ibtn_zoom_idle, alpha=hud_ibtn_alpha_idle)
                        action NullAction()
                        sensitive False
                    text "Week [current_week_text] | [current_day_text] [current_hour_text]:[current_minute_text]" yalign 0.5 
            
            hbox:
                spacing 15
                yalign 0.5
                imagebutton:
                    idle Transform(f"{img_btn_path}two{idle_img_btn}", zoom=hud_ibtn_zoom_idle, alpha=hud_ibtn_alpha_idle)
                    hover Transform(f"{img_btn_path}two{hover_img_btn}", zoom=hud_ibtn_zoom_idle, alpha=hud_ibtn_alpha_hover)
                    action Jump("go_update_mhd_twominutes")
                    hovered SetScreenVariable("tooltip_text", "Wait 2 minutes")
                    unhovered SetScreenVariable("tooltip_text", "")
                imagebutton:
                    idle Transform(f"{img_btn_path}thirteen{idle_img_btn}", zoom=hud_ibtn_zoom_idle, alpha=hud_ibtn_alpha_idle)
                    hover Transform(f"{img_btn_path}thirteen{hover_img_btn}", zoom=hud_ibtn_zoom_idle, alpha=hud_ibtn_alpha_hover)
                    action Jump("go_update_mhd_thirteenminutes")
                    hovered SetScreenVariable("tooltip_text", "Wait 13 minutes")
                    unhovered SetScreenVariable("tooltip_text", "")
                imagebutton:
                    idle Transform(f"{img_btn_path}sixty{idle_img_btn}", zoom=hud_ibtn_zoom_idle, alpha=hud_ibtn_alpha_idle)
                    hover Transform(f"{img_btn_path}sixty{hover_img_btn}", zoom=hud_ibtn_zoom_idle, alpha=hud_ibtn_alpha_hover)
                    action Jump("go_update_mhd_onehour")
                    hovered SetScreenVariable("tooltip_text", "Wait 60 minutes")
                    unhovered SetScreenVariable("tooltip_text", "")

            for stat in ["bravery", "lust", "mood", "beauty", "money"]:
                frame:
                    background None
                    hbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 20
                        imagebutton:
                            idle Transform(f"{img_btn_path}{stat}{idle_img_btn}", zoom=hud_ibtn_zoom_idle, alpha=hud_ibtn_alpha_idle)
                            hover Transform(f"{img_btn_path}{stat}{hover_img_btn}", zoom=hud_ibtn_zoom_idle, alpha=hud_ibtn_alpha_hover)
                            action [NullAction()]
                            hovered Show(f"{stat}_details_screen")
                            unhovered Hide(f"{stat}_details_screen")
                        if stat == "mortal_coil":
                            text f"[{stat}_text] / [max_{stat}_text]" yalign 0.5
                        else:
                            text f"[{stat}_text]" yalign 0.5

    if tooltip_text != "":
        frame:
            background "#0000007b"
            xalign 0.5
            yalign 0.25
            xsize 300
            padding (10, 5)
            text tooltip_text