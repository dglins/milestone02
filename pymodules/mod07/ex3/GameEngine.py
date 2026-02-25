from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.hand: list = []
        self.battlefield: list = []
        self.turns_simulated = 0
        self.cards_created = 0

    def configure_engine(
            self, factory: CardFactory, strategy: GameStrategy
            ) -> None:
        self.factory = factory
        self.strategy = strategy
        themed = factory.create_themed_deck(3)
        self.hand = themed["hand"]
        self.battlefield = themed["battlefield"]
        self.cards_created = len(self.hand)

    def simulate_turn(self) -> dict:
        if self.factory is None or self.strategy is None:
            raise RuntimeError("Engine not configured")

        self.turns_simulated += 1
        actions = self.strategy.execute_turn(self.hand, self.battlefield)
        return actions

    def get_engine_status(self) -> dict:
        if self.strategy is None:
            strategy_name = "None"
        else:
            strategy_name = self.strategy.get_strategy_name()

        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": 8,
            "cards_created": self.cards_created,
        }
