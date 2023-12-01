from datetime import date, timedelta, datetime


def get_birthdays_per_week(users):
    if not users:
        return {}

    birthdays_per_week = {}
    today = date.today()

    for user in users:
        birthday = user['birthday'].replace(year=today.year)

        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        if today <= birthday <= today + timedelta(days=6):
            if birthday.weekday() >= 5:
                birthday = birthday + timedelta(days=(7 - birthday.weekday()))

            birthday_day_of_week = birthday.weekday()
            day_string = {
                0: 'Monday',
                1: 'Tuesday',
                2: 'Wednesday',
                3: 'Thursday',
                4: 'Friday',
                5: 'Saturday',
                6: 'Sunday'
            }[birthday_day_of_week]
            if day_string not in birthdays_per_week:
                birthdays_per_week[day_string] = []

            birthdays_per_week[day_string].append(user['name'])
    result = {day: names for day, names in birthdays_per_week.items() if names}
    return result


if __name__ == "__main__":
    users = [
        {"name": "Bill", "birthday": datetime(2023, 12, 3).date()},
        {"name": "Jan", "birthday": datetime(2023, 12, 2).date()},
        {"name": "Kim", "birthday": datetime(2023, 12, 1).date()},
        {"name": "Alice", "birthday": datetime(2023, 12, 30).date()},
        {"name": "Dima", "birthday": datetime(2023, 12, 2).date()},
        {"name": "Igor", "birthday": datetime(2023, 12, 3).date()},
        {"name": "Slava", "birthday": datetime(2023, 12, 3).date()}
    ]

    result = get_birthdays_per_week(users)
    if result:
        for day_name, names in result.items():
            print(f"{day_name}: {', '.join(names)}")
