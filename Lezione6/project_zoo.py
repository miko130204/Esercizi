class Zoo:
    def __init__(self, zoo_name: str):
        self._zoo_name: str = zoo_name
        self._fences = []
        self._zoo_keepers = []

    def add_fence(self, fence):
        self._fences.append(fence)

    def add_animal(self, animal, fence):
        if fence._area >= animal._area and animal._preferred_habitat == fence._name:
            fence.add_animal(animal)
            print(f"{animal._name} added to {fence._name}.")
        else:
            print("Animal cannot be added to this fence.")

    def remove_animal(self, animal, fence):
        if fence in self._fences:
            fence.remove_animal(animal)
            print(f"{animal._name} removed from {fence._name}.")
        else:
            print("Animal or fence not found.")

    def add_zoo_keeper(self, zoo_keeper):
        self._zoo_keepers.append(zoo_keeper)

    def feed(self, animal):
        for fence in self._fences:
            fence.feed_animals(animal)

    def clean(self) -> float:
        total_cleaning_time = 0.0
        for fence in self._fences:
            total_cleaning_time += fence.clean()
        return total_cleaning_time

    def describe_zoo(self):
        print(f"Zoo: {self._zoo_name}")
        print("Zoo Keepers:")
        for keeper in self._zoo_keepers:
            print(f"- {keeper._name} {keeper._surname} (ID: {keeper._id})")
        print("Fences:")
        for fence in self._fences:
            fence.describe_fence()


class Animal:
    def __init__(self, name: str, specie: str, age: int, height: int, width: int, preferred_habitat: str):
        self._name: str = name
        self._specie: str = specie
        self._age: int = age
        self._height: int = height
        self._width: int = width
        self._preferred_habitat: str = preferred_habitat
        self._health: float = round(100 * (1 / self._age), 3)
        self._area: int = self._height * self._width
        self._fence = Fence


class Fence:
    def __init__(self, name: str, area: int, temperature: int, habitat: str):
        self._name: str = name
        self._area: int = area
        self._temperature: int = temperature
        self._habitat: str = habitat
        self._animals_list: list = []

    def add_animal(self, animal: Animal):
        if self._area > animal._area and animal._preferred_habitat == self._name:
            self._animals_list.append(animal)
            self._area -= animal._area 
        else: 
            print("Can't add animal. There isn't enough space!")
    
    def remove_animal(self, animal: Animal):
        if animal in self._animals_list:
            self._animals_list.remove(animal)
            self._area += animal._area
        else:
            print("This animal in not in this fence.")

    def feed_animals(self, animal : Animal):
        for animal[Animal] in self._animals_list:
            if self._area >= (animal._area * 1.04):
                animal._health += (animal._health/100)*1
                animal._area += (animal._area/100)*4
                print(f"{animal._name} has been fed ")
            else:
                print(f"Not enough space in {self._name} to feed {animal._name}.")

    def clean(self, animal = Animal) -> float:
        occ_area = sum(animal._area for animal[Animal] in self._animals_list)
        if self._area > 0:
            cleaning_time = occ_area / self._area
        else:
            cleaning_time = occ_area
        print(f"{self._name} cleaned. Cleaning time: {cleaning_time} hours.")
        return cleaning_time
    
    def describe_fence(self):
        print(f"- {self._name}:")
        print(f"  - Area: {self._area}")
        print(f"  - Temperature: {self._temperature}")
        print(f"  - Habitat: {self._habitat}")
        if self._animals:
            print("  - Animals:")
            for animal in self._animals:
                print(f"    - {animal._name} ({animal._species}), Age: {animal._age}, Health: {animal._health}")
        else:
            print("  - No animals in this fence.")
        

class Zoo_Keeper:
    def __init__(self, name: str, surname: str, id: int):
        self._name: str = name
        self._surname: str = surname
        self._id: int = id

   

zoo = Zoo(zoo_name = "2M Zoo")
fence1 = Fence(name = "Savannah", area = 1000, temperature = 40, habitat = "Grassland")
fence2 = Fence(name = "Jungle", area = 1500, temperature = 28, habitat = "Rainforest")
zoo.add_fence(fence1)
zoo.add_fence(fence2)
keeper1 = Zoo_Keeper(name = "John", surname = "Doe", id = 1)
keeper2 = Zoo_Keeper(name = "Jane", surname = "Smith", id = 2)
zoo.add_zoo_keeper(keeper1)
zoo.add_zoo_keeper(keeper2)
lion = Animal(name = "Simba", specie = "Lion", age = 5, height = 2, width = 2, preferred_habitat = "Savannah")
elephant = Animal(name = "Dumbo", specie = "Elephant", age = 8, height = 4, width = 3, preferred_habitat = "Jungle")
zoo.add_animal(lion, fence1)
zoo.add_animal(elephant, fence2)
zoo.feed(lion)
zoo.clean()
zoo.describe_zoo()