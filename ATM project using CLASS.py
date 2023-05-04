class Atm:
    # creating a constructor in python that is __init__ which get called when class is called
    def __init__(self):
        self.pin = ''
        self.balance = 0

        self.menu()

    # method are the functions which are created inside the class
    def menu(self):

        user_inp = input("""
        1. How we would like to procide
        Enter 1 to create pin
        Enter 2 to Deposit 
        Enter 3 to withdraw
        Enter 4 to check balance
        Enter 5 to exit

        """)

        if user_inp == '1':
            self.createpin()
            print("Create Pin")

        elif user_inp == '2':
            self.deposit()

        elif user_inp == '3':
            self.withdraw()

        elif user_inp == '4':
            self.check_balance()

        else:
            print("Exit")

    def createpin(self):
        self.pin = input("Enter Pin")
        print("pin set successful")
        self.menu()

    def deposit(self):
        enter_pin = input("Enter Pin")
        if enter_pin == self.pin:

            amount = int(input('Enter the Amount'))
            self.balance = self.balance + amount

        else:
            print('Wrong Pin')
        self.menu()

    def withdraw(self):

        enter_pin = input("Enter Pin")

        if enter_pin == self.pin:

            amount = int(input('Enter the Amount'))

            if amount <= self.balance:
                self.balance = self.balance - amount
                print("opp success")
            else:
                print("Not Enough Balance", self.balance)

        else:
            print('Wrong Pin')
        self.menu()

    def check_balance(self):

        enter_pin = input("Enter Pin")

        if enter_pin == self.pin:
            print(self.balance)

        else:
            print('Wrong Pin')
        self.menu()

obj = Atm()
obj