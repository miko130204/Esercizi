#1

class Film:
    def __init__(self, title: str, duration: int):
        self.title: str = title
        self.duration: int = duration

class Room:
    def __init__(self, room_number: int, film: Film, all_seats: int):
        self.room_number: int = room_number
        self.film: Film = film
        self.all_seats: int = all_seats
        self.booked: int = 0

    def book_seat(self, num_seats: int) -> str:
        if num_seats > self.seats_left():
            return f"Error: only {self.seats_left()} seats left!"
        else:
            self.booked += num_seats
            return f"{num_seats} seats booked for '{self.film.title}' in room {self.room_number}"

    def seats_left(self) -> int:
        seats_left = self.all_seats - self.booked
        return seats_left

class Cinema:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []

    def add_room(self, room: Room) -> str:
        self.rooms.append(room)
        return f"Room {room.room_number} added, with film '{room.film.title}'"

    def book_film(self, title_film: str, num_seats: int) -> str:
        for room in self.rooms:
            if room.film.title == title_film:
                return room.book_seat(num_seats)
        return f"Error: film '{title_film}' not found"

cinema1 = Cinema("Cinelandia")
film1 = Film("Godzilla", 130)
film2 = Film("Avengers", 180)
room1 = Room(1, film1, 50)
room2 = Room(2, film2, 30)
print(cinema1.add_room(room1))
print(cinema1.add_room(room2))

print(cinema1.book_film("Godzilla", 30))
print(cinema1.book_film("Avengers", 35))
print(f"Seats left in room 1: {room1.seats_left()}")



#2

class Product:
    def __init__(self, name: str, quantity: int):
        self.name: str = name
        self.quantity: int = quantity

class Stock:
    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, product: Product):
        self.products.append(product)
        return f"{product} successfully added."

    def find_product(self, name: str) -> Product:
        for product in self.products:
            if product.name == name:
                return product

    def availability(self, name: str) -> str:
        product = self.find_product(name)
        if product:
            return f"{name} is available. {product.quantity} left."
        else:
            return f"{name} is not available."
        

stock = Stock()
product1: Product = Product("Iphone", 2000)
print(stock.add_product(product1))
print(stock.availability(product1.name))
        