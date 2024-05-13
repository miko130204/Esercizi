class Zoo:
    def _init_(self, name: str):
        self._name: str = name
        self.fences = []
        self.zoo_keepers = []

    def add_fence(self, fence):
        self.fences.append(fence)

    def add_zoo_keeper(self, zoo_keeper):
        self.zoo_keepers.append(zoo_keeper)

    def add_animal(self, animal, fence):
        if fence in self.fences and fence.area >= animal.width * animal.height and animal.preferred_habitat == fence.habitat:
            fence.add_animal(animal)
            print(f"{animal.name} added to {fence.name}.")
        else:
            print("Animal cannot be added to this fence.")

    def remove_animal(self, animal, fence):
        if fence in self.fences:
            fence.remove_animal(animal)
            print(f"{animal.name} removed from {fence.name}.")
        else:
            print("Animal or fence not found.")

    def feed(self):
        for fence in self.fences:
            fence.feed_animals()

    def clean(self):
        total_cleaning_time = 0.0
        for fence in self.fences:
            total_cleaning_time += fence.clean()
        return total_cleaning_time

    def describe_zoo(self):
        print(f"Zoo: {self.name}")
        print("Zoo Keepers:")
        for keeper in self.zoo_keepers:
            print(f"- {keeper.name} {keeper.surname} (ID: {keeper.id})")
        print("Fences:")
        for fence in self.fences:
            fence.describe_fence()


class Animal:
    def _init_(self, name, species, age, height, width, preferred_habitat):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age), 3)


class Fence:
    def _init_(self, name, area, temperature, habitat):
        self.name = name
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []

    def add_animal(self, animal):
        if self.area >= animal.width * animal.height:
            self.animals.append(animal)
            self.area -= animal.width * animal.height
        else:
            print("Not enough space in the fence to add this animal.")

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            self.area += animal.width * animal.height
        else:
            print("Animal not found in this fence.")

    def feed_animals(self):
        for animal in self.animals:
            if self.area >= (animal.width * 1.02) * (animal.height * 1.02):
                animal.health += 1
                animal.height *= 1.02
                animal.width *= 1.02
                print(f"{animal.name} fed.")
            else:
                print(f"Not enough space in {self.name} to feed {animal.name}.")

    def clean(self):
        occupied_area = sum(animal.width * animal.height for animal in self.animals)
        if self.area > 0:
            cleaning_time = occupied_area / self.area
        else:
            cleaning_time = occupied_area
        print(f"{self.name} cleaned. Cleaning time: {cleaning_time} hours.")
        return cleaning_time

    def describe_fence(self):
        print(f"- {self.name}:")
        print(f"  - Area: {self.area}")
        print(f"  - Temperature: {self.temperature}")
        print(f"  - Habitat: {self.habitat}")
        if self.animals:
            print("  - Animals:")
            for animal in self.animals:
                print(f"    - {animal.name} ({animal.species}), Age: {animal.age}, Health: {animal.health}")
        else:
            print("  - No animals in this fence.")


class ZooKeeper:
    def _init_(self, name, surname, id):
        self.name = name
        self.surname = surname
        self.id = id


# Esempio di utilizzo:
zoo = Zoo()
fence1 = Fence(name = "Savannah", area = 1000, temperature = "Warm", habitat = "Grassland")
fence2 = Fence("Jungle", 1500, "Tropical", "Rainforest")
zoo.add_fence(fence1)
zoo.add_fence(fence2)
keeper1 = ZooKeeper("John", "Doe", 1)
keeper2 = ZooKeeper("Jane", "Smith", 2)
zoo.add_zoo_keeper(keeper1)
zoo.add_zoo_keeper(keeper2)
lion = Animal("Simba", "Lion", 5, 2, 2, "Savannah")
elephant = Animal("Dumbo", "Elephant", 8, 4, 3, "Jungle")
zoo.add_animal(lion, fence1)
zoo.add_animal(elephant, fence2)
zoo.feed()
zoo.clean()
zoo.describe_zoo()