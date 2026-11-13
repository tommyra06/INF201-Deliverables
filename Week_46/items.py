from dice import Dice


class Weapon:
    """Represents a weapon that uses a Dice to decide its damage."""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """Creates a weapon with a name and a damage dice."""
        self.name, self.damage_dice = name, damage_dice

    def roll_damage(self) -> int:
        """Rolls the damage dice and returns the damage dealt."""
        return self.damage_dice.roll()

    def __repr__(self) -> str:
        """Returns a representation of the weapon."""
        return f"Weapon(name={self.name!r}, damage_dice={self.damage_dice!r})"