print("Eligibility Checker")
print("===================")
age=int(input("Input Age: "))
has_id_input=input("Do you have a valid ID? (yes/no): ")
has_id=has_id_input=="yes"
if age >= 60 and has_id:
    print("Eligible! (Senior Discount Applied!)")
elif age >= 18 and has_id:
    print("Eligible!")
else:
    print("Not eligible")
