class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.speed = 0

    def start(self, speed):
        self.speed += speed

    def state(self):
        print ("name",self.make, self.model, self.speed)

car1 = Car("Ford", "Mustang", 1999)
car1.start(30)
car1.state()