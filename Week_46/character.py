class Character:
    """Represents a character in the RPG."""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon = None) -> None:
        """Creates a character with a name, max HP, base damage and an optional weapon."""
        self.name, self.hp_max, self.damage, self.weapon = name, hp_max, damage, weapon
        self._hp = hp_max

    def attack(self, target) -> None:
        """Damages the target, using the weapon's damage roll if one is equipped."""
        target.take_damage(self.weapon.roll_damage() if self.weapon else self.damage)

    def take_damage(self, dmg_taken: int) -> None:
        """Lowers HP by the damage taken, but not below 0."""
        self._hp = max(self._hp - dmg_taken, 0)

    def heal(self) -> None:
        """Increases HP by 10, but not above hp_max."""
        self._hp = min(self._hp + 10, self.hp_max)

    def __repr__(self) -> str:
        """Returns a representation of the character."""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"

    @property
    def hp(self) -> int:
        """Read-only HP."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Returns True if HP is above 0."""
        return self._hp > 0