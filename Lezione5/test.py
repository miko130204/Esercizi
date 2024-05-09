class Food:
    def __init__(self, name: str, price: float, description: str):
        self._name: str = name
        self._price: float = price
        self._description: str = description

class Menu:
    def __init__(self, food_list: list = []):
        self._foodlist: list = food_list

    def addFood(self, food = Food):
        self._foodlist.append(food)
    
    def removeFood(self, index: int):
        del self._foodlist[index]

    def printPrices(self):
        for food in food_list:
            print(food._price)

    def get_average_price(self) -> float:
        sium: float = 0
        for food in food_list:
            sium += food._price
        avg = sium/len(food_list)
        return avg

food1: Food = Food("Peach", 5, "Fruit")
food2: Food = Food("Meat", 10, "BONO")
food3: Food = Food("Pasta", 15, "CARBONARA")
food4: Food = Food("Cianuro", 100, "NON TOSSICO")
food5: Food = Food("Plutonio", 40, "yes")

food_list: list = [food1, food2, food3]
menu_fesso: Menu = Menu([food_list])

menu_fesso.addFood(food4)
menu_fesso.addFood(food5)
menu_fesso.removeFood(0)

print(menu_fesso.get_average_price())