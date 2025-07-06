import random
import string

def generate_password(length):
    # Define the character sets
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine all character sets
    character_set = lower_case + upper_case + digits + special_chars

    # Generate a random password from the combined character set
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

# User Input: Prompt the user to specify the desired length of the password
length = int(input("Enter the desired length of the password: "))

# Generate the password
password = generate_password(length)

# Display the password
print(f"Generated Password: {password}")
