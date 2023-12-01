from FieldInhabitant import FieldInhabitant


class Veggies(FieldInhabitant):
    """
    General Description: Veggies subclass of FieldInhabitant.
    :param p1: Name
    :type p1: string with name of animal
    :param p2: symbol
    :type p1: Character of the animal
    :param p3: points
    :type p3: integer to indicate the worth of vegetable
    :return: None.
    """

    def __init__(self, name, symbol, points):
        super().__init__(symbol)
        self._name = name
        self._points = points

    # override the __str__ function for legible output
    def __str__(self):
        print(f"The vegetables are : \n {self.symbol}.\n {self._name} \t {self._points} points ")

    # getter and setter functions for name parameter
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # getter and setter function for the points parameter
    def get_points(self):
        return self._points

    def set_points(self, points):
        self._points = points
