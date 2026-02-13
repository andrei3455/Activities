print("Login System")
print("============")
correct_user = "admin"
correct_pass = "12345"

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