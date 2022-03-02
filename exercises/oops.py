class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelS = Vehicle(200,20)
print(modelS.max_speed, modelS.mileage)