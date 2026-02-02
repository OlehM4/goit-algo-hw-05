def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "list index out of range"
        except KeyError:
            return "Contact not defined!"
    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contact):
    name, phone = args
    contact[name] = int(phone)
    return "Contact added."


@input_error   
def change_contact(args, contact):
    name, phone = args
    
    if name in contact:
        contact[name] = int(phone)
        return "Contact updated."
    
    return "Contact not defined!"
        
    
@input_error    
def show_phone(args, contact):
    name = args[0]
    
    if name in contact:
        return contact[name]
    
    return "Contact not defined!"


@input_error 
def show_all(contact):
    result = ""
    if contact == {}:
        return "No contacts."
    
    for name, phone in contact.items():
        result += f"{name}: {phone}\n"
    return result



def main():
    contact = {}
    print("Welcome to the assistant bot")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ["exit", "close"]:
            print("Good bye!")
            break
        if command == "hello":
            print("How can i help you?")    
        elif command == "add":
            print(add_contact(args, contact))
        elif command == "change":
            print(change_contact(args, contact))    
        elif command == "phone":
            print(show_phone(args, contact))
        elif command == "all":
            print(show_all(contact))
        else:
            print("Invalid code")
            
if __name__ == "__main__":
    main()