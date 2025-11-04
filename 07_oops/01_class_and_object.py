class Car:
    def __init__(self ,brand , model):
        self.Brand = brand
        self.Model = model

    def full_name(self):
        return f"{self.Brand} {self.Model}"
    

def ElectricCar(Car):
    def __init__(self , brand , model , battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_car = Car("Mahindra" , "BE6")
# print(my_car.Brand)
# print(my_car.Model)
print(my_car.full_name())

my_new_car = Car("RangeRover" , "Evoque")
# print(my_new_car.Brand)
# print(my_new_car.Model)
print(my_new_car.full_name())