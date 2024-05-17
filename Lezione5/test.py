import random

def print_race(hare_pos, tortoise_pos):
    for i in range(70):
        if i == hare_pos and i == tortoise_pos:
            print("OUCH!!!", end=" ")
        elif i == hare_pos:
            print("H", end = " ")
        elif i == tortoise_pos:
            print("T", end = " ")
        else:
            print("_", end = " ")

def tortoise_move(weather, energy):
    move = random.randint(1, 10)
    if weather == "sunny":
        if move <= 5:
            energy -= 5
            return 3
        elif move <= 7:
            energy -= 10
            return -6
        else:
            energy -= 3
            return 1
    elif weather == "rainy":
        if move <= 5:
            return 2
        elif move <= 7:
            return -7
        else:
            return 0
    
    
def hare_move(weather, energy):
    move = random.randint(1, 10)
    if weather == "sunny":
        if move <= 2:
            return 0
        elif move <= 4:
            return 9
        elif move <= 5:
            return -12
        elif move <= 8:
            return 1
        else:
            return -2
    elif weather == "rainy":
        if move <= 2:
            return -2
        elif move <= 4:
            return 7
        elif move <= 5:
            return -14
        elif move <= 8:
            return -1
        else:
            return -4
    
def print_race(hare_pos, tortoise_pos):
    for i in range(70):
        if i == hare_pos and i == tortoise_pos:
            print("OUCH!!!", end=" ")
        elif i == hare_pos:
            print("H", end = " ")
        elif i == tortoise_pos:
            print("T", end = " ")
        else:
            print("_", end = " ")


print("BANG !!!!! AND THEY'RE OFF !!!!!")

hare_position = 1
tortoise_position = 1
weather = "sunny"
clock = 0
hare_energy = 100
tortoise_energy = 100


while hare_position <= 70 and tortoise_position <= 70:
    hare_position += hare_move(weather, hare_energy)
    if hare_position < 1:
        hare_position = 1
    tortoise_position += tortoise_move(weather, tortoise_energy)
    if tortoise_position < 1:
        tortoise_position = 1

    print_race(hare_position, tortoise_position)

    clock += 1
    if clock % 10 == 0:
        weather = random.choice(["sunny", "rainy"])

    if hare_position >= 70 and tortoise_position >= 70:
        print("\nIT'S A TIE.")
        break
    elif hare_position >= 70:
        print("\nHARE WINS || YUCH!!!")
        break
    elif tortoise_position >= 70:
        print("\nTORTOISE WINS! || VAY!!!")
        break 
    elif hare_energy <= 0 and tortoise_energy <= 0:
        print("\nBOTH ANIMALS ARE EXHAUSTED. IT'S A TIE.")
        break
    elif hare_energy <= 0:
        print("\nHARE IS EXHAUSTED. TORTOISE WINS! || VAY!!!")
        break
    elif tortoise_energy <= 0:
        print("\nTORTOISE IS EXHAUSTED. HARE WINS || YUCH!!!")
        break

