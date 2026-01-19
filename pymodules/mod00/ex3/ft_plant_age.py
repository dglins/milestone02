def ft_plant_age() -> str:
    """Checks if it is ready to harvest"""
    msg_harvest: str = "Plant is ready to harvest!"
    msg_need_grow: str = "Plant needs more time to grow."
    age: int = int(input("Enter plant age in days: "))
    msg: str = msg_harvest if age > 60 else msg_need_grow
    print(msg)
    return msg
