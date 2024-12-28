def add_everything_up(a, b):
    # Проверяем, являются ли оба аргумента числом (int или float)
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    # Проверяем, являются ли оба аргумента строками
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    # Если типы отличаются, конкатенируем их в строковом представлении
    else:
        return str(a) + str(b)

# Примеры использования
print(add_everything_up(5, 10))
print(add_everything_up(5.5, 4.5))
print(add_everything_up("Hello, ", "world!"))
print(add_everything_up(5, " apples"))
print(add_everything_up("Count: ", 10))       
