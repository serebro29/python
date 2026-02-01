import sqlite3
from colorama import init, Fore, Style

init()

connection = sqlite3.connect("FruitBasket.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS Fruits")

cursor.execute("""
CREATE TABLE Fruits (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Назва_фрукта TEXT,
    Колір TEXT
);
""")

cursor.execute("INSERT INTO Fruits (Назва_фрукта, Колір) VALUES (?, ?)", ("Яблуко", "Зелене"))
cursor.execute("INSERT INTO Fruits (Назва_фрукта, Колір) VALUES (?, ?)", ("Банан", "Жовтий"))
cursor.execute("INSERT INTO Fruits (Назва_фрукта, Колір) VALUES (?, ?)", ("Апельсин", "Помаранчевий"))

print("Жовті фрукти:")
cursor.execute("SELECT * FROM Fruits WHERE Колір = 'Жовтий'")
for row in cursor.fetchall():
    print(row)

print("\nУсі фрукти:")
cursor.execute("SELECT * FROM Fruits")
for row in cursor.fetchall():
    if row[1] == "Яблуко":
        print(Fore.GREEN + str(row) + Style.RESET_ALL)
    else:
        print(row)

connection.commit()
connection.close()