# from datetime import date, timedelta, datetime
#
# def get_birthdays_per_week(users):
#     # Если список пользователей пуст, возвращаем пустой словарь
#     if not users:
#         return {}
#
#     # Создаем пустой словарь для хранения дней рождений по дням недели
#     birthdays_per_week = {}
#
#     today = date.today()
#     current_day_index = today.weekday()
#
#     # Перебираем пользователей и определяем их дни рождения на текущей и следующей неделе
#     for user in users:
#         birthday = user['birthday']
#         # Если день рождения уже прошёл в текущем году, переносим его на следующий год
#         if birthday.replace(year=today.year) < today:
#             birthday = birthday.replace(year=today.year + 1)
#
#         # Проверяем, если день рождения попадает в текущую или следующую неделю
#         if today <= birthday <= today + timedelta(days=6 - current_day_index):
#             # Создаем ключ для дня рождения в словаре
#             day_name = birthday.strftime('%A')  # Получаем название дня недели
#             if day_name not in birthdays_per_week:
#                 birthdays_per_week[day_name] = []
#
#             # Добавляем пользователя в список дня рождения
#             birthdays_per_week[day_name].append(user['name'])
#
#     return birthdays_per_week
#
# if __name__ == "__main__":
#     # Тестовые данные с пользователями, у которых дни рождения в прошлом и будущем
#     users = [
#         {"name": "Bill", "birthday": datetime(2023, 12, 3).date()},
#         {"name": "Jan", "birthday": datetime(2023, 12, 2).date()},
#         {"name": "Kim", "birthday": datetime(2023, 12, 1).date()},
#         {"name": "Alice", "birthday": datetime(2023, 11, 30).date()},
#         {"name": "Dima", "birthday": datetime(2023, 12, 4).date()},
#         {"name": "Igor", "birthday": datetime(2023, 12, 5).date()},
#         {"name": "Slava", "birthday": datetime(2023, 12, 6).date()}
#
#     ]
#     result = get_birthdays_per_week(users)
#     if result:
#         for day_name, names in result.items():
#             print(f"{day_name}: {', '.join(names)}")
#     else:
#         print("На этой неделе нет дней рождений.")
#

from datetime import date, timedelta, datetime

def get_next_weekday(date_obj):
    """
    Функция, которая возвращает ближайший рабочий день (понедельник), если переданный день - выходной
    """
    while date_obj.weekday() > 4:  # Проверяем, является ли день выходным (субботой или воскресеньем)
        date_obj += timedelta(days=1)  # Переносим на следующий день
    return date_obj

def get_birthdays_per_week(users):
    if not users:
        return {}

    today = date.today()
    current_day_index = today.weekday()
    next_week_end = today + timedelta(days=6 - current_day_index)

    birthdays_per_week = {}

    for user in users:
        birthday = user['birthday'].replace(year=today.year)  # Заменяем год на текущий

        if birthday < today:  # Если день рождения уже был в этом году
            next_year_birthday = user['birthday'].replace(year=today.year + 1)  # Переносим на следующий год
            if today <= next_year_birthday <= next_week_end:  # Проверяем, будет ли на следующей неделе в следующем году
                next_year_birthday = get_next_weekday(next_year_birthday)  # Переносим на ближайший рабочий день
                day_name = next_year_birthday.strftime('%A')  # Получаем название дня недели
                if day_name not in birthdays_per_week:
                    birthdays_per_week[day_name] = []
                birthdays_per_week[day_name].append(user['name'])

        elif today <= birthday <= next_week_end:  # Проверяем, попадает ли в диапазон текущей и следующей недели в текущем году
            birthday = get_next_weekday(birthday)  # Переносим на ближайший рабочий день
            day_name = birthday.strftime('%A')  # Получаем название дня недели
            if day_name not in birthdays_per_week:
                birthdays_per_week[day_name] = []
            birthdays_per_week[day_name].append(user['name'])

    return birthdays_per_week



if __name__ == "__main__":
    users = [
        {"name": "Bill", "birthday": datetime(2023, 12, 3).date()},
        {"name": "Jan", "birthday": datetime(2023, 12, 2).date()},
        {"name": "Kim", "birthday": datetime(2023, 12, 1).date()},
        {"name": "Alice", "birthday": datetime(2023, 11, 30).date()},
        {"name": "Dima", "birthday": datetime(2023, 12, 4).date()},
        {"name": "Igor", "birthday": datetime(2023, 12, 5).date()},
        {"name": "Slava", "birthday": datetime(2023, 12, 6).date()}
    ]

    result = get_birthdays_per_week(users)
    if result:
        for day_name, names in result.items():
            print(f"{day_name}: {', '.join(names)}")


