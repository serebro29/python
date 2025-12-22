class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_done(self):
        self.completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        for task in self.tasks:
            status = "Виконано" if task.completed else "Не виконано"
            print(task.title, "-", status)

print("=== TASK MANAGER ===")
tm = TaskManager()
t1 = Task("Математика", "Зробити ДЗ", "20.12")
tm.add_task(t1)
tm.show_tasks()
t1.mark_done()
tm.show_tasks()

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_price(self):
        return sum(p.price for p in self.products)

print("\n=== SHOP ===")
p1 = Product("Хліб", 25)
p2 = Product("Молоко", 40)
cart = Cart()
cart.add_product(p1)
cart.add_product(p2)
print("Сума:", cart.total_price())

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

print("\n=== BANK ===")
acc = BankAccount("Іван", 100)
acc.deposit(50)
print("Баланс:", acc.balance)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Department:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def total_salary(self):
        return sum(e.salary for e in self.employees)

print("\n=== COMPANY ===")
dep = Department()
dep.add_employee(Employee("Анна", 10000))
dep.add_employee(Employee("Олег", 12000))
print("Зарплата відділу:", dep.total_salary())