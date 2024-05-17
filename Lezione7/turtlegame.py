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
    print()  # For new line after each race status

def tortoise_move(weather):
    move = random.randint(1, 10)
    if weather == "sunny":
        if move <= 5:
            return 3, -5
        elif move <= 7:
            return -6, -10
        else:
            return 1, -3
    elif weather == "rainy":
        if move <= 5:
            return 2, 0
        elif move <= 7:
            return -7, 0
        else:
            return 0, 0
    
def hare_move(weather):
    move = random.randint(1, 10)
    if weather == "sunny":
        if move <= 2:
            return 0, 0
        elif move <= 4:
            return 9, 0
        elif move <= 5:
            return -12, 0
        elif move <= 8:
            return 1, 0
        else:
            return -2, 0
    elif weather == "rainy":
        if move <= 2:
            return -2, 0
        elif move <= 4:
            return 7, 0
        elif move <= 5:
            return -14, 0
        elif move <= 8:
            return -1, 0
        else:
            return -4, 0

def adjust_for_obstacles_and_bonuses(position, effects):
    if position in effects:
        position += effects[position]
    return max(position, 1)  # Ensure position does not go below 1

print("BANG !!!!! AND THEY'RE OFF !!!!!")

# Initialize positions, weather, and energy
hare_position = 1
tortoise_position = 1
weather = "sunny"
clock = 0
hare_energy = 100
tortoise_energy = 100

# Define obstacles and bonuses
obstacles = {15: -3, 30: -5, 45: -7}
bonuses = {10: 5, 25: 3, 50: 10}

while hare_position < 70 and tortoise_position < 70:
    hare_move_result, hare_energy_change = hare_move(weather)
    tortoise_move_result, tortoise_energy_change = tortoise_move(weather)
    
    hare_position += hare_move_result
    hare_energy += hare_energy_change
    
    tortoise_position += tortoise_move_result
    tortoise_energy += tortoise_energy_change

    # Adjust positions for obstacles and bonuses
    hare_position = adjust_for_obstacles_and_bonuses(hare_position, obstacles)
    hare_position = adjust_for_obstacles_and_bonuses(hare_position, bonuses)
    
    tortoise_position = adjust_for_obstacles_and_bonuses(tortoise_position, obstacles)
    tortoise_position = adjust_for_obstacles_and_bonuses(tortoise_position, bonuses)

    # Ensure positions do not go below 1
    hare_position = max(hare_position, 1)
    tortoise_position = max(tortoise_position, 1)

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
