#Exercise 1: 

import math
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * self.radius ** 2
        return area
    
    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


#Exercise 2:

class MathOperations:
    def __init__(self, n1: int, n2: int):
        self.n1: int = n1
        self.n2: int = n2

    def add(self):
        result = self.n1 + self.n2
        return result
    
    def multiply(self):
        result = self.n1 * self.n2
        return result


#Exercise 3: 

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def __str__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}')"
    
    def from_string(cls, book_str: str):
        title, author, isbn = book_str.split(', ')
        return cls(title, author, isbn)

class Member:
    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_book(self, book: Book):
        self.borrowed_books.append(book)
    
    def return_book(self, book: Book):
        self.borrowed_books.remove(book)
    
    def __str__(self):
        borrowed_books_str = ', '.join([str(book) for book in self.borrowed_books])
        return f"Member(name='{self.name}', member_id='{self.member_id}', borrowed_books=[{borrowed_books_str}])"
    
    def from_string(cls, member_str: str):
        name, member_id = member_str.split(', ')
        return cls(name, member_id)

class Library:
    total_books = 0
    
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, book: Book):
        self.books.append(book)
        Library.total_books += 1
    
    def remove_book(self, book: Book):
        self.books.remove(book)
        Library.total_books -= 1
    
    def register_member(self, member: Member):
        self.members.append(member)
    
    def lend_book(self, book: Book, member: Member):
        if book in self.books and member in self.members:
            member.borrow_book(book)
            self.remove_book(book)
    
    def __str__(self):
        books_str = ', '.join([str(book) for book in self.books])
        members_str = ', '.join([str(member) for member in self.members])
        return f"Library(total_books={Library.total_books}, books=[{books_str}], members=[{members_str}])"
    
    def library_statistics(cls):
        return f"Total number of books: {cls.total_books}"


#Exercise 4

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_role(self):
        pass

    def __str__(self):
        return f"{self.get_role()}: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def get_role(self):
        return "Student"

    def enroll(self, course):
        self.courses.append(course)
        course.add_student(self)

    def __str__(self):
        return f"{super().__str__()}, Student ID: {self.student_id}"

class Professor(Person):
    def __init__(self, name, age, professor_id, department):
        super().__init__(name, age)
        self.professor_id = professor_id
        self.department = department
        self.courses = []

    def get_role(self):
        return "Professor"

    def assign_to_course(self, course):
        self.courses.append(course)
        course.set_professor(self)

    def __str__(self):
        return f"{super().__str__()}, Professor ID: {self.professor_id}, Department: {self.department}"

class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.students = []
        self.professor = None

    def add_student(self, student):
        self.students.append(student)

    def set_professor(self, professor):
        self.professor = professor

    def __str__(self):
        professor_name = self.professor.name if self.professor else "None"
        student_names = ', '.join(student.name for student in self.students)
        return (f"Course: {self.course_name} ({self.course_code}), "
                f"Professor: {professor_name}, Students: [{student_names}]")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.courses = []
        self.professors = []

    def add_course(self, course):
        self.courses.append(course)

    def add_professor(self, professor):
        self.professors.append(professor)

    def __str__(self):
        course_names = ', '.join(course.course_name for course in self.courses)
        professor_names = ', '.join(professor.name for professor in self.professors)
        return (f"Department: {self.department_name}, Courses: [{course_names}], "
                f"Professors: [{professor_names}]")

class University:
    def __init__(self, name):
        self.name = name
        self.departments = []
        self.students = []

    def add_department(self, department):
        self.departments.append(department)

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        department_names = ', '.join(department.department_name for department in self.departments)
        student_names = ', '.join(student.name for student in self.students)
        return (f"University: {self.name}, Departments: [{department_names}], Students: [{student_names}]")


math_department = Department("Math")
cs_department = Department("Computer Science")

calculus = Course("Calculus", "M001")
algebra = Course("Algebra", "M002")
algorithms = Course("Algorithms", "CS001")
data_structures = Course("Data Structures", "CS002")

prof_jones = Professor("Mike", 47, "P1001", "Math")
prof_smith = Professor("Logan", 40, "P1002", "Computer Science")

student_jack = Student("Jack", 21, "001")
student_sara = Student("Sara", 23, "002")

math_department.add_course(calculus)
math_department.add_course(algebra)
cs_department.add_course(algorithms)
cs_department.add_course(data_structures)

math_department.add_professor(prof_jones)
cs_department.add_professor(prof_smith)

prof_jones.assign_to_course(calculus)
prof_jones.assign_to_course(algebra)
prof_smith.assign_to_course(algorithms)
prof_smith.assign_to_course(data_structures)

student_jack.enroll(calculus)
student_jack.enroll(algorithms)
student_sara.enroll(algebra)
student_sara.enroll(data_structures)

uni = University("Tech University")
uni.add_department(math_department)
uni.add_department(cs_department)
uni.add_student(student_jack)
uni.add_student(student_sara)

print(uni)
for department in uni.departments:
    print(department)
    for course in department.courses:
        print(f"  {course}")
print("\nStudents and their details:")
for student in uni.students:
    print(student)
    for course in student.courses:
        print(f"  Enrolled in: {course.course_name}")