from abc import ABC, abstractmethod
from enum import Enum


class CardType(Enum):
    CREATURE = "Creature"
    SPELL = "Spell"
    ARTIFACT = "Artifact"


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


# Card (Abstract Base Class)
class Card(ABC):
    def __init__(
        self, name: str, cost: int, rarity: Rarity, card_type: CardType
    ) -> None:
        if cost < 0:
            raise ValueError("cost must be >= 0")
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.card_type = card_type

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        raise NotImplementedError

    def get_card_info(self) -> dict:
        return self.__dict__.copy()

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost

    def __str__(self) -> str:
        return f"{self.name} ({self.cost})"
