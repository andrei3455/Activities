print("Grade Calculator")
print("================")
print("Grade: A - Excellent!")
print("Grade: B - Very Good!")
print("Grade: C - Good Job!")
print("Grade: D - Keep Improving!")
print("Grade: F - Try again!")
print(" ")
student_score=int(input("Input Score (0-100): "))
if student_score > 100 or student_score < 0:
    print("Invalid score! Please enter a number between 0 and 100.")
elif student_score >= 98:
    print("Grade: A+ - Excellent!")
elif student_score >= 93:
    print("Grade: A - Excellent!")
elif student_score >= 90:
    print("Grade: A- - Excellent!")
elif student_score >= 87:
    print("Grade: B+ - Very Good!")
elif student_score >= 83:
    print("Grade: B - Very Good!")
elif student_score >= 80:
    print("Grade: B- - Very Good!")
elif student_score >= 77:
    print("Grade: C+ - Good Job!")
elif student_score >= 73:
    print("Grade: C - Good Job!")
elif student_score >= 70:
    print("Grade: C- - Good Job!")
elif student_score >= 67:
    print("Grade: D+ - Keep Improving!")
elif student_score >= 60:
    print("Grade: D - Keep Improving!")
else:
    print("Grade: F - Try again!")
