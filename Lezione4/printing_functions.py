def car_info(param1, param2, param3, param4):
    car = {'manufacturer': param1, 
           'model': param2, 
           'color': param3, 
           "optional": param4}
    return car

#######################################

def describe_city(param1, param2):
    message = f"{param1} is in {param2}"
    return message

######################################

def city_country(param1, param2):
    message = f"{param1}, {param2}"
    return message

#################################

def make_album(param1, param2, param3 = None):
    album = {'artist': param1, 'title': param2}
    if param3:
        album ['songs'] = param3
    return album