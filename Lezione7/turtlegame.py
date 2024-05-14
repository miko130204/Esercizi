import random


def print_race(hare_pos, tortoise_pos):
    positions: list[str] = ["_"] * 70
    for i in positions:
        if i == hare_pos and i == tortoise_pos:
            print("OUCH!!!", end=" ")
        elif i == hare_pos:
            print("H", end = " ")
        elif i == tortoise_pos:
            print("T", end = " ")
        else:
            print("_", end = " ")

def tortoise_move():
    move = random.randint(1, 10)
    if move <= 5:
        return 3
    elif move <= 7:
        return -6
    else:
        return 1

def hare_move():
    move = random.randint(1, 10)
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

print("BANG !!!!! AND THEY'RE OFF !!!!!")

hare_position = 1
tortoise_position = 1

while hare_position <= 70 and tortoise_position <= 70:
    hare_position += hare_move()
    if hare_position < 0:
        hare_position = 0
    tortoise_position += tortoise_move()
    if tortoise_position < 0:
        tortoise_position = 0

    print_race(hare_position, tortoise_position)

    if hare_position >= 70 and tortoise_position >= 70:
        print("\nIT'S A TIE.")
        break
    elif hare_position >= 70:
        print("\nHARE WINS || YUCH!!!")
        break
    elif tortoise_position >= 70:
        print("\nTORTOISE WINS! || VAY!!!")
        break
