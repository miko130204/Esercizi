class Room:
    def __init__(self, id: int, floor: int, seats: int):
        self.id: int = id
        self.floor: int = floor
        self.seats: int = seats
        self.area: int = self.seats * 2
        
    def get_id(self):
        return self.id
        
    def get_floor(self):
        return self.floor
        
    def get_seats(self):
        return self.seats
        
    def get_area(self):
        return self.area
        
    
class Building:
    def __init__(self, name: str, address: str, floors: tuple):
        self.name: str = name
        self.address: str = address
        self.floors: tuple = floors
        self.rooms: list = []

    def get_floors(self):
        return self.floors

    def get_rooms(self):
        return self.rooms

    def add_room(self, room: Room):
        floor = room.get_floor()
        min_floor, max_floor = self.floors
        if room not in self.rooms and min_floor <= floor <= max_floor:
            self.rooms.append(room)

    def area(self):
        total_area: int = 0
        total_area += sum(room.get_area() for room in self.rooms)
        return total_area


class Person:
    def __init__(self, cf: str, name: str, surname: str, age: int):
        self.cf: str = cf
        self.name: str = name
        self.surname: str = surname
        self.age: int = age


class Student(Person):
    def __init__(self, cf: str, name: str, surname: str, age: int):
        super().__init__(cf, name, surname, age)
        self.group: Group = None

    def set_group(self, group):
        self.group = group


class Lecturer(Person):
    def __init__(self, cf: str, name: str, surname: str, age: int):
        super().__init__(cf, name, surname, age)

        
class Group:
    def __init__(self, name: str, limit: int):
        self.name: str = name
        self.limit: int = limit
        self.students: list = []
        self.lecturers: list = []

    def get_name(self):
        return self.name
    
    def get_limit(self):
        return self.limit
    
    def get_students(self):
        return self.students
    
    def get_limit_lecturers(self):
        return max(1, len(self.students) // 10)
    
    def add_student(self, student: Student):
        if len(self.students) < self.limit:
            self.students.append(student)
            student.set_group(self)
    
    def add_lecturer(self, lecturer: Lecturer):
        if len(self.lecturers) < self.get_limit_lecturers():
            self.lecturers.append(lecturer)


class Course:
    def __init__(self, name: str):
        self.name: str = name
        self.groups: list = []

    def register(self, student: Student):
        for group in self.groups:
            if len(group.get_students()) < group.get_limit() and student not in group.get_students():
                group.add_student(student)
                return
        print(f"No available group for student {student.name} {student.surname}")

    def get_groups(self):
        return self.groups

    def add_group(self, group: Group):
        self.groups.append(group)