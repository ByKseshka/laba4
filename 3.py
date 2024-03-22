def is_magic_date(date):
    try:
        day, month, year = map(int, date.split('.'))
        if day * month == year % 100:
            return True
        else:
            return False
    except (IndexError, ValueError):
        return False

user_date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
if is_magic_date(user_date):
    print("Это магическая дата!")
else:
    print("Это не магическая дата.")