from random import randint

class Die():
    """Basic die class"""

    def __init__(self, num_sides = 6):
        """By default there is 6 sides"""
        self.num_sides = num_sides

    def roll(self):
        """Random roll"""
        return randint(1, self.num_sides)
