from ex0.Card import Card, Rarity, CardType


class CreatureCard(Card):
    def __init__(
            self, name: str, cost: int, rarity: Rarity,
            attack: int, health: int
            ) -> None:
        super().__init__(name, cost, rarity, CardType.CREATURE)
        if attack <= 0 or health <= 0:
            raise ValueError("attack and health must be > 0")
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        print(f"Playing {self.name} with {game_state['mana']} mana available:")
        playable = self.is_playable(game_state["mana"])
        print(f"Playable: {playable}")

        result = {
            "card_played": self.name, "mana_used": self.cost, "effect": "None"
            }
        if playable:
            game_state["mana"] -= self.cost
            result["effect"] = "Creature summoned to battlefield"
        return result

    def attack_target(self, target: "CreatureCard") -> dict:
        print(f"{self.name} attacks {target.name}:")
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack,
            "combat_type": "melee",
        }
