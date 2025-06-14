from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    result = []

    for person in users:
        # Convert birthday string to date
        birthday = datetime.strptime(person["birthday"], "%Y.%m.%d").date()

        # Use birthday in current year
        birthday_this_year = birthday.replace(year=today.year)

        # If already passed this year — take next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Check if birthday is within 7 days from today
        if 0 <= (birthday_this_year - today).days <= 7:
            greet_date = birthday_this_year

            # If birthday on weekend, move to Monday
            if greet_date.weekday() == 5:  # Saturday
                greet_date += timedelta(days=2)
            elif greet_date.weekday() == 6:  # Sunday
                greet_date += timedelta(days=1)

            # Add to result list
            result.append({
                "name": person["name"],
                "congratulation_date": greet_date.strftime("%Y.%m.%d")
            })

    return result

#  Example
if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.06.15"},
        {"name": "Jane Smith", "birthday": "1990.06.17"},
        {"name": "Olga", "birthday": "1995.06.14"},
        {"name": "Max", "birthday": "1992.12.25"}
    ]

    upcoming = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming)

    """
    TERMINAL:
    goit-pycore-hw-03 git:(main) ✗ /usr/local/bin/python3 /Users/olga/Developer/goit-pycore-hw-03/task_4.py
    Список привітань на цьому тижні: [{'name': 'John Doe', 'congratulation_date': '2025.06.16'}, {'name': 'Jane Smith', 'congratulation_date': '2025.06.17'}, {'name': 'Olga', 'congratulation_date': '2025.06.16'}]
    """

"""Завдання 4

У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати. Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.

У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я користувача та його день народження. Оскільки дні народження колег можуть припадати на вихідні, ваша функція також повинна враховувати це та переносити дату привітання на наступний робочий день, якщо необхідно.



Вимоги до завдання:

Параметр функції users - це список словників, де кожен словник містить ключі name (ім'я користувача, рядок) та birthday (день народження, рядок у форматі 'рік.місяць.дата').
Функція має визначати, чиї дні народження випадають вперед на 7 днів включаючи поточний день. Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.
Функція повертає список словників, де кожен словник містить інформацію про користувача (ключ name) та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата').


Рекомендації для виконання:

Припускаємо, що ви отримали список users, де кожен словник містить name (ім'я користувача) та birthday (дата народження у форматі рядка 'рік.місяць.дата'). Ви повинні перетворити дати народження з рядків у об'єкти datetime. Конвертуйте дату народження із рядка у datetime об'єкт - datetime.strptime(user["birthday"], "%Y.%m.%d").date(). Оскільки потрібна лише дата (без часу), використовуйте .date() для отримання тільки дати.
Визначте поточну дату системи за допомогою datetime.today().date().
Пройдіться по списку users та аналізуйте дати народження кожного користувача (for user in users:).
Перевірте, чи вже минув день народження в цьому році (if birthday_this_year < today). Якщо так, розгляньте дату на наступний рік.
Визначте різницю між днем народження та поточним днем для визначення днів народження на наступний тиждень.
Перевірте, чи день народження припадає на вихідний. Якщо так, перенесіть дату привітання на наступний понеділок.
Створіть структуру даних, яка зберігатиме ім'я користувача та відповідну дату привітання, якщо день народження відбувається протягом наступного тижня.
Виведіть зібрані дані у вигляді списку словників з іменами користувачів та датами привітань.


Критерії оцінювання:

Актуальність та коректність визначення днів народження на 7 днів вперед.
Правильність обробки випадків, коли дні народження припадають на вихідні.
Читабельність та структурованість коду.


Приклад:

Припустимо, у вас є список users:

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

Використання функції get_upcoming_birthdays:

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

Якщо сьогодні 2024.01.22 результатом може бути:

[
    {'name': 'John Doe', 'congratulation_date': '2024.01.23'}, 
    {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}
]

Цей список містить інформацію про те, кого і коли потрібно привітати з днем народження.
"""