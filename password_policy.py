##Write a script to enforce basic security measures, like strong password policies.
import re
import getpass

def is_password_strong(password):
    # Define the password policy using regular expressions
    # At least 8 characters long
    # Contains at least one uppercase letter
    # Contains at least one lowercase letter
    # Contains at least one digit
    # Contains at least one special character
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    return re.match(pattern, password)

def main():
    print("Please enter a new password:")
    password = getpass.getpass()

    if is_password_strong(password):
        print("Password meets the strength requirements. It is strong!")
    else:
        print("Password does not meet the strength requirements. Please choose a stronger password.")

if __name__ == "__main__":
    main()
