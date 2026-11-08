


class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, is_alive: bool = True) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.is_alive = is_alive

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        target.take_damage(self.damage)
        

    def take_damage(self, dmg_taken: int) -> None:
        self._hp -= dmg_taken
        self._hp = max(self._hp, 0)
        self.alive_check()

    def heal(self) -> None:
        self._hp += 10
        self._hp = min(self._hp, self.hp_max)

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"


    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    def alive_check(self) -> bool:
        if self._hp > 0:
            self.is_alive = True
        else:
            self.is_alive = False
        return(self.is_alive)

class Warrior(Character):
    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, is_alive: bool = True, armor: int = 5):
        super().__init__(name, hp_max, damage, is_alive)
        self.armor = armor

    def take_damage(self, dmg_taken):
        dmg_taken -= self.armor
        return super().take_damage(dmg_taken)

class Mage(Character):
    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, is_alive: bool = True, mana: int = 30, mana_max: int = 30):
        super().__init__(name, hp_max, damage, is_alive)
        self.mana = mana
        self.mana_max = mana_max

    def attack(self, target):
        if self.mana >= 10:
            self.mana -= 10
            self.damage *= 2
            return super().attack(target)
        else:
            self.mana += 5
            self.mana = min(self.mana, self.mana_max)
        


brad = Character('brad')
pitt = Mage('pitt')

pitt.attack(brad) 
print(pitt.damage)   
print(brad._hp)
