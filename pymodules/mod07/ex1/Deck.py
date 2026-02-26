from random import shuffle
from ex0.Card import Card, CardType


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop()

    def get_deck_stats(self) -> dict:
        total = len(self.cards)
        creatures = sum(
            1 for c in self.cards if c.card_type == CardType.CREATURE
            )
        spells = sum(
            1 for c in self.cards if c.card_type == CardType.SPELL
            )
        artifacts = sum(
            1 for c in self.cards if c.card_type == CardType.ARTIFACT
            )
        avg_cost = (sum(c.cost for c in self.cards) / total) if total else 0.0

        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": round(avg_cost, 1),
        }
