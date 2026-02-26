from ex3.GameStrategy import GameStrategy
from ex0.Card import CardType


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played: list[str] = []
        mana_used = 0
        damage_dealt = 0
        targets_attacked = ["Enemy Player"]

        creatures = [c for c in hand if c.card_type == CardType.CREATURE]
        spells = [c for c in hand if c.card_type == CardType.SPELL]

        creatures.sort(key=lambda c: c.cost)
        if creatures:
            c = creatures[0]
            hand.remove(c)
            battlefield.append(c)
            cards_played.append(c.name)
            mana_used += c.cost
            damage_dealt += getattr(c, "attack", 0)

        if spells:
            s = spells[0]
            hand.remove(s)
            cards_played.append(s.name)
            mana_used += s.cost
            damage_dealt += 6

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt,
        }
