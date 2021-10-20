class Cell:
    def __init__(self, parts):
        self.parts = parts

    def __add__(self, other):
        return Cell(self.parts + other.parts)

    def __sub__(self, other):
        diff = self.parts - other.parts
        if diff >= 0:
            return Cell(diff)
        else:
            print(f'ERROR!!!')

    def __mul__(self, other):
        return Cell(self.parts * other.parts)

    def __truediv__(self, other):
        return Cell(self.parts // other.parts)

    def make_order(self, count):
        s = ''
        for i in range(self.parts // count):
            s += '#' * count + '\n'
        s += '#' * (self.parts % count) + '\n'
        return s
    def __str__(self):
        return '%s' % self.parts


cell = Cell(50)
print(cell.make_order(7))
cell_2 = Cell(20)
print(cell_2.make_order(10))

print(cell - cell_2)
print(cell + cell_2)
print(cell * cell_2)
print(cell / cell_2)
print(cell_2 - cell)



