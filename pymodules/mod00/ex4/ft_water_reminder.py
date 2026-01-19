def ft_water_reminder() -> str:
    msg_need_water: str = "Water the plants!"
    msg_fine: str = "Plants are fine"
    msg: str = "We need to know the days!"
    last_watering: int = int(input("Days since last watering: "))
    msg = msg_need_water if last_watering > 2 else msg_fine
    print(msg)
    return msg
