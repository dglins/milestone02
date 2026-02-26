from ex0.Card import Card, CardType, Rarity


class SpellCard(Card):
    def __init__(
            self, name: str, cost: int, rarity: Rarity, effect_type: str
            ) -> None:
        super().__init__(name, cost, rarity, CardType.SPELL)
        self.effect_type = effect_type

    def resolve_effect(self, targets: list) -> dict:
        return {"effect_type": self.effect_type, "targets": targets}

    def play(self, game_state: dict) -> dict:
        result = {
            "card_played": self.name, "mana_used": self.cost, "effect": "None"
            }
        if self.is_playable(game_state["mana"]):
            game_state["mana"] -= self.cost
            if self.effect_type == "damage":
                result["effect"] = "Deal 3 damage to target"
            elif self.effect_type == "heal":
                result["effect"] = "Heal 3 health"
            else:
                result["effect"] = f"Spell effect: {self.effect_type}"
        return result
