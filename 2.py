def divide_100_by_user_input():
    try:
        number = float(input("Введите число: "))
        result = 100 / number
        print(f"Результат деления 100 на {number} равен {result}")
    except ValueError:
        print("Ошибка: Введено не число")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль")

divide_100_by_user_input()