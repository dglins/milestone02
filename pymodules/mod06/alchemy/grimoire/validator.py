def validate_ingredients(ingredients: str) -> str:
    lowered = ingredients.lower()
    is_valid = any(
        token in lowered
        for token in ("fire", "water", "earth", "air")
        )
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
