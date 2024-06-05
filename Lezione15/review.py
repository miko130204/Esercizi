class Media:
    def __init__(self, title):
        self.title = title
        self.reviews = []

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def aggiungiValutazione(self, voto):
        if voto >= 1 and voto <= 5:
            self.reviews.append(voto)
        else:
            print("Valutazione non valida. La valutazione deve essere compresa tra 1 e 5.")

    def getMedia(self):
        if len(self.reviews) == 0:
            return 0
        return sum(self.reviews) / len(self.reviews)

    def getRate(self):
        media = self.getMedia()
        if media >= 4.5:
            return "Eccezionale"
        elif media >= 3.5:
            return "Ottimo"
        elif media >= 2.5:
            return "Buono"
        elif media >= 1.5:
            return "Sufficiente"
        else:
            return "Insufficiente"

    def ratePercentage(self, voto):
        if len(self.reviews) == 0:
            return 0
        return (self.reviews.count(voto) / len(self.reviews)) * 100

    def recensione(self):
        print("Titolo del Media:", self.title)
        print("Voto Medio:", "{:.2f}".format(self.getMedia()))
        print("Giudizio:", self.getRate())
        for voto in range(1, 6):
            print(f"{voto} stelle: {self.ratePercentage(voto):.2f}%")


class Film(Media):
    pass

film1 = Film("Transformers")
film2 = Film("Inception")

valutazioni_film1 = [5, 4, 4, 3, 5, 4, 5, 5, 3, 4]
valutazioni_film2 = [5, 5, 4, 5, 3, 4, 4, 5, 5, 5]

for voto in valutazioni_film1:
    film1.aggiungiValutazione(voto)

for voto in valutazioni_film2:
    film2.aggiungiValutazione(voto)

film1.recensione()
print("\n")
film2.recensione()
