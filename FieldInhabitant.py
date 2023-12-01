
class FieldInhabitant:
    """
    General Description: FieldInhibitant superclass takes in the parameter symbol as the animals in farm.
    :param p1: symbol
    : type p1: character to indicate animal/captain
    :return: None
    """
    def __init__(self, symbol):
        self._symbol = symbol

    # Getter and setter function for the symbol parameter
    def get_symbol(self):
        return self._symbol

    def set_symbol(self, symbol):
        self._symbol = symbol
