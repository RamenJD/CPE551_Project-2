from FieldInhabitant import FieldInhabitant


class Creature(FieldInhabitant):
    """
    General Description: Creature subclass of FieldInhabitant that keeps track of the field animals.
    :param p1: x_coord
    :type p1: integer with X axis position of the creatures
    :param p2: y_coord
    :type p1: integer with Y axis position of the creatures
    :param p3: symbol
    :type p3: Character to indicate the animal
    :return: None.
    """

    # Subclass Creature from Superclass FieldInhabitant to store positions of different animals
    def __init__(self, x_coord, y_coord, symbol):
        super().__init__(symbol)
        self._x_coord = x_coord
        self._y_coord = y_coord

    # Getter and Setter function for the X coordinate
    def get_x_coord(self):
        return self._x_coord

    def set_x_coord(self, x_coord):
        self._x_coord = x_coord

    # Getter and Setter function for the Y Coordinate
    def get_y_coord(self):
        return self._y_coord

    def set_y_coord(self, y_coord):
        self._y_coord = y_coord
