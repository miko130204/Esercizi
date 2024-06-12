class Forma:
    def __init__(self, nome):
        self.nome = nome

    def getArea(self):
        pass

    def render(self):
        pass


class Quadrato(Forma):
    def __init__(self, lato):
        super().__init__("Quadrato")
        self.lato = lato

    def getArea(self):
        return self.lato * self.lato

    def render(self):
        print(f"Ecco un {self.nome} di lato {self.lato}!\n")
        for i in range(self.lato):
            for j in range(self.lato):
                if i == 0 or i == self.lato - 1 or j == 0 or j == self.lato - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        print(f"L'area di questo {self.nome.lower()} vale: {self.getArea()}\n")


class Rettangolo(Forma):
    def __init__(self, base, altezza):
        super().__init__("Rettangolo")
        self.base = base
        self.altezza = altezza

    def getArea(self):
        return self.base * self.altezza

    def render(self):
        print(f"Ecco un {self.nome} avente base {self.base} ed altezza {self.altezza}!\n")
        for i in range(self.altezza):
            for j in range(self.base):
                if i == 0 or i == self.altezza - 1 or j == 0 or j == self.base - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        print(f"L'area di questo {self.nome.lower()} vale: {self.getArea()}\n")


class Triangolo(Forma):
    def __init__(self, lato):
        super().__init__("Triangolo")
        self.lato = lato

    def getArea(self):
        return (self.lato * self.lato) / 2

    def render(self):
        print(f"Ecco un {self.nome} avente base {self.lato} ed altezza {self.lato}!\n")
        for i in range(self.lato):
            for j in range(self.lato):
                if j == 0 or i == self.lato - 1 or i == j:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        print(f"L'area di questo {self.nome.lower()} vale: {self.getArea()}\n")


# test
quadrato = Quadrato(4)
quadrato.render()

rettangolo = Rettangolo(8, 4)
rettangolo.render()

triangolo = Triangolo(4)
triangolo.render()
