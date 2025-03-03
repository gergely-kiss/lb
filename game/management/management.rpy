default bravery = 0
default bravery_text = [bravery]
default lust = 0
default lust_text = [lust]
default mood = 0
default mood_text = [mood]
default money = 0
default money_text = [money]
default pennies_text = [money]
default beauty = 0
default beauty_text = [beauty]
default beauty_allure = 0
default beauty_clothing = 0
default beauty_makeup = 0
default beauty_lust = 0
default beauty_allure_text = [beauty_allure]
default beauty_clothing_text = [beauty_clothing]
default beauty_makeup_text = [beauty_makeup]
default beauty_lust_text = [beauty_lust]
default mood_hunger = 0
default mood_resting = 0
default mood_hygenic = 0
default mood_emotional = 0
default mood_hunger_text = "[mood_hunger]" 
default mood_resting_text = "[mood_resting]" 
default mood_hygenic_text = "[mood_hygenic]" 
default mood_emotional_text = "[mood_emotional]" 
default cumulative_minutes_passed = 0
default minutes_processed = 0
default hunger_processed = 0
default resting_processed = 0
default hygien_processed = 0
default current_week = 0
default current_day = 0
default current_hour = 0
default current_minute = 0
default current_week_text = ""
default current_day_text = ""
default current_hour_text = ""
default current_minute_text = ""
default is_eating = False
default is_sleeping = False
default is_cleaning_herself = False
default in_screen = False
default can_change_outfit = False
default time_to_move_items = 0


label update_money(inc=0):
    $ money += inc
    $ money_text = f"{money:04d}"
    if in_screen:
            $ renpy.restart_interaction()
            $ renpy.pause()
    return


label update_bravery(inc=0):
    $ bravery += inc
    $ bravery_text = bravery
    if in_screen:
        $ renpy.restart_interaction()
        $ renpy.pause()
    return

label update_mood(mood_type="", inc=0):
    if mood_type == "hunger":
        $ mood_hunger += inc
        $ mood_hunger = max(-24, min(24, mood_hunger))
        $ mood_hunger_text = str(mood_hunger)

    elif mood_type == "resting":
        $ mood_resting += inc
        $ mood_resting = max(-24, min(24, mood_resting))
        $ mood_resting_text = str(mood_resting)

    elif mood_type == "hygenic":
        $ mood_hygenic += inc
        $ mood_hygenic = max(-24, min(24, mood_hygenic))
        $ mood_hygenic_text = str(mood_hygenic)

    elif mood_type == "emotional":
        $ mood_emotional += inc
        $ mood_emotional = max(-24, min(24, mood_emotional))
        $ mood_emotional_text = str(mood_emotional)

    # Re-sum
    $ mood = (mood_hunger + mood_resting  + mood_hygenic + mood_emotional)
    $ mood_text = str(mood)

    # Force the screen to refresh:
    if in_screen:
        $ renpy.restart_interaction()
        $ renpy.pause()
    return

label update_lust(inc=0):
    # Compute new value
    $ new_val = lust + inc
    $ new_val = max(0, min(9, new_val))  # clamp between 0 and 9
    $ lust = new_val

    # Color-coded logic
    if lust == 0:
        $ lust_text = "{color=#FFFFFF}%d{/color}" % lust
    elif lust == 1:
        $ lust_text = "{color=#FFE6E6}%d{/color}" % lust
    elif lust == 2:
        $ lust_text = "{color=#FFCCCC}%d{/color}" % lust
    elif lust == 3:
        $ lust_text = "{color=#FFB3B3}%d{/color}" % lust
    elif lust == 4:
        $ lust_text = "{color=#FF9999}%d{/color}" % lust
    elif lust == 5:
        $ lust_text = "{color=#FF8080}%d{/color}" % lust
    elif lust == 6:
        $ lust_text = "{color=#FF6666}%d{/color}" % lust
    elif lust == 7:
        $ lust_text = "{color=#FF4D4D}%d{/color}" % lust
    elif lust == 8:
        $ lust_text = "{color=#FF3333}%d{/color}" % lust
    elif lust == 9:
        $ lust_text = "{color=#FF0000}%d{/color}" % lust
    $ beauty_lust = lust
    $ beauty_lust_text = str(beauty_lust)
    $ beauty = (beauty_allure + beauty_clothing + beauty_makeup + beauty_lust)
    $ beauty_text = str(beauty)
    if in_screen:
        $ renpy.restart_interaction()
        $ renpy.pause()
    return

label update_beauty(va_type="", inc=0):
    if va_type == "allure":
        $ beauty_allure += inc
        $ beauty_allure_text = str(beauty_allure)
    elif va_type == "clothing":
        $ beauty_clothing += inc
        $ beauty_clothing_text = str(beauty_clothing)
    elif va_type == "makeup":
        $ beauty_makeup += inc
        $ beauty_makeup_text = str(beauty_makeup)
    elif va_type == "lust":
        $ beauty_lust += inc
        $ beauty_lust_text = str(beauty_lust)

    # Recalc total
    $ beauty = (beauty_allure + beauty_clothing + beauty_makeup + beauty_lust)
    $ beauty_text = str(beauty)

    if in_screen:
        $ renpy.restart_interaction()
        $ renpy.pause()
    return

