from abc import ABC, abstractmethod

# Object-Oriented Programming (OOP) in Python

# ============================================
# 1. CLASSES AND OBJECTS
# ============================================

class Car:
    """A class to represent a car"""
    
    # Class variable (shared by all instances)
    total_cars = 0
    
    # Constructor - called when object is created
    def __init__(self, brand, model, year):
        # Instance variables (unique to each object)
        self.brand = brand
        self.model = model
        self.year = year
        Car.total_cars += 1
    
    # Instance method
    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"
    
    # Class method
    @classmethod
    def get_total_cars(cls):
        return cls.total_cars
    
    # Static method
    @staticmethod
    def is_vintage(year):
        return year < 2000


# Creating objects (instances)
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 1998)

print(car1.display_info())  # 2020 Toyota Camry
print(Car.get_total_cars())  # 2
print(Car.is_vintage(1998))  # True


# ============================================
# 2. INHERITANCE
# ============================================

class Vehicle:
    """Parent class"""
    def __init__(self, name):
        self.name = name
    
    def move(self):
        return f"{self.name} is moving"


class Bike(Vehicle):
    """Child class inherits from Vehicle"""
    def move(self):
        return f"{self.name} is pedaling"


bike = Bike("Mountain Bike")
print(bike.move())  # Mountain Bike is pedaling


# ============================================
# 3. ENCAPSULATION (Private/Protected Attributes)
# ============================================

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute (name mangling)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}"
        return "Invalid amount"
    
    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
print(account.deposit(500))  # Deposited $500
print(account.get_balance())  # 1500


# ============================================
# 4. POLYMORPHISM
# ============================================

class Dog:
    def sound(self):
        return "Woof!"


class Cat:
    def sound(self):
        return "Meow!"


def animal_sound(animal):
    print(animal.sound())


animal_sound(Dog())  # Woof!
animal_sound(Cat())  # Meow!


# ============================================
# 5. ABSTRACTION (Abstract Base Classes)
# ============================================



class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2


circle = Circle(5)
print(f"Circle area: {circle.area()}")  # Circle area: 78.5