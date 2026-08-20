

def main():
    print("Welcome to the Feynman Mobile Banking App\n\nFor first time users please create an account first.")
    print("\n1.Create Account\n2.Login")

    while True:
        user_choice = input("\nPlease Enter 1 to continue: ")
        if user_choice.isdigit() and int(user_choice) == 1:
            user_choice = int(user_choice)
            break
        print("Please Enter 1 to create an account.")

    Account_details = create_account()

    while True:
        login = input("\nPlease Enter 2 to login into the Mobile Banking App Now: ")
        if login.isdigit() and int(login) == 2:
            break
        print("\nPlease Enter 2 to login.")

    login_account(Account_details)

    while True:
        print(f"\nWelcome {Account_details['name']}, Please choose from our services:\n1.Deposit\n2.Transfer Money\n3.Check Balance\n4.Exit")

        while True:
            choose_options = input("\nPlease select an option from our services: ")
            if choose_options.isdigit() and int(choose_options) in [1, 2, 3, 4]:
                choose_options = int(choose_options)
                break
            print("Please select from an option of services. Enter 1, 2, 3 or 4.")

        if choose_options == 1:
            Deposit_func(Account_details)
        elif choose_options == 2:
            Transfer_Money(Account_details)
        elif choose_options == 3:
            check_balance(Account_details)
        elif choose_options == 4:
            print("\nThank you for banking with us, do business everywhere you go with the Feynman mobile banking app!")
            break

        print("\nDo you want to perform any other transaction again? \n1.Yes\n2.No")
        while True:
            another_transaction = input("\nPlease Enter 1 or 2: ")
            if another_transaction.isdigit() and int(another_transaction) in [1, 2]:
                another_transaction = int(another_transaction)
                break
            print("\nPlease enter 1 or 2.")

        if another_transaction == 2:
            print("\nThank you for banking with us, do business everywhere you go with the Feynman mobile banking app!")
            break


def create_account():
    account_details = {}
    account_details['name'] = input("\nEnter your first name please: ")
    while not account_details['name'].isalpha():
        print("\nName must be only string characters and not numbers")
        account_details['name'] = input("\nEnter your first name please: ")

    account_details['Account_Number'] = input("\nPlease Enter your 8 digit bank account Number: ")
    while len(account_details['Account_Number']) != 8 or not account_details['Account_Number'].isdigit():
        print("Account number must consist of 8 digits")
        account_details['Account_Number'] = input("\nPlease Enter your 8 digit bank account Number: ")

    account_details['Account Balance'] = input("\nPlease make an initial deposit of $100 or above to open the mobile bank account: ")
    while not account_details['Account Balance'].replace(".", "", 1).isdigit() or float(account_details['Account Balance']) < 100:
        print("Deposit must be $100 or above")
        account_details['Account Balance'] = input("\nPlease make an initial deposit of $100 or above: ")
    account_details['Account Balance'] = float(account_details['Account Balance'])

    account_details['password_pin'] = input("\nPlease enter your 4 digit bank account pin: ")
    while len(account_details['password_pin']) != 4 or not account_details['password_pin'].isdigit():
        print("The bank pin must be a 4 digit number.")
        account_details['password_pin'] = input("\nPlease enter your bank account pin: ")

    print("\nThank you for creating an account with us!")
    return account_details


def login_account(Account_details):
    print("\nPlease Login into your account with your credentials")
    login_account_number = input("\nPlease enter your account number: ")
    while login_account_number != Account_details['Account_Number']:
        print("This account number does not exist")
        login_account_number = input("\nPlease enter your account number again: ")

    login_pin = input("\nEnter your bank account pin: ")
    while login_pin != Account_details['password_pin']:
        print("Please Enter the right pin to login")
        login_pin = input("\nEnter your bank account pin: ")

    print(f"\nLogin successful! Welcome, {Account_details['name']}.")


def Deposit_func(Account_details):
    amount_money = input("\nHow much do you want to deposit in your account? ")
    while not amount_money.replace(".", "", 1).isdigit() or float(amount_money) <= 0:  
        print("\nThis value must be greater than zero.")
        amount_money = input("\nHow much do you want to deposit in your account? ")
    amount_money = float(amount_money)
    Account_details['Account Balance'] += amount_money
    print(f"\n{Account_details['name']}, your account has been credited with ${amount_money}")
    print(f"Your current balance is ${Account_details['Account Balance']}")


def Transfer_Money(Account_details):
    print(f"\nYour current balance is ${Account_details['Account Balance']}")
    Account_number_receiver = input("\nPlease enter the 8 digit bank account number of the receiver: ")
    while len(Account_number_receiver) != 8 or not Account_number_receiver.isdigit() or Account_number_receiver == Account_details['Account_Number']:
        print("Either you entered an invalid account or recipient account is the same as yours.")
        Account_number_receiver = input("\nPlease enter the 8 digit bank account number of the receiver again: ")

    Amount_to_send = input("\nEnter amount of money you want to send: ")
    while not Amount_to_send.replace(".", "", 1).isdigit() or float(Amount_to_send) <= 0:  
        print("Please enter a valid amount greater than zero.")
        Amount_to_send = input("Enter amount of money you want to send: ")
    Amount_to_send = float(Amount_to_send)

    if Amount_to_send >= Account_details['Account Balance']:
        print("\nYou do not have enough balance to perform this transaction.")
        print("Please make a deposit to credit your balance with enough money.")
    else:
        print(f"\nTransaction details:\nRecipient Account Number: {Account_number_receiver}\nAmount: ${Amount_to_send}")
        confirmation_pin = input("\nPlease Enter your bank account pin to complete transaction: ")
        while confirmation_pin != Account_details['password_pin']:
            print("Invalid pin")
            confirmation_pin = input("\nPlease Enter your bank account pin to complete transaction: ")

        Account_details['Account Balance'] -= Amount_to_send  
        print(f"\nYou have successfully sent ${Amount_to_send} to Account number {Account_number_receiver}.")
        print(f"Your available balance is ${Account_details['Account Balance']}")


def check_balance(Account_details):
    print(f"\n{Account_details['name']}, your current balance is ${Account_details['Account Balance']}")


if __name__ == "__main__":
    main()