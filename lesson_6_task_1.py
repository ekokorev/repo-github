from time import sleep

class traff_light:
    colors = ('Red', 'Yello', 'Green')
    delay = (5, 2, 7)

    def __init__(self):
        self.__color = 'Green'
    def working(self):
           while True:
               for i in self.colors:
                   self.__color = i
                   print(self.__color)
                   sleep(self.delay[self.colors.index(self.__color)])

tr_light = traff_light()
tr_light.working()


