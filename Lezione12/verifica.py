class Contatore:
    def __init__(self):
        self.conteggio: int = 0
        
    def setZero(self):
        self.conteggio = 0
            
    def add1(self):
        self.conteggio += 1 
        
    def sub1(self):
        if self.conteggio > 0:
            self.conteggio -= 1
        else:
            print("Non è possibile eseguire la sottrazione")
        
    def get(self):
        return self.conteggio
        
    def mostra(self):
        print(f"Conteggio attuale: {self.conteggio}")


# 2

class RecipeManager:
    def __init__(self):
        self.recipes: dict = {}

    def create_recipe(self, name, ingredients):
        self.recipes[name] = ingredients
        return {name: ingredients}

    def add_ingredient(self, recipe_name, ingredient):
        self.recipes[recipe_name].append(ingredient)
        return {recipe_name: self.recipes[recipe_name]}

    def remove_ingredient(self, recipe_name, ingredient):
        self.recipes[recipe_name].remove(ingredient)
        return {recipe_name: self.recipes[recipe_name]}

    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):
        index = self.recipes[recipe_name].index(old_ingredient)
        self.recipes[recipe_name][index] = new_ingredient
        return {recipe_name: self.recipes[recipe_name]}

    def list_recipes(self):
        return list(self.recipes.keys())

    def list_ingredients(self, recipe_name):
        return self.recipes[recipe_name]

    def search_recipe_by_ingredient(self, ingredient):
        found_recipes = {recipe: ingredients for recipe, ingredients in self.recipes.items() if ingredient in ingredients}
        return found_recipes
    

# 3

class Veicolo:
    def __init__(self, marca: str, modello: str, anno: int):
        self.marca: str = marca
        self.modello: str = modello
        self.anno: int = anno

    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")


class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, numero_porte: int):
        super().__init__(marca, modello, anno)
        self.numero_porte: int = numero_porte

    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}")


class Moto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, tipo: str):
        super().__init__(marca, modello, anno)
        self.tipo: str = tipo

    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")


# 4

        