from abc import ABC, abstractmethod


# Combatable (Abstract Interface)
class Combatable(ABC):
    @abstractmethod
    def attack(self, target) -> dict:
        raise NotImplementedError("Please Implement the method.")

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        raise NotImplementedError("Please Implement the method.")

    @abstractmethod
    def get_combat_stats(self) -> dict:
        raise NotImplementedError("Please Implement the method.")
