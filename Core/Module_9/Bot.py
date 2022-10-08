CONTACTS = {}


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
            print("Sorry, I don't know this comand.")

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
        "add": add_contact,
        "phone": find_contact,
        "show all": show_contacts,
        "change": change_contact,
        "find": find_contact
    }

    for command in all_phrases:

        if command in commands:
            return commands[command](words)

        else:
            raise ValueError


def hello(*args):
    return "Hello! How can I help you?"


def quit_func(*args):
    print("Good bye. Hope to see you soon")
    quit()


@input_error
def add_contact(words):
    name = words[1]
    phone = words[2]
    CONTACTS[name] = phone
    result = f"{name} {phone} added to your Contacts."

    return result


@input_error
def find_contact(words):
    name = words[1]
    result = f'{name}: {CONTACTS[name]}'

    return result


@input_error
def change_contact(words):
    name = words[1]
    phone = words[2]

    if name in CONTACTS:
        CONTACTS[name] = phone
        result = f'Phone number was changed: {name} {CONTACTS[name]}'
        return result

    else:
        raise KeyError


@input_error
def show_contacts(*args):

    for name, phone in CONTACTS.items():
        print(name, phone)

    result = "These are all your contacts"

    return result


if __name__ == "__main__":
    main()
