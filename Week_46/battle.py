from character import Character


class Battle:
    """Manages a turn-based battle between two characters."""

    def __init__(self, hero: Character, enemy: Character) -> None:
        """Creates a battle where the hero attacks first."""
        self.hero, self.enemy, self.rounds = hero, enemy, 0

    def play_round(self) -> None:
        """The hero attacks, and the enemy attacks back if it is still alive."""
        self.rounds += 1
        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self, max_rounds: int = 1000) -> Character | None:
        """Plays rounds until one character is defeated, and returns the winner, or None after max_rounds."""
        while self.hero.is_alive and self.enemy.is_alive:
            if self.rounds == max_rounds:
                return None
            self.play_round()
        return self.hero if self.hero.is_alive else self.enemy