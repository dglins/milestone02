def ft_plant_age()-> None:
    msg_harvest:    str = "Plant is ready to harvest!"
    msg_need_grow:  str = "Plant needs more time to grow."
    msg:    str = "We need to know the age!"
    age:    int = int(input("Enter plant age in days: "))
    if (age > 60):
        msg = msg_harvest
    else:
        msg = msg_need_grow
    print(msg)
    return msg
