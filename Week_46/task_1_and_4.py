


class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10) -> None:
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
        

    def attack(self, target) -> None:
        """Activates take_damage function for target"""
        target.take_damage(self.damage)
        

    def take_damage(self, dmg_taken: int) -> None:
        """Lowers hp based of damage taken"""
        self._hp -= dmg_taken
        self._hp = max(self._hp, 0)
        self.alive_check()

    def heal(self) -> None:
        """Increases hp"""
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

    @property
    def is_alive(self) -> bool:
        """Checks if hp is below 0 and returns alive status"""
        return self._hp > 0

class Warrior(Character):
    """Represents the warrior subclass"""
    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, armor: int = 5):
        super().__init__(name, hp_max, damage)
        """
            Initialise the Character
    
            Args:
                name (str): The name of the character.
                hp_max (int): Max hit points (default = 100)
                damage (int): Damage delt when character attacks (default = 10)
                armor (int): Damage negated when character is attacked (default = 5)
        """
        self.armor = armor
    

    def take_damage(self, dmg_taken: int):
        """Lowers hp based of damage taken minus armor"""
        dmg_taken -= self.armor
        return super().take_damage(dmg_taken)

class Mage(Character):
    """Represents the mage subclass"""
    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, mana: int = 30, mana_max: int = 30):
        super().__init__(name, hp_max, damage)
        """
            Initialise the Character
            
            Args:
                name (str): The name of the character.
                hp_max (int): Max hit points (default = 100)
                damage (int): Damage delt when character attacks (default = 10)
                
        """
        self.mana = mana
        self.mana_max = mana_max

    def attack(self, target):
        """Deals different amount of damage based off of mana left"""
        base_dmg = self.damage
        if self.mana >= 10:
            self.mana -= 10
            self.damage *= 2
        else:
            self.mana += 5
            self.mana = min(self.mana, self.mana_max)

        try:
            return super().attack(target)
        finally:
            self.damage = base_dmg
        


brad = Character('brad')
pitt = Mage('pitt')

pitt.attack(brad) 
print(pitt.damage)   
print(brad._hp)
print(brad.is_alive())