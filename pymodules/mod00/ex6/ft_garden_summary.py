def ft_garden_summary() -> tuple[str, str, str]:
    """Status of the garden"""
    name: str = input("Enter garden name: ")
    qtd_plants: str = input("Enter number of plants: ")
    msg: str = "Status: Growing well!"
    print(f"Garden: {name}")
    print(f"Plants: {qtd_plants}")
    print(msg)
    return name, qtd_plants, msg
