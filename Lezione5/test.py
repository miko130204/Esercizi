def car_info(param1, param2, param3, param4):
    car = {'manufacturer': param1, 
           'model': param2, 
           'color': param3, 
           "optional": param4}
    return car

param1 = input("Manufacturer: ")
param2 = input("Model: ")
param3 = input("Color: ")
param4 = input("Optional: ")

print(car_info(param1, param2, param3, param4))