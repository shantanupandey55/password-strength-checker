password = input("Enter your password: ")

score = 0

feedback = []

# Length check


if len(password) >= 8:
    score += 1
else:
    feedback.append("Password should be at least 8 characters long")

# Uppercase check


if any(char.isupper() for char in password):
    score += 1
else:
    feedback.append("Add at least one uppercase letter")

# Lowercase check


if any(char.islower() for char in password):
    score += 1
else:
    feedback.append("Add at least one lowercase letter")

# Number check
if any(char.isdigit() for char in password):
    score += 1
else:
    feedback.append("Add at least one number")

# Special character check


special_chars = "!@#$%^&*?"

if any(char in special_chars for char in password):
    score += 1
else:
    feedback.append("Add at least one special character")

# Password strength result

if score <= 2:
    print(" Weak Password")

elif score == 3 or score == 4:
    print("Medium Password")

else:
    print("Strong Password")

# Suggestions


if feedback:
    print("\nSuggestions:")

    for item in feedback:
        print("-", item)