# For this project I thought of inserting all the functions into the "Fence" class instead of inserting them in the "Zoo_Keeper" class, 
# because I found it more convenient. 
# The program works and performs all required functions.

class Zoo:
    def __init__(self, zoo_name: str):
        self.zoo_name: str = zoo_name
        self.fences = []
        self.zoo_keepers = []

    def add_fence(self, fence):
        self.fences.append(fence)

    def add_animal(self, animal, fence):
        if fence.area >= animal.area:
            if animal.preferred_habitat == fence.name:
                fence.add_animal(animal)
                print(f"{animal.name} added to {fence.name}.")
            else: 
                 print(f"There's enough space for {animal.name} but the habitat is wrong. ")
        else:
            print(f"{animal.name} cannot be added to {fence.name} because there's no space and the habitat is wrong. ")

    def remove_animal(self, animal, fence):
        if fence in self.fences:
            fence.remove_animal(animal)
            print(f"{animal.name} removed from {fence.name}.")
        else:
            print("Animal or fence not found.")

    def add_zoo_keeper(self, zoo_keeper):
        self.zoo_keepers.append(zoo_keeper)

    def feed(self, animal):
        for fence in self.fences:
            fence.feed_animals(animal)

    def clean(self) -> float:
        total_cleaning_time = 0.0
        for fence in self.fences:
            total_cleaning_time += fence.clean()
        return total_cleaning_time

    def describe_zoo(self):
        print("\n\nGuardians:")
        for keeper in self.zoo_keepers:
            print(f"\nZooKeeper(name={keeper.name}, surname={keeper.surname}, id={keeper.id})")
        print("\nFences:")
        for fence in self.fences:
            print(f"\n{fence.name}(area={fence.area}, temperature={fence.temperature}, habitat={fence.habitat})", end="\n\n")
            if fence.animals:
                print("with animals:\n")
                for animal in fence.animals:
                    print(f"Animal(name={animal.name}, species={animal.specie}, age={animal.age})",end="\n\n")
            print("#"*30)
        print(end="\n\n")


class Animal:
    def __init__(self, name: str, specie: str, age: int, height: int, width: int, preferred_habitat: str) -> None:
        self.name: str = name
        self.specie: str = specie
        self.age: int = age
        self.height: int = height
        self.width: int = width
        self.preferred_habitat: str = preferred_habitat
        self.health: float = round(100 * (1 / self.age), 3)
        self.area: int = self.height * self.width


class Fence:
    def __init__(self, name: str, area: int, temperature: int, habitat: str):
        self.name: str = name
        self.area: int = area
        self.temperature: int = temperature
        self.habitat: str = habitat
        self.animals: list[Animal] = []

    def add_animal(self, animal: Animal):
        if self.area > animal.area and animal.preferred_habitat == self.name:
            self.animals.append(animal)
            self.area -= animal.area 
        else: 
            print("Can't add animal. There isn't enough space!")
    
    def remove_animal(self, animal: Animal):
        if animal in self.animals:
            self.animals.remove(animal)
            self.area += animal.area
        else:
            print("This animal is not in this fence.")

    def feed_animals(self, animal: Animal):
        for animal in self.animals:
            if self.area >= (animal.area * 1.04):
                animal.health += (animal.health/100)*1
                animal.area += (animal.area/100)*4
                print(f"{animal.name} has been fed. ")
            else:
                print(f"Not enough space in {self.name} to feed {animal.name}.")

    def clean(self) -> float:
        occ_area = sum(animal.area for animal in self.animals)
        if self.area > 0:
            cleaning_time = occ_area / self.area
        else:
            cleaning_time = occ_area
        print(f"{self.name} has been cleaned in {cleaning_time} hours.")
        return cleaning_time
        
class Zoo_Keeper:
    def __init__(self, name: str, surname: str, id: int):
        self.name: str = name
        self.surname: str = surname
        self.id: int = id