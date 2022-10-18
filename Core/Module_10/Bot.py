import email
from Core import AddressBook, Record


CONTACTS = AddressBook()


def main():
    while True:
        user_input = input("-> ")

        words = user_input.split()
        all_phrases = get_phrases(words)
        result = run_handler(all_phrases, words)

        if result:
            print(result)

        if not result:
            print("Try again.")


def input_error(handler):

    def wrapper(*args, **kwargs):

        try:
            return handler(*args, **kwargs)

        except KeyError:
            print("Sorry, I don't know this person. ")

        except ValueError:
            print("Sorry, I don't know this command.")

        except IndexError:
            print("I need more information.")

    return wrapper


def get_phrases(words):
    all_phrases = [word.lower() for word in words]

    for i in range(len(words)-1):
        all_phrases.append((words[i] + " " + words[i+1]).lower())

    return all_phrases


@input_error
def run_handler(all_phrases, words):
    commands = {
        "hello": hello,
        "hi": hello,
        "exit": quit_func,
        "quit": quit_func,
        "end": quit_func,
        "bye": quit_func,
        "good bye": quit_func,
        "add contact": add_contact,
        "add phone": add_phone,
        "add email": add_email,

        "find name": find_contact,
        "find phone": find_by_phone,
        "find email": find_by_email,

        "remove phone": remove_phone,

        "show all": show_contacts,
        "change phone": change_phone

    }

    for command in all_phrases:
        if command in commands:
            words = tuple(words[len(command.split()):])

            return commands[command](words)

    raise ValueError


def hello(*args):
    return "Hello! How can I help you?"


def quit_func(*args):
    print("Good bye. Hope to see you soon")
    quit()


@input_error
def add_contact(words):
    record = Record(*words)
    CONTACTS.add_record(record)

    result = f" Contact {record.name.value} phone: {record.phones} email: {record.emails} added to your Address Book."

    return result


@input_error
def add_phone(words):
    name, phone = words
    CONTACTS[name].add_phone(phone)
    result = f"Phone: {phone} was added to Contact {name}."

    return result


@input_error
def add_email(words):
    name, email = words
    CONTACTS[name].add_email(email)

    result = f"Email: {email} was added to Contact {name}."

    return result


@input_error
def find_contact(words):
    name = ''.join(words)
    return CONTACTS.find_contact(name)


@input_error
def find_by_phone(words):
    phone = ''.join(words)
    return CONTACTS.find_by_phone(phone)


@input_error
def find_by_email(words):
    email = ''.join(words)
    return CONTACTS.find_by_email(email)


@input_error
def change_phone(words):
    name, old_phone, new_phone = words
    CONTACTS[name].change_phone(old_phone, new_phone)
    result = f'{name} Phone number {old_phone} was changed to {new_phone}'
    return result


@input_error
def remove_phone(words):
    name, phone = words
    CONTACTS[name].remove_phone(phone)
    result = f'Phone number {phone} was removed from contact {name}'
    return result


@input_error
def show_contacts(*args):

    for _, contact in CONTACTS.items():
        print(contact)

    result = "These are all your contacts"

    return result


if __name__ == "__main__":
    main()
