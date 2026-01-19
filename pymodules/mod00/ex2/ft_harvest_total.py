def ft_harvest_total() -> int:
    """Calculates the total harvest within the 3 days asked"""
    total: int = 0
    day1: int = int(input("Day 1 harvest: "))
    day2: int = int(input("Day 2 harvest: "))
    day3: int = int(input("Day 3 harvest: "))
    total = day1 + day2 + day3
    print(f"Total harvest: {total}")
    return total
