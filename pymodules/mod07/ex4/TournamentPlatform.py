class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: dict[str, object] = {}
        self.matches_played = 0

    def register_card(self, card) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        self.matches_played += 1
        c1 = self.cards[card1_id]
        c2 = self.cards[card2_id]

        winner = c1 if c1.rating >= c2.rating else c2
        loser = c2 if winner is c1 else c1

        winner.update_wins(1)
        loser.update_losses(1)

        winner.rating += 16
        loser.rating -= 16

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating,
        }

    def get_leaderboard(self) -> list:
        ordered = sorted(
            self.cards.values(), key=lambda c: c.rating, reverse=True
            )
        return ordered

    def generate_tournament_report(self) -> dict:
        if not self.cards:
            avg = 0
        else:
            avg = sum(c.rating for c in self.cards.values()) // len(self.cards)

        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": avg,
            "platform_status": "active",
        }
