import string
print(string.punctuation)
any(char in string.punctuation for char in "password")
# Password Length Checker
# This script checks if a given password meets the minimum length requirement.
input_password = input("Enter your password: ")
min_length = 8
has_upper = any(char.isupper() for char in input_password)
has_lower = any(char.islower() for char in input_password)
has_digit = any(char.isdigit() for char in input_password)
has_special = any(char in string.punctuation for char in input_password)
if len(input_password) < min_length:
    print(f"Password; is too short. It must be at least {min_length} characters long.")
if not has_upper:
    print("Password must contain at least one uppercase letter.")
if not has_lower:
    print("Password must contain at least one lowercase letter.")
if not has_digit:
    print("Password must contain at least one digit.")
if not has_special:
    print("Password must contain at least one special character.")
    print(f"Password must be at least {min_length} characters long.")
    print(f"Your password is {len(input_password)} characters long.")
else:
    print("Password length is sufficient.")
# This script prompts the user to enter a password and checks if it meets the minimum length requirement
# of 8 characters. If the password is too short, it informs the user
