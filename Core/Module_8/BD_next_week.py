from collections import defaultdict
from datetime import datetime, timedelta


users_list = [
    {"name": "Vika",
     "birthday": datetime(year=1988, month=10, day=2)},
    {"name": "John",
     "birthday": datetime(year=1978, month=10, day=2)},
    {"name": "Adele",
     "birthday": datetime(year=1991, month=10, day=5)},
    {"name": "Denys",
     "birthday": datetime(year=1998, month=9, day=30)},
    {"name": "Alex",
     "birthday": datetime(year=1988, month=9, day=30)},
    {"name": "Diana",
     "birthday": datetime(year=1978, month=10, day=1)},
    {"name": "Dasha",
     "birthday": datetime(year=1991, month=10, day=3)},
    {"name": "Alla",
     "birthday": datetime(year=1998, month=10, day=5)},
    {"name": "Slava",
     "birthday": datetime(year=1978, month=10, day=8)},
    {"name": "Max",
     "birthday": datetime(year=1991, month=10, day=7)},
    {"name": "Olya",
     "birthday": datetime(year=1998, month=10, day=4)},

]


def get_birthdays_per_week(users):
    birthdays = defaultdict(list)

    today = datetime.today()
    next_week = [today + timedelta(days=i) for i in range(1, 8)]

    for date in next_week:

        for person in users_list:

            if person["birthday"].month == date.month and person["birthday"].day == date.day:

                if date.isoweekday() == 6 or date.isoweekday() == 7:
                    birthdays["Monday"].append(person["name"])

                else:
                    birthdays[date.strftime("%A")].append(person["name"])

    for weekday in birthdays:
        if birthdays[weekday]:
            printable = "{}: {} ".format(
                weekday, ', '.join(birthdays[weekday]))
            print(printable)


get_birthdays_per_week(users_list)
