from datetime import datetime, timedelta, date
from collections import UserDict


class AddressBook(UserDict):
    N = 2
    page = 0

    def iterator(self):
        for record in self.data.values():
            yield record

    def add_record(self, record):
        self.data[record.name.value] = record

    def find_contact(self, name):
        if name in self.data:
            return self.data[name]
        else:
            print("Contact is not found")

    def find_by_phone(self, phone):
        for record in self.data.values():
            if phone in [phone.value for phone in record.phones]:
                return record

    def find_by_email(self, email):
        for record in self.data.values():
            if email in [email.value for email in record.emails]:
                return record


class Record:

    def __init__(self, name, phone=None, email=None, birthday=None):
        self.name = Name(name)
        self.birthday = None

        if phone:
            self.phones = [Phone(phone)]
        else:
            self.phones = []

        if email:
            self.emails = [Email(email)]
        else:
            self.emails = []

        if birthday:
            self.birthday = Birthday(birthday)

    def __repr__(self) -> str:
        return f'{self.name}: {", ".join([phone.value for phone in self.phones])} ' \
            f'{", ".join([email.value for email in self.emails])} '\
            f'Birthday: {self.birthday}'

    def change_name(self, name):
        self.name = Name(name)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_email(self, email):
        self.emails.append(Email(email))

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def remove_phone(self, phone):
        for phone_number in self.phones:
            if phone == phone_number.value:
                self.phones.remove(phone_number)

    def change_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def remove_email(self, email):
        for email_address in self.emails:
            if email == email_address.value:
                self.emails.remove(email_address)

    def days_to_birthday(self):
        today = date.today()
        this_year_birthday = self.birthday.value.replace(year=today.year)

        if this_year_birthday == today:
            return f"{self.name} has Birthday TODAY!!!"

        elif this_year_birthday < today:
            next_birthday = self.birthday.value.replace(year=today.year+1)
            days_to_birthday = next_birthday - today
            return f'{self.name} will have birthday on {next_birthday.strftime("%d %B %Y")}. Days left: {days_to_birthday.days}'

        else:
            days_to_birthday = this_year_birthday - today
            return f'{self.name} will have birthday on {this_year_birthday.strftime("%d %B %Y")}. Days left: {days_to_birthday.days}'


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    def __repr__(self) -> str:
        return self.value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if len(value) > 1:
            self.__value = value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        new_value = (
            value.removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
        )

        if len(new_value) > 5 and new_value.isdigit():
            self.__value = new_value

        else:
            raise TypeError


class Email(Field):
    pass


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if len(value) == 9:
            birthday = datetime.strptime(value, "%d%b%Y")
            value = birthday.date()
            self.__value = value

        else:
            raise TypeError

    def __repr__(self) -> str:
        birthday = self.__value.strftime("%d %B %Y")
        return birthday
