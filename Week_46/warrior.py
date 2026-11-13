from character import Character


class Warrior(Character):
    """Represents a warrior, whose armor reduces incoming damage."""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon = None, armor: int = 5) -> None:
        """Creates a warrior with armor (default 5)."""
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor

    def take_damage(self, dmg_taken: int) -> None:
        """Takes damage reduced by armor, but never below 0."""
        super().take_damage(max(dmg_taken - self.armor, 0))