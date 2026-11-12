import random


class Dice:
    """
    Represents a dice that can be rolled to get a random number n>=2, with a default value of 6.
    """

    def __init__(self, sides: int = 6) -> None:
        """
        Create a Dice with the specified number of sides, defaulting to 6.
        """
        
        if sides >= 2:
            self.sides = sides
        else:
            raise ValueError("Dice must have at least 2 sides.")

    def roll(self) -> int:
        """
        Rolls the dice and returns a random number between 1 and the number of sides.
        """
        
        return random.randint(1, self.sides)
    
    def __repr__(self) -> str:
        """
        Returns a string representation of the Dice object.
        """
        
        return f"Dice(sides={self.sides})"
    
    def __call__(self) -> int:
        """
        Allows the Dice object to be called like a function to roll it.
        """
        
        return self.roll()