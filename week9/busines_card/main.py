from available_functios import add, delete, list_info, get


def help_with_info():
    help_info = f'''
        #############
        ###Options###
        #############

        1. `add` - insert new business card
        2. `list` - list all business cards
        3. `delete` - delete a certain business card (`ID` is required)
        4. `get` - display full information for a certain business card (`ID` is required)
        5. `help` - list all available options
        6. `exit` to exit
    '''
    print(help_info)


def print_info(data):
    for i in range(len(data)):
        print("ID: ", data[i][0])
        print("Full Name: ", data[i][1])
        print("Email :", data[i][2])
        print("Age :", data[i][3])
        print("Phone :", data[i][4])
        if data[i][5] is not None:
            print("Additional info", data[i][5])


def main():
    print("Hello! This is your business card catalog. \
           WHat would you like? (enter ""help"" to list all available options)")
    help_command = 1
    while help_command is 1:
        user_input = input("Enter command:")
        if user_input == "help":
            help_with_info()
        elif user_input == "add":
            user_name = input("Enter user name: ")
            email = input("Enter email: ")
            age_h = input("Enter age: ")
            age = int(age_h)
            phone_h = input("Enter phone: ")
            phone = str(phone_h)
            add_info_h = input("Enter addional info (optional): ")
            add_info = str(add_info_h)
            add(user_name, email, age, phone, add_info)
        elif user_input == "list":
            data = list_info()
            print_info(data)
        elif user_input == "get":
            id_number = input("ID: ")
            data = get(id_number)
            print("ID: ", data[0][0])
            print("email: ", data[0][1])
            print("name: ", data[0][2])
        elif user_input == "delete":
            to_be_deleted = input("ID: ")
            to_be_deleted = int(to_be_deleted)
            delete(to_be_deleted)
        elif user_input == "exit":
            help_command = 0
        else:
            print("Wrong command")


if __name__ == '__main__':
    main()
