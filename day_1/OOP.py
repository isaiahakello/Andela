
class BoundsCheckingSpeed(object):
    def __init__(self, maxspeed):
        self.maxspeed = maxspeed

    def __get__(self, instance, cls):
        return instance._speed

    def __set__(self, instance, value):
        s = int(value)
        s = max(0, s)
        instance._speed = min(self.maxspeed, s)


class car(object):
    speed = BoundsCheckingSpeed(0)

    def __init__(self, name):
        self.name = name

    @property
    def speed_description(self):
        return '{name} the {type} is going {speed} kph!'.format(name=self.name,
                                                                type=self.__class__.__name__.lower(), speed=self.speed)


class Car(car):
    speed = BoundsCheckingSpeed(120)


class Porsche(car):
    speed = BoundsCheckingSpeed(120)


class Bus(car):
    speed = BoundsCheckingSpeed(80)


SaloonCar = Car('Mark X')
SaloonCar.speed = 120
print(SaloonCar.speed_description)

PorscheCarrera = Porsche('Porsche Carrera')
PorscheCarrera.speed = 110
print(PorscheCarrera.speed_description)

Bus = Bus('Andela')
Bus.speed = 100
print(Bus.speed_description)
