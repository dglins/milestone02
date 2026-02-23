from Card import Card


# CreatureCard (Concrete Implementation)
class CreatureCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.mana = 6

    def set_mana(self, change_mana):
        self.mana = change_mana

    def play(self, game_state: dict) -> dict:
        play_result = {'card_played': self.name,
                       'mana_used': self.cost,
                       'effect': 'None'}
        playable = self.is_playable(game_state['mana'])
        if playable:
            self.mana -= self.cost
            play_result['effect'] = 'Creature summoned to battlefield'
        return play_result

    def attack_target(self, target: Card) -> dict:
        enemy_state = target.get_card_info()
        attack_result = {
            'attacker': self.name, 'target': enemy_state['name'],
            'damage_dealt': self.attack, 'combat_resolved': False}
        if enemy_state['health'] <= self.attack:
            attack_result['combat_resolved'] = True
        return attack_result

    def _validade_health(self):
        return self.health > 0

    def _validade_attack(self):
        return self.attack > 0
