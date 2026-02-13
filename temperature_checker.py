print("Temperature Checker")
print("==================")
temperature=int(input("Input Temperature: "))

if temperature>30:
    print("'Hot day! Stay hydrated.")
elif temperature<=30 and temperature >=10:
    print("Pleasant weather!")
elif temperature<10:
    print("It's cold outside, make sure to wear a jacket.")