result = []

def divider(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Передано нечислове значення")
    if a < b:
        raise ValueError("Число 'a' менше за 'b'")
    if b > 100:
        raise IndexError("Число 'b' більше за 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as e:
        print(f"Виняток типу {type(e).__name__}: {e} (для ключа {key})")

print("-" * 20)
print("Результат:", result)