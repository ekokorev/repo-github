class car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Go!')
    def stop(self):
        print('Stop')
    def turn(self, direction):
        print('Car turned to %s' % direction)
    def get_speed(self):
        print('Current Speed: %s' % self.speed)


class town_car(car):

    def get_speed(self):
        super().get_speed()
        if self.speed > 60:
            print('Over Speed!')

class sport_car(car):
    pass

class work_car(car):
    def get_speed(self):
        super().get_speed()
        if self.speed > 40:
            print('Over Speed!')

class police_car(car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

town = town_car(90, 'Green', 'Town')
sport = sport_car(120, 'yello', 'Sport')
work = work_car(50, 'Blue', 'Work')
police = police_car(100, 'Grey', 'Police')

town.get_speed()
work.get_speed()
work.speed = 30
work.get_speed()

police.turn('Right')



