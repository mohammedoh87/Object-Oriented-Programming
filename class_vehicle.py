class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
model_x = vehicle(240, 18)
print("The max_speed is ", model_x.max_speed)
print("The mileage is ", model_x.mileage)

model_y = vehicle(320,20)
print("The max_speed is ", model_y.max_speed)
print("The mileage is ", model_y.mileage)


