def ft_count_harvest_recursive(
    days_until_harvest: int | None = None, day: int = 1
) -> None:
    """Count down the days to harvest recursively."""
    if days_until_harvest is None:
        days_until_harvest = int(input("Days until harvest: "))

    if days_until_harvest <= 0:
        print("Harvest time!")
        return

    print(f"Day {day}")
    ft_count_harvest_recursive(days_until_harvest - 1, day + 1)
