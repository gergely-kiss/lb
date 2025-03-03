default active_buffs = []

label apply_mortal_coil_buff(buff_type="small"):
    if buff_type == "small":
        $ buff_amount = 2
        $ duration_minutes = 14  # 2 hours 13 minutes
    elif buff_type == "large":
        $ buff_amount = 10
        $ duration_minutes = (1 * 24 * 60) + (1 * 60) + 1  # 1 day 1 hour 1 minute
    else:
        return

    $ mortal_coil += buff_amount
    $ mortal_coil_text = str(mortal_coil)
    $ expiration_time = cumulative_minutes_passed + duration_minutes
    $ active_buffs.append({
        "stat": "mortal_coil", 
        "amount": buff_amount, 
        "expires": expiration_time
    })
    if in_screen:
        $ renpy.restart_interaction()
        $ renpy.pause()
    return

label apply_crimson_dare_buff(buff_type="small"):
    if buff_type == "small":
        $ buff_amount = 1
        $ duration_minutes = 13 
    elif buff_type == "large":
        $ buff_amount = 2
        $ duration_minutes = (1 * 24 * 60) 
    else:
        return

    $ crimson_dare += buff_amount
    $ crimson_dare_text = str(crimson_dare)
    $ expiration_time = cumulative_minutes_passed + duration_minutes
    $ active_buffs.append({
        "stat": "crimson_dare", 
        "amount": buff_amount, 
        "expires": expiration_time
    })
    if in_screen:
        $ renpy.restart_interaction()
        $ renpy.pause()
    return

label use_item(container, item_id):
    $ cont = Containers[container]
    if item_id not in cont:
        return 

    $ item, quantity = cont[item_id]

    $ new_quantity = quantity - 1
    if new_quantity <= 0:
        $ cont.pop(item_id)
    else:
        $ cont[item_id] = (item, new_quantity)

    if item.type == "mortal_coil_buff":
        call apply_mortal_coil_buff(item.subtype) from _call_apply_mortal_coil_buff
    elif item.type == "crimson_dare_buff":
        call apply_crimson_dare_buff(item.subtype) from _call_apply_crimson_dare_buff

    return