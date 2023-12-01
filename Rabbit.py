from Creature import Creature


class Rabbit(Creature):
    """
    General Description: Rabbit subclass of Creature that eats veggies and gains points.
    :param p1: x_coord
    :type p1: integer with X axis position of the Rabbit
    :param p2: y_coord
    :type p1: integer with Y axis position of the Rabbit
    :return: None.
    """

    # Subclass Rabbit that inherits from Superclass Creature to keep track of the Rabbits that eats veggies
    def __init__(self, x_coord, y_coord):
        # superclass constructor is called for the creature Rabbit with symbol R
        super().__init__(x_coord, y_coord, "R")
