from Creature import Creature


class Captain(Creature):
    """
    General Description: Captain subclass of Creature that collects veggies.
    :param p1: x_coord
    :type p1: integer with X axis position of the Captain
    :param p2: y_coord
    :type p1: integer with Y axis position of the Captain
    :return: None.
    """

    def __init__(self, x_coord, y_coord):
        # superclass constructor is called
        super().__init__(x_coord, y_coord, "V")
        # An empty list called Collection is created to store the veggies that the Captain has collected
        self.Collection = []

    def addVeggie(self, veggie):
        # append the veggies to the empty list
        self.Collection.append(veggie)
