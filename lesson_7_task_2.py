from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5

class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def consumption(self):
        return 2 * self.h + 0.3

    def sum_consumption(self, list_suits):
        s = 0
        for suit in list_suits:
            s += suit.consumption
        return s

coat = Coat(80)
suit_1 = Suit(1.50)
suit_2 = Suit(1.85)
suit_3 = Suit(1.92)
suit_4 = Suit(1.65)
l_suits = [suit_4, suit_3, suit_2, suit_1]
print('Coat:', round(coat.consumption, 2), ' sq.m')
print('Suit:', round(suit_1.consumption, 2), ' sq.m')
print('Total Cloth:', round(suit_1.sum_consumption(l_suits), 2), ' sq.m')
