CONTACTS = {}


def input_error(handler):

    def wrapper(*args, **kwargs):

        try:
            result = handler(*args, **kwargs)
            return result

        except KeyError:
            print("Sorry, I don't know this person. ")

        except ValueError:
            print("ValueError. Try again")

        except IndexError:
            print("Sorry, I don't know this comand.")

    return wrapper


def main():
    string = input("-> ")
    result = get_command(string)

    if result:
        print(result)

    if not result:
        print("Try again.")


def hello(*args):
    return "Hello! How can I help you?"


def quit_func(*args):
    print("Good bye. Hope to see you soon")
    quit()


def get_command(string):
    user_input = string.lower()
    words_list = user_input.split()

    for i in range(len(words_list)-1):
        words_list.append(words_list[i] + " " + words_list[i+1])

    for command in words_list:
        if command in COMMANDS:

            return COMMANDS[command](string)


@input_error
def add_contact(string):
    words = string.split()
    name = words[1]
    phone = words[2]
    CONTACTS[name] = phone
    result = f"{name} {phone} added to your Contacts."

    return result


@input_error
def find_contact(string):
    words = string.split()
    name = words[1]
    result = f'{name}: {CONTACTS[name]}'

    return result


@input_error
def change_contact(string):
    words = string.split()
    name = words[1]
    phone = words[2]
    CONTACTS[name] = phone
    result = f'Phone number was changed: {name} {CONTACTS[name]}'
    return result


@input_error
def show_contacts(*args):

    for name, phone in CONTACTS.items():
        print(name, phone)

    result = "There are all your contacts"
    return result


COMMANDS = {
    "hello": hello,
    "hi": hello,
    "exit": quit_func,
    "quit": quit_func,
    "end": quit_func,
    "bye": quit_func,
    "good bye": quit_func,
    "add": add_contact,
    "phone": find_contact,
    "show all": show_contacts,
    "change": change_contact,
    "find": find_contact
}

if __name__ == "__main__":
    while True:
        main()
