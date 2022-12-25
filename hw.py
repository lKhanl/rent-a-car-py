import datetime
import os

username = ""


def main():
    global username
    time = datetime.datetime.now()

    check_files()

    print("""
                   _______
                  //  ||\ \\
            _____//___||_\ \___
            )  _          _    \\
            |_/ \________/ \___|
           ___\_/________\_/______
       """)

    print("\n\tWELCOME TO CAR RENTAL SHOP!\n")
    print(f"\tCurrent date and time: {time}")

    while True:
        print("""
        ******** Car Rental Shop ********
        1. Admin
        2. Unregistered Customer
        3. Registered Customer
        4. Exit the program
        """)

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number!")
            continue

        if choice == 1:
            admin()

        elif choice == 2:
            unregistered_function()

        elif choice == 3:
            registered_function()

        elif choice == 4:
            break

        else:
            print("Please enter a choice between 1-4 only!")


def login(user, password, elevated):

    with open("User_Data.txt" if not elevated else "Admin_Data.txt", "r+") as text:
        print("%s Login ********" %
              ("******** Admin" if elevated else "******** User"))
        for record in text:
            recordList = record.rstrip().split(":")
            if user.lower() in recordList[0].lower() and password in recordList[1]:
                print("Welcome, %s" % user)
                return True
        print("Error! Wrong username or password")
        return False


def admin():
    nValue = input("Enter username: ")
    pValue = input("Enter password: ")
    if login(nValue, pValue, True):
        admin_function()


def admin_function():
    while True:
        print("""
            ******** Access System ********
            1. Add Car with details, to be rented out
            2. Modify Car Details
            3. Display All records of
                a. Cars available for Rent
                b. Customer Payment for a specific time duration
            4. Exit to main menu
            """)

        try:
            choice = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a number!")
            continue

        if choice == 1:
            add_cars()

        elif choice == 2:
            modify_cars()

        elif choice == 3:
            option = input("option a or b? ")
            if option == 'a':
                display_cars()
            else:
                display_booking()

        # elif choice == 4:
        #     option = input("option a or b?")
        #     if option == 'a':
        #         # search_car_booking of function goes here
        #         print("Specific Search of Car Booking")
        #     else:
        #         # search_customer_pay function goes here
        #         print("Specific Search of Customer Payment")

        # elif choice == 5:
        #     print("return_cars()")

        elif choice == 4:
            break

        else:
            print("Please enter a number between 1-6 only!")


def get_new_users():

    with open("User_Data.txt", "r+") as text:
        while True:
            name = input("Enter name to register: ")
            for record in text:
                recordList = record.rstrip().split(":")
                if name in recordList[0]:
                    print("Username already exists")
                    return
            password = input("Enter password: ")
            record = name + ":" + password
            text.write(record + "\n")
            break


def existing_users():
    global username
    nValue = input("Username: ")
    pValue = input("Password: ")
    username = nValue
    return login(nValue, pValue, False)


def display_cars():
    with open("DisplayCars_Data.txt", "r+") as text:
        lines = text.readlines()
        index = 1
        if len(lines) == 0:
            print("No cars available")
            return
        for line in lines:
            splitted = line.rstrip().split(":")
            car_type = splitted[0]
            brand = splitted[1]
            color = splitted[2]
            year = splitted[3]
            price = splitted[4]
            print("%d. Type: %s Brand: %s Color: %s Year: %s Price: %s" %
                  (index, car_type, brand, color, year, price))
            index += 1


def add_cars():
    with open("DisplayCars_Data.txt", "a") as text:
        car_type = input("Type: ")
        brand = input("Brand: ")
        color = input("Color: ")
        year = input("Year: ")
        price = input("Price: ")
        text.write("%s:%s:%s:%s:%s\n" % (car_type, brand, color, year, price))


def modify_cars():
    display_cars()
    with open("DisplayCars_Data.txt", "r+") as text:
        index_to_modify = int(input("Select record to modify: "))
        lines = text.readlines()
        if index_to_modify - 1 >= len(lines) or index_to_modify < 0:
            print("Invalid index")
            return
        entries = []
        for line in lines:
            entries.append(line.rstrip().split(":"))
    with open("DisplayCars_Data.txt", "w") as text:
        car_type = input("Type: ")
        brand = input("Brand: ")
        color = input("Color: ")
        year = input("Year: ")
        price = input("Price: ")
        entries[index_to_modify - 1] = (car_type, brand, color, year, price)
        for entry in entries:
            text.write("%s:%s:%s:%s:%s\n" %
                       (entry[0], entry[1], entry[2], entry[3], entry[4]))


def display_booking():
    print("******** Display Booking ********")
    with open("Booking_Data.txt", "r+") as text:
        lines = text.readlines()
        index = 1
        if len(lines) == 0:
            print("No bookings available")
            return
        for line in lines:
            splitted = line.rstrip().split(":")
            username = splitted[0]
            type = splitted[1]
            brand = splitted[2]
            color = splitted[3]
            year = splitted[4]
            price = splitted[5]
            total = splitted[6]
            date = splitted[7]
            print("%d. Username: %s Type: %s Brand: %s Color: %s Year: %s Price: %s Total Price: %s Date: %s" %
                  (index, username, type, brand, color, year, price, total, date))
            index += 1


def unregistered_function():
    while True:
        print("""
        ******** All Customers ********
        1. View all cars available for rent
        2. Register as a new user
        3. Exit to main menu
        """)
        try:
            choice = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a number!")
            continue

        if choice == 1:
            display_cars()

        elif choice == 2:
            get_new_users()
            break

        elif choice == 3:
            break

        else:
            print("Please enter a choice between 1-2 only!")


