from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find_contact(self, name):
        if name in self.data:
            return self.data[name]
        else:
            print("Contact is not found")


class Record:
    phones = []
    emails = []

    def __init__(self, name, phone=None, email=None):
        self.name = Name(name)
        if phone:
            self.phones.append(Phone(phone).value)
        if email:
            self.emails.append(Email(email).value)

    def change_name(self, name):
        self.name = Name(name)

    def add_phone(self, phone):
        self.phones.append(Phone(phone).value)

    def remove_phone(self, phone):
        self.phones.remove(Phone(phone).value)

    def change_phone(self, old_phone, new_phone):
        self.phones.remove(Phone(old_phone).value)
        self.add_phone(Phone(new_phone).value)

    def add_email(self, phone):
        self.phones.append(Email(email).value)


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Email(Field):
    pass
