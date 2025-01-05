class Car(object):
    color = "white"

    def __init__(self, maximum_speed, mileage):
        self.maximum_speed = maximum_speed
        self.mileage = mileage
        self.seats = None

    def set_seating_capacity(self, seats):
        self.seats = seats

    def display_properties(self):
        print("the color of car is", self.color)
        print("the maximum speed is:", self.maximum_speed)
        print("the mileage is:", self.mileage)
        print("seating capacity is:", self.seats)


Vehicle1 = Car(200, 20)
Vehicle1.set_seating_capacity(5)
Vehicle1.display_properties()

Vehicle2 = Car(180, 25)
Vehicle2.set_seating_capacity(4)
Vehicle2.display_properties()


