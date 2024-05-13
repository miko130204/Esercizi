class Zoo:
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


    def describe_zoo(self):
        print(f"Zoo: {self.name}")
        print("Zoo Keepers:")
        for keeper in self.zoo_keepers:
            print(f"- {keeper.name} {keeper.surname} (ID: {keeper.id})")
        print("Fences:")
        for fence in self.fences:
            fence.describe_fence()




class Fence:
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