label go_update_mhd_twominutes:
    call update_mhd(2, 0, 0)
    return

label go_update_mhd_fiveminutes:
    call update_mhd(5, 0, 0)
    return

label go_update_mhd_thirteenminutes:
    call update_mhd(13, 0, 0)
    return

label go_update_mhd_onehour:
    call update_mhd(0, 1, 0)
    return

screen fade_black(sleep_duration=1):  # Takes the sleep time as an argument
    add "#000" at fade_effect(sleep_duration)

label update_mhd(added_minute=0, added_hour=0, added_day=0):
    if time_to_move_items > 0:
        $ time_to_move_items = 0
    # Add the minutes
    $ total_added = (added_day * 24 * 60) + (added_hour * 60) + added_minute
    $ cumulative_minutes_passed += total_added

    # Now compute new day/hour/minute
    $ total_current = (current_day * 24 * 60) + (current_hour * 60) + current_minute + total_added
    $ updated_total_days = total_current // (24 * 60)
    $ remainder = total_current % (24 * 60)
    $ updated_hour = remainder // 60
    $ updated_minute = remainder % 60

    # Update week/day
    $ current_week += updated_total_days // 7
    $ current_day = updated_total_days % 7
    $ current_hour = updated_hour
    $ current_minute = updated_minute

    # Day-of-week text
    if current_day == 0:
        $ current_day_text = "Sun"
    elif current_day == 1:
        $ current_day_text = "Mon"
    elif current_day == 2:
        $ current_day_text = "Tue"
    elif current_day == 3:
        $ current_day_text = "Wed"
    elif current_day == 4:
        $ current_day_text = "Thu"
    elif current_day == 5:
        $ current_day_text = "Fri"
    elif current_day == 6:
        $ current_day_text = "Sat"

    $ current_week_text = "%02d" % current_week
    $ current_hour_text = "%02d" % current_hour
    $ current_minute_text = "%02d" % current_minute

    python:
        for buff in list(active_buffs):
            if buff["expires"] <= cumulative_minutes_passed:
                if buff["stat"] == "mood":
                    mood -= buff["amount"]
                    mood_text = str(mood)
                elif buff["stat"] == "lust":
                    lust -= buff["amount"]
                    lust_text = str(lust)
                    mood_text = str(mood)
                elif buff["stat"] == "beauty":
                    beauty -= buff["amount"]
                    beauty_text = str(beauty)
                elif buff["stat"] == "mood_hunger":
                    mood_hunger -= buff["amount"]
                    mood_hunger_text = str(mood_hunger)
                elif buff["stat"] == "mood_resting":
                    mood_resting -= buff["amount"]
                    mood_resting_text = str(mood_resting)
                elif buff["stat"] == "mood_resting":
                    mood_hygenic -= buff["mood_hygenic"]
                    mood_hygenic_text = str(mood_hygenic)
                elif buff["stat"] == "mood_emotional":
                    mood_emotional -= buff["mood_emotional"]
                    mood_emotional_text = str(mood_emotional)
                elif buff["stat"] == "beauty_allure":
                    beauty_allure -= buff["beauty_allure"]
                    beauty_allure_text = str(beauty_allure)
                elif buff["stat"] == "beauty_makeup":
                    beauty_makeup -= buff["beauty_makeup"]
                    beauty_makeup_text = str(beauty_makeup)
                active_buffs.remove(buff)
    # Process hunger, rest, etc.
    while (cumulative_minutes_passed - hunger_processed) >= 65:
        if not is_eating:
            $ mood_hunger -= 1
            $ mood_hunger = max(-24, min(24, mood_hunger))
            $ mood_hunger_text = str(mood_hunger)
        $ hunger_processed += 65

    while (cumulative_minutes_passed - resting_processed) >= 116:
        if not is_sleeping:
            $ mood_resting -= 1
            $ mood_resting = max(-24, min(24, mood_resting))
            $ mood_resting_text = str(mood_resting)
        $ resting_processed += 116

    while (cumulative_minutes_passed - hygien_processed) >= 104:
        if not is_cleaning_herself:
            $ mood_hygenic -= 1
            $ mood_hygenic = max(-24, min(24, mood_hygenic))
            $ mood_hygenic_text = str(mood_hygenic)
        $ hygien_processed += 104

    if is_sleeping:
        if mood_resting < 0:
            $ mood_resting += int(added_hour)
            if mood_resting > 0:
                $ mood_resting = 0
        $ mood_resting_text = str(mood_resting)
        $ is_sleeping = False

    $ mood = (mood_hunger + mood_resting  + mood_hygenic + mood_emotional)
    $ mood_text = str(mood)

    if in_screen:
        $ renpy.restart_interaction()
        $ renpy.pause()
    return
    