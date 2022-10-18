from collections import UserDict


class AddressBook(UserDict):

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

    def __init__(self, name, phone=None, email=None):
        self.name = Name(name)

        if phone:
            self.phones = [Phone(phone)]
        else:
            self.phones = []

        if email:
            self.emails = [Email(email)]
        else:
            self.emails = []

    def __repr__(self) -> str:
        return f'{self.name}: {", ".join([phone.value for phone in self.phones])} ' \
            f'{", ".join([email.value for email in self.emails])}'

    def change_name(self, name):
        self.name = Name(name)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for phone_number in self.phones:
            if phone == phone_number.value:
                self.phones.remove(phone_number)

    def change_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def add_email(self, email):
        self.emails.append(Email(email))

    def remove_email(self, email):
        self.phones.remove(Email(email))


class Field:
    def __init__(self, value):
        self.value = value

    def __repr__(self) -> str:
        return self.value


class Name(Field):
    pass


class Phone(Field):
    pass


class Email(Field):
    pass
