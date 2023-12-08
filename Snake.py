from Creature import Creature


class Snake(Creature):
    """
    General Description: Snake subclass of Creature that makes captain lose veggie points if it collides with Captain.
    :param p1: x_coord
    :type p1: integer with X axis position of the Snake
    :param p2: y_coord
    :type p1: integer with Y axis position of the Snake
    :return: None.
    """

    # Subclass Snake that inherits from Superclass Creature that can attack the Captain
    def __init__(self, x_coord, y_coord):
        # Superclass constructor is called for the creature Snake with symbol S
        super().__init__(x_coord, y_coord, "\033[0;31mS\033[0m")
