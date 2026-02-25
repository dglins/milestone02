from ex0.Card import Card, CardType, Rarity
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: Rarity) -> None:
        super().__init__(name, cost, rarity, CardType.CREATURE)
        self.attack_power = 5
        self.block_power = 3
        self.mana_pool = 4
        self.health = 10

    def play(self, game_state: dict) -> dict:
        result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "None",
        }
        if self.is_playable(game_state["mana"]):
            game_state["mana"] -= self.cost
            result["effect"] = "Elite creature enters battlefield"
        return result

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": str(target),
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(self.block_power, max(0, incoming_damage))
        taken = max(0, incoming_damage - blocked)
        self.health -= taken
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "block": self.block_power,
            "health": self.health,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_used = 4
        self.mana_pool = max(0, self.mana_pool - mana_used)
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_used,
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana_pool += amount
        return {"channeled": amount, "total_mana": self.mana_pool}

    def get_magic_stats(self) -> dict:
        return {"mana_pool": self.mana_pool}
