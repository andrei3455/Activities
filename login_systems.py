print("Login System")
print("============")
correct_user = "andreiabena"
correct_pass = "andrei3455"

username=input("Input Username: "
    )
password=input("Input Password: "
    )

if username == correct_user:
    if password == correct_pass:
        print("Welcome! Login successful.")
    else:
        print("Incorrect password.")
else:
    print("User not found.")
