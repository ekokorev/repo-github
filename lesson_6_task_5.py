class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Begin drawing!')

class Pen(Stationery):
    def draw(self):
        print('Begin drawing with pen! %s' % self.title)

class Pencil(Stationery):
    def draw(self):
        print('Begin drawing with pencil! %s' % self.title)

class Handle(Stationery):
    def draw(self):
        print('Begin drawing with handle! %s' % self.title)

pen = Pen('Hello')
pencil = Pencil('World')
handle = Handle('Python')
for i in (pen, pencil, handle):
    i.draw()



