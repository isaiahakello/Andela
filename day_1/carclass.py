class Car(object):
  speed = 0

  def __init__(self, name='Suv', model='cadillac', vehicle_type=suv):
    self.name = name
    self.model = model
    self.vehicle_type = vehicle_type


    if self.name in ['range', 'rover']:
      self.num_of_doors = 2
    else:
      self.num_of_doors = 4

    if self.vehicle_type == 'sport':
      self.num_of_wheels = 8
    else:
      self.num_of_wheels = 4


  def is_saloon(self):
    if self.vehicle_type is not 'sport':
        self.vehicle_type == 'ferrari'
        return True
    return False

  def drive(self, moving_speed):
    if moving_speed == 3:
      Car.speed = 1000
    elif moving_speed == 7:
      Car.speed = 77

    return self
