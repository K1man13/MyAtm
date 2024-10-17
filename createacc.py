accounts = {}

def create_account():
    print("Attempting to create account...")  # Debugging
    username = input("Please enter your name: ")
    if username in accounts:
        print("Account already exists.")
        return
    
    pin = input("Set a 4-digit PIN (4 digits only): ")
    while len(pin) != 4 or not pin.isdigit():
        print("Invalid PIN. Please enter a 4-digit PIN.")
        pin = input("Set a 4-digit PIN (4 digits only): ")
    
    initial_balance = float(input("Please enter initial balance: "))
    accounts[username] = {'pin': pin, 'balance': initial_balance}
    print(f"Account created successfully for {username} with an initial balance of KES {initial_balance}.")
    print("Current accounts:", accounts)  # Debugging

def login():
    print("Attempting to log in...")  # Debugging
    username = input("Please enter your name: ")
    if username in accounts:
        pin = input("Enter your PIN: ")
        if accounts[username]['pin'] == pin:
            print("Login successful!")  # Debugging
            return username
        else:
            print("Incorrect PIN.")
            return None
    else:
        print("Username not found.")
        return None

def check_balance(username):
    print(f"Your current balance is: KES {accounts[username]['balance']}")  # Debugging

def deposit(username):
    amount = float(input("Enter deposit amount: "))
    if amount > 0:
        accounts[username]['balance'] += amount
        print(f"KES {amount} deposited successfully.")
    else:
        print("Invalid deposit amount.")

def withdraw(username):
    amount = float(input("Enter withdrawal amount: "))
    if amount > 0:
        if amount <= accounts[username]['balance']:
            accounts[username]['balance'] -= amount
            print(f"KES {amount} withdrawn successfully.")
        else:
            print("Insufficient funds.")
    else:
        print("Invalid withdrawal amount.")

def atm_menu(username):
    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            check_balance(username)
        elif choice == '2':
            deposit(username)
        elif choice == '3':
            withdraw(username)
        elif choice == '4':
            print("Thank you for using Python ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

def main_menu():
    while True:
        print("\n1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            username = login()
            if username:
                atm_menu(username)
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
