import random
import string

def generate_short_password():
    print("Welcome to the Short Password Generator!")
    
    # User input for password length (minimum 4, maximum 12)
    try:
        length = int(input("Enter the desired password length (between 4 and 12): "))
        if length < 4 or length > 12:
            print("Password length must be between 4 and 12.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
    # Character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all characters
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure at least one character from each category (if length allows)
    password = []
    if length >= 4:
        password = [
            random.choice(lowercase_letters),
            random.choice(uppercase_letters),
            random.choice(digits),
            random.choice(special_characters)
        ]
        remaining_length = length - 4
    else:
        remaining_length = length

    # Fill the remaining length with random characters
    password += random.choices(all_characters, k=remaining_length)
    
    # Shuffle the password to make it more random
    random.shuffle(password)
    
    # Convert list to string
    final_password = ''.join(password)
    print(f"Your generated password is: {final_password}")

# Run the short password generator
generate_short_password()