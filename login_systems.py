print("Login System")
print("============")
correct_username = "andreiabena"
correct_password = "andrei3455"

username_input=input("Input Username: ")
password_input=input("Input Password: ")

if username_input == correct_username:
    if password_input == correct_password:
        print("Welcome! Login successful.")
    else:
        print("Incorrect password.")
else:
    print("User not found.")
