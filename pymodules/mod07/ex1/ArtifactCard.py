from ex0.Card import Card, CardType, Rarity


class ArtifactCard(Card):
    def __init__(
            self, name: str, cost: int, rarity: Rarity,
            durability: int, effect: str
            ) -> None:
        super().__init__(name, cost, rarity, CardType.ARTIFACT)
        if durability <= 0:
            raise ValueError("durability must be > 0")
        self.durability = durability
        self.effect = effect

    def activate_ability(self) -> dict:
        return {"effect": self.effect, "durability": self.durability}

    def play(self, game_state: dict) -> dict:
        result = {
            "card_played": self.name, "mana_used": self.cost, "effect": "None"
            }
        if self.is_playable(game_state["mana"]):
            game_state["mana"] -= self.cost
            result["effect"] = f"Permanent: {self.effect}"
        return result
