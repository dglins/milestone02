from ex0.Card import Card, CardType, Rarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
            self, card_id: str, name: str,
            cost: int, rarity: Rarity, rating: int
            ) -> None:
        super().__init__(name, cost, rarity, CardType.CREATURE)
        self.card_id = card_id
        self.rating = rating
        self.wins = 0
        self.losses = 0
        self.attack_power = 5

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name, "mana_used": self.cost,
            "effect": "Tournament card played"
            }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name, "target": str(target),
            "damage": self.attack_power, "combat_type": "melee"
            }

    def defend(self, incoming_damage: int) -> dict:
        blocked = 1
        taken = max(0, incoming_damage - blocked)
        return {
            "defender": self.name, "damage_taken": taken,
            "damage_blocked": blocked, "still_alive": True
            }

    def get_combat_stats(self) -> dict:
        return {"attack": self.attack_power}

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {"rating": self.rating, "record": f"{self.wins}-{self.losses}"}

    def get_tournament_stats(self) -> dict:
        return {
            "id": self.card_id,
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
        }
