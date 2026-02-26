from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.Card import Rarity


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self._registry = {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }

    def get_supported_types(self) -> dict:
        return self._registry.copy()

    def create_creature(self, name_or_power: str | int | None = None):
        if name_or_power == "goblin" or name_or_power == "Goblin Warrior":
            return CreatureCard("Goblin Warrior", 2, Rarity.COMMON, 2, 2)
        return CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)

    def create_spell(self, name_or_power: str | int | None = None):
        return SpellCard("Lightning Bolt", 3, Rarity.RARE, "damage")

    def create_artifact(self, name_or_power: str | int | None = None):
        return ArtifactCard(
            "Mana Ring", 2, Rarity.RARE, 10, "+1 mana per turn"
            )

    def create_themed_deck(self, size: int) -> dict:
        hand = [
            self.create_creature("dragon"),
            self.create_creature("goblin"),
            self.create_spell(None)
            ]
        battlefield: list = []
        return {"hand": hand[:size], "battlefield": battlefield}
