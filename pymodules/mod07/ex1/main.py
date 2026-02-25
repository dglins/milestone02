from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")

    deck = Deck()
    deck.add_card(CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3, Rarity.RARE, "damage"))
    deck.add_card(
        ArtifactCard("Mana Crystal", 2, Rarity.COMMON, 10, "+1 mana per turn")
    )

    print(f"Deck stats: {deck.get_deck_stats()}")
    print("Drawing and playing cards:\n")

    deck.shuffle()
    game_state = {"mana": 10}

    while True:
        try:
            card = deck.draw_card()
        except IndexError:
            break

        print(f"Drew: {card.name} ({card.card_type.value})")
        print(f"Play result: {card.play(game_state)}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
