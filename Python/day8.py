#OOPs
# Class

class Car:
    def __init__(self):
        pass

    def start(self):
        print("Car started")

# car1 = Car()
# car1.start()

# car2 = Car()
# car2.start()

class Mobile:
    def __init__ (self, brand, color, ram):
        self.company = brand
        self.colour = color
        self.memory = ram
    
    def show_details(self):
        print(f"Brand: {self.company}, Color: {self.colour}, RAM: {self.memory}GB")

# mobile1 = Mobile("Samsung", "Black", 8)
# mobile1.show_details()
# print(mobile1.company)

# mobile2 = Mobile("Apple", "White", 4)
# mobile2.show_details()

# mobile3 = Mobile("OnePlus", "Blue", 12)
# mobile3.show_details()

class Animal:
    def make_sound(self, sound):
        print(f"The animal makes a {sound} sound")

cat = Animal()
# cat.make_sound("meow")

class Employee:
    def __init__ (self, eid, ename, designation):
        self.id = eid
        self.name = ename
        self.position = designation

    def login(self):
        print(f"Employee {self.name} logged in")

    def logout(self):
        print(f"Employee {self.name} logged out")

    def show_details(self, id, name, position):
        print(f"ID: {id}, Name: {name}, Position: {position}")

emp1 = Employee(101, "Alice", "Developer")
emp2 = Employee(102, "Bob", "Manager")
# emp1.login()
# emp1.logout()
emp1.show_details(emp1.id, emp2.name, emp1.position)
# emp1.show_details(1, 'Smith', 'Manager')
# print(emp1.name)