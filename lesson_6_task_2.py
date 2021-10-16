class road:
    def __init__(self, l, w):
        self._l = l
        self._w = w

    def get_w(self, mass, thick):
        return self._l * self._w * mass * thick
r = road(5000, 20)
print('Required mass of asphalt: %s' % r.get_w(25, 5), 'kg')
