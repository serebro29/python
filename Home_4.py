class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Тварина видає звук")

class Dog(Animal):
    def sound(self):
        print(f"{self.name} гавкає")

class Cat(Animal):
    def sound(self):
        print(f"{self.name} нявкає")

class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def age(self, current_year):
        return current_year - self.birth_year

class Driver(Person):
    def __init__(self, name, birth_year, license_number):
        super().__init__(name, birth_year)
        self.license_number = license_number

class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print(f"Рухається зі швидкістю {self.speed} км/год")

class Car(Vehicle):
    pass

class Bicycle(Vehicle):
    pass

class Device:
    def turn_on(self):
        print("Пристрій увімкнено")

    def turn_off(self):
        print("Пристрій вимкнено")

class Phone(Device):
    pass

class Laptop(Device):
    pass

class ProgrammingLanguage:
    def __init__(self, name):
        self.name = name

    def show_greeting(self):
        print(f"Привіт! Я мова програмування {self.name}")

class PythonLang(ProgrammingLanguage):
    pass

class JavaScriptLang(ProgrammingLanguage):
    pass

dog = Dog("Бобік")
cat = Cat("Мурчик")
dog.sound()
cat.sound()

driver = Driver("Іван", 2000, "AB123456")
print("Вік водія:", driver.age(2025))

car = Car(100)
car.move()

phone = Phone()
phone.turn_on()

python_lang = PythonLang("Python")
python_lang.show_greeting()