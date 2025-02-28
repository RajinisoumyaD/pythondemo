import random
import getpass
import time
import os

# User database (in a real application, you would use a more secure storage method)
users = {
    "admin": "admin123",
    "user1": "password123"
}

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def register_user():
    """Register a new user with username and password."""
    clear_screen()
    print("\n===== USER REGISTRATION =====")
    
    while True:
        username = input("\nEnter a username (or 'cancel' to go back): ")
        
        if username.lower() == 'cancel':
            return False
            
        if username in users:
            print("Username already exists. Please choose another.")
            continue
            
        if len(username) < 3:
            print("Username must be at least 3 characters long.")
            continue
            
        break
    
    while True:
        password = getpass.getpass("Enter a password (min 6 characters): ")
        
        if len(password) < 6:
            print("Password must be at least 6 characters long.")
            continue
            
        confirm_password = getpass.getpass("Confirm password: ")
        
        if password != confirm_password:
            print("Passwords don't match. Try again.")
            continue
            
        break
    
    # Add new user to database
    users[username] = password
    print("\nRegistration successful!")
    time.sleep(1.5)
    return True

def login():
    """Authenticate user with username and password."""
    attempts = 3
    
    while attempts > 0:
        clear_screen()
        print("\n===== LOGIN =====")
        print(f"Attempts remaining: {attempts}")
        
        username = input("\nUsername (or 'register' for new user): ")
        
        if username.lower() == 'register':
            register_result = register_user()
            if register_result:
                continue
            else:
                attempts = 3
                continue
                
        if username not in users:
            print("Username not found.")
            attempts -= 1
            time.sleep(1)
            continue
            
        password = getpass.getpass("Password: ")
        
        if users[username] == password:
            print("\nLogin successful!")
            time.sleep(1)
            return username
            
        print("Incorrect password.")
        attempts -= 1
        time.sleep(1)
    
    print("\nToo many failed attempts. Please try again later.")
    return None

def guess_the_number(username):
    """The main game function."""
    target = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    score = 100
    
    clear_screen()
    print(f"\n===== WELCOME TO GUESS THE NUMBER, {username.upper()} =====")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")
    print("Each wrong guess reduces your score.\n")
    
    while attempts < max_attempts:
        try:
            user_input = input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess (or 'Q' to quit): ")
            
            if user_input.upper() == 'Q':
                print(f"\nGiving up? The number was {target}.")
                break
                
            guess = int(user_input)
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
                
            attempts += 1
            
            if guess == target:
                print(f"\nCONGRATULATIONS! You guessed correctly in {attempts} attempts!")
                print(f"Final score: {score} points")
                break
            elif guess < target:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
                
            # Reduce score with each wrong guess
            score -= 15 if attempts > 1 else 0
            
        except ValueError:
            print("Please enter a valid number or 'Q' to quit.")
    
    if attempts == max_attempts and guess != target:
        print(f"\nGame over! You've used all {max_attempts} attempts.")
        print(f"The number was {target}.")
        print("Score: 0 points")
    
    input("\nPress Enter to continue...")

def main_menu(username):
    """Display the main menu for the game."""
    while True:
        clear_screen()
        print(f"\n===== MAIN MENU =====")
        print(f"Logged in as: {username}")
        print("\n1. Play Guess the Number")
        print("2. Game Rules")
        print("3. Change Password")
        print("4. Logout")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            guess_the_number(username)
        elif choice == '2':
            clear_screen()
            print("\n===== GAME RULES =====")
            print("1. The computer selects a random number between 1 and 100.")
            print("2. You have 7 attempts to guess the correct number.")
            print("3. After each guess, you'll be told if your guess was too high or too low.")
            print("4. You start with 100 points, and lose 15 points for each wrong guess.")
            print("5. The game ends when you guess correctly or run out of attempts.")
            input("\nPress Enter to return to the menu...")
        elif choice == '3':
            change_password(username)
        elif choice == '4':
            print("\nLogging out...")
            time.sleep(1)
            return
        else:
            print("\nInvalid choice. Please try again.")
            time.sleep(1)

def change_password(username):
    """Allow user to change their password."""
    clear_screen()
    print("\n===== CHANGE PASSWORD =====")
    
    current_password = getpass.getpass("Enter current password: ")
    
    if current_password != users[username]:
        print("Incorrect password!")
        time.sleep(1.5)
        return
    
    while True:
        new_password = getpass.getpass("Enter new password (min 6 characters): ")
        
        if len(new_password) < 6:
            print("Password must be at least 6 characters long.")
            continue
            
        confirm_password = getpass.getpass("Confirm new password: ")
        
        if new_password != confirm_password:
            print("Passwords don't match. Try again.")
            continue
            
        break
    
    users[username] = new_password
    print("\nPassword changed successfully!")
    time.sleep(1.5)

# Main program
if __name__ == "__main__":
    while True:
        clear_screen()
        print("\n===== GUESS THE NUMBER GAME =====")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        
        menu_choice = input("\nSelect an option (1-3): ")
        
        if menu_choice == '1':
            logged_user = login()
            if logged_user:
                main_menu(logged_user)
        elif menu_choice == '2':
            register_user()
        elif menu_choice == '3':
            clear_screen()
            print("\nThank you for playing! Goodbye.")
            break
        else:
            print("\nInvalid option. Please try again.")
            time.sleep(1)