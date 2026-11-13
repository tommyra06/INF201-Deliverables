from character import Character


class Mage(Character):
    """Represents a mage, who uses mana for magic attacks."""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon = None, mana: int = 30, mana_max: int = 30) -> None:
        """Creates a mage with mana and max mana (default 30)."""
        super().__init__(name, hp_max, damage, weapon)
        self.mana, self.mana_max = mana, mana_max

    def attack(self, target) -> None:
        """Spell for double damage without the weapon if mana >= 10, otherwise a normal attack that restores 5 mana."""
        if self.mana >= 10:
            self.mana -= 10
            target.take_damage(self.damage * 2)
        else:
            self.mana = min(self.mana + 5, self.mana_max)
            super().attack(target)