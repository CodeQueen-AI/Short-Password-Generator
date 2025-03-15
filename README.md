# 📝 Short Password Generator 
> 📌 A simple program that generates a secure password with a length between 4 and 12 characters, ensuring at least one lowercase letter, uppercase letter, digit, and special character

## ⚙️ How It Works
# 1️⃣ User Input
The user enters a password length (between 4 and 12)

If the input is invalid, an error message is shown

# 2️⃣ Character Selection

Uses lowercase, uppercase, digits, and special characters from the string module

Ensures the password contains at least one of each type (if length is 4 or more)

# 3️⃣ Randomization & Output

Fills the remaining password length with random characters

Uses random.shuffle() to mix characters for better security

Displays the final password

# 🔧 Key Functions Used
🔹 random.choice() → Picks a random character from a given set

🔹 random.choices() → Selects multiple random characters at once

🔹 random.shuffle() → Shuffles the password to improve randomness

🔹 string.ascii_lowercase / ascii_uppercase / digits / punctuation → Provides character sets


### *Code Queen keeps it simple yet effective! ⚡*







