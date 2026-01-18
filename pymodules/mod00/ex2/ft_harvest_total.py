def ft_harvest_total()-> int:
    total:  int = 0
    day1:   int = int(input(f"Day 1 harvest: "))
    day2:   int = int(input(f"Day 2 harvest: "))
    day3:   int = int(input(f"Day 3 harvest: "))
    total = day1 + day2 + day3
    print(f"Total harvest: {total}")
    return total
