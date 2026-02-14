print("Grade Calculator")
print("================")
score=int(input("Input Score (0-100): "))

if score > 100 or score < 0:
    print("Invalid score! Please enter a number between 0 and 100.")
elif score >= 90:
    print("Grade: A - Excellent!")
elif score >= 80:
    print("Grade: B - Very Good!")
elif score >= 70:
    print("Grade: C - Good Job!")
elif score >= 60:
    print("Grade: D - Keep Improving!")
else:
    print("Grade: F - Try again!")
