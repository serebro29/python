import requests
import sqlite3
from datetime import datetime

connection = sqlite3.connect("weather.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datetime TEXT,
    temperature REAL
)
""")
connection.commit()

url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=49.4444"
    "&longitude=32.0598"
    "&current_weather=true"
)

response = requests.get(url)
data = response.json()

temperature = data["current_weather"]["temperature"]
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

cursor.execute(
    "INSERT INTO weather (datetime, temperature) VALUES (?, ?)",
    (now, temperature)
)

connection.commit()
connection.close()

print("✅ Дані збережено")
print("📅 Дата і час:", now)
print("🌡 Температура:", temperature, "°C")