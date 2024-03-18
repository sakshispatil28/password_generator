import streamlit as st
import random
import string

def generate_password(length):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Ensure at least one character from each set is included
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password with random characters from all sets
    for _ in range(length - 4):
        password.append(random.choice(lowercase + uppercase + digits + special_chars))

    # Shuffle the characters to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def main():
    st.title("Random Password Generator")
    st.divider()


    # User input for password length and quantity
    password_length = st.number_input("Password Length", min_value=8, max_value=100, value=12, step=1)
    quantity = st.number_input("Number of Passwords", min_value=1, max_value=10, value=1, step=1)

    if st.button("Generate Passwords"):
        for _ in range(quantity):
            password = generate_password(password_length)
            st.write(password)

if __name__ == "__main__":
    main()