def registered_function():
    if existing_users() is True:
        while True:
            print("""
            ******** Registered Customer ********
            1. Personal Rental History
            2. Available Cars
            3. Booking Cars
            4. Car Delivery
            5. Exit to main menu
            """)
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a number!")
                continue

            if choice == 1:
                show_personal_history()

            elif choice == 2:
                display_cars()

            elif choice == 3:
                book_cars()

            elif choice == 4:
                delivery_car()

            elif choice == 5:
                break

            else:
                print("Please enter a choice between 1-5 only!")
    else:
        print("1. Please re-enter login details")
        print("2. Exit to main menu")
        choice = int(input("Enter choice: "))
        if choice == 1:
            existing_users()
        else:
            return


def book_cars():
    print("******** Booking Cars ********")

    display_cars()

    with open("DisplayCars_Data.txt", "r+") as text:
        lines = text.readlines()

        index = int(input("Select Car for booking: "))
        index = index - 1

        record = lines[index].split(':')

        print("1. Type: ", record[0])
        print("2. Brand: ", record[1])
        print("3. Color: ", record[2])
        print("4. Year: ", record[3])
        print("5. Price: ", record[4])

        day = int(input("Enter day(s) for your booking: "))

        total_price = int(record[4]) * day
        print("Total Price: ", total_price)

        # get today's date
        today = datetime.date.today()

        # add day of today
        booking_date = today + datetime.timedelta(days=day)

        # convert to string
        booking_date = booking_date.strftime("%d/%m/%Y")
        print("Booking Date: ", booking_date)

        # write to file
        with open("Booking_Data.txt", "a") as text:

            record_str = username + ":"
            for rec in record:
                if rec.endswith("\n"):
                    record_str += rec[:-1] + ":"
                else:
                    record_str += rec + ":"

            text.write(record_str + str(total_price) +
                       ":" + booking_date + "\n")

        # remove from display cars
        with open("DisplayCars_Data.txt", "w") as text:
            for line in lines:
                if line != lines[index]:
                    text.write(line)


def delivery_car():
    print("******** Car Delivery ********")

    with open("Booking_Data.txt", "r+") as text:
        lines = text.readlines()
        for i, line in enumerate(lines):
            record = line.rstrip().split(":")
            if record[0] == username:
                print(str(i + 1) + ". Type: %s Brand: %s Color: %s Year: %s Booking Date: %s" %
                      (record[1], record[2], record[3], record[4], record[7]))

        index = int(
            input("Press enter the number of the car you want to deliver: ")) - 1

        # if index error
        if index + 1 > len(lines):
            print("Please enter a valid number!")
            return

        record = lines[index].split(':')

        date = record[7].replace("\n", "")
        # convert to date
        date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
        # get today's date
        today = datetime.date.today()
        # get difference
        difference = today - date
        # convert to int
        difference = int(difference.days)
        # get price
        price = int(record[5])
        # calculate total price
        total_price = (price * difference) + int(record[6])
        if difference > 0:
            print("Total Price: ", total_price)
        else:
            print("Total Price: ", price)

    # remove from booking cars
    with open("Booking_Data.txt", "w") as text:
        for line in lines:
            if line != lines[index]:
                text.write(line)

    # add to display cars
    with open("DisplayCars_Data.txt", "a") as text:
        for line in lines:
            if line == lines[index]:
                text.write(line.split(":")[1] + ":" + line.split(":")[2] + ":" +
                           line.split(":")[3] + ":" + line.split(":")[4] + ":" + line.split(":")[5] + "\n")


def show_personal_history():

    with open("Booking_Data.txt", "r+") as text:
        print("\n******** Personal Rental History ********")
        lines = text.readlines()
        if len(lines) == 0:
            print("No booking history yet!")
        else:
            for i, line in enumerate(lines):
                record = line.rstrip().split(":")
                if record[0] == username:
                    print(str(i+1) + ". Type: %s Brand: %s Color: %s Year: %s Booking Date: %s Price: %s" %
                          (record[1], record[2], record[3], record[4], record[7], record[5]))


def check_files():
    if os.path.isfile("Admin_Data.txt") is False:
        with open("Admin_Data.txt", "a") as text:
            pass

            with open("Admin_Data.txt", "r+") as text:
                if len(text.readlines()) == 0:
                    text.write("admin:admin\n")
    if os.path.isfile("DisplayCars_Data.txt") is False:
        with open("DisplayCars_Data.txt", "a") as text:
            pass

            with open("DisplayCars_Data.txt", "r+") as text:
                if len(text.readlines()) == 0:
                    text.write("sedan:Renault:clio:white:2020:100\n")
                    text.write("sedan:Honda:Civic:gray:2022:200\n")
                    text.write("sedan:Mazda:3:white:2018:150\n")
                    text.write("sedan:Tesla:model3:black:2022:500\n")
                    text.write("sedan:Toyota:Corolla:gray:2017:100\n")
                    text.write("sport:Lamborghini:Aventador:white:2022:1000\n")

    if os.path.isfile("Booking_Data.txt") is False:
        with open("Booking_Data.txt", "a") as text:
            pass
    if os.path.isfile("User_Data.txt") is False:
        with open("User_Data.txt", "a") as text:
            pass
    if os.path.isfile("User_Data.txt") is False:
        with open("User_Data.txt", "a") as text:
            pass


if __name__ == "__main__":
    main()
