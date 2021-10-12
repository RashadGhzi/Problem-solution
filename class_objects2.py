class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class bus (vehicle):
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity = 50)

a = bus("Volvo",180,20)
print("Bus name = ", a.name, "\nBus speed = ", a.max_speed, "\nBus mileage = ",a.mileage)
print(a.seating_capacity())

