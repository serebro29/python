class BankAccount:
    def __init__(self, account_number: str, balance: float = 0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Сума поповнення має бути більшою за 0")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Сума зняття має бути більшою за 0")
        if amount > self.balance:
            raise ValueError("Недостатньо коштів на рахунку")
        self.balance -= amount
        return self.balance

class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self) -> str:
        return f"{self.year} {self.make} {self.model}"

class Employee:
    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self) -> str:
        return f"Заробітна плата {self.name}: {self.salary}"

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height

    def calculate_perimeter(self) -> float:
        return 2 * (self.width + self.height)

class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def display_info(self) -> str:
        return (
            f"Товар: {self.name}\n"
            f"Ціна: {self.price}\n"
            f"Кількість: {self.quantity}\n"
            f"Загальна вартість: {self.calculate_total_price()}")

if __name__ == "__main__":
    account = BankAccount("UA123456", 1000)
    account.deposit(500)
    print("Баланс після поповнення:", account.balance)

    try:
        account.withdraw(300)
        print("Баланс після зняття:", account.balance)
    except ValueError as e:
        print(e)

    car = Car("Toyota", "Corolla", 2020)
    print(car.get_info())

    employee = Employee("Іван", "Розробник", 25000)
    print(employee.get_salary_info())

    rectangle = Rectangle(5, 3)
    print("Площа:", rectangle.calculate_area())
    print("Периметр:", rectangle.calculate_perimeter())

    product = Product("Ноутбук", 30000, 2)
    print(product.display_info())
