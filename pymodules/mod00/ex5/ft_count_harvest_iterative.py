def ft_count_harvest_iterative() -> None:
    msg: str = "Harvest time!"
    days_until_harvest: int = int(input("Days until harvest: "))
    for day in range(days_until_harvest):
        print(f"Day {day + 1}")
    print(msg)
