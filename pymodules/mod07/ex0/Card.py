from abc import ABC, abstractmethod


# Card (Abstract Base Class)
class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        raise NotImplementedError

    def get_card_info(self) -> dict:
        return self.__dict__

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
