def ft_water_reminder()-> str:
    msg_need_water: str = "Water the plants!"
    msg_fine:   str = "Plants are fine"
    msg:    str = "We need to know the days!"
    last_watering: int = int(input("Days since last watering: "))
    if (last_watering > 2):
        msg = msg_need_water
    else:
        msg = msg_fine
    print(msg)
    return msg
