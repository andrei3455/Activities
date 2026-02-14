print("=== MOVIE TICKET SYSTEM ===")
day=input("Day (weekday/weekend): "
    )
customer=input("Customer type (regular/student/senior): "
    )
time=int(input("Show time (9-22 Hours): "
    ))
tickets=int(input("Number of tickets (1 or more): "
    ))

if time < 9 or time > 22 or tickets <= 0:
    print("Invalid input")
else:
    if day == "weekend":
        base_rate = 300.0
    else:
        base_rate = 200.0
    
    total = base_rate * tickets
    current_price = total

    student_discount = 0.0
    senior_discount = 0.0
    matinee_discount = 0.0
    group_discount = 0.0

    if customer == "student":
        student_discount = current_price * 0.20
        current_price = current_price - student_discount
    elif customer == "senior":
        senior_discount = current_price * 0.30
        current_price = current_price - senior_discount
        
    if time < 12:
        matinee_discount = current_price * 0.10
        current_price = current_price - matinee_discount
        
    if tickets >= 5:
        group_discount = current_price * 0.05
        current_price = current_price - group_discount

    print("--- RECEIPT ---")
    print(f"Base price: {base_rate} x {tickets} = {total}")
    
    if student_discount > 0:
        print(f"Student discount (20%): -{student_discount}")
    if senior_discount > 0:
        print(f"Senior discount (30%): -{senior_discount}")
    if matinee_discount > 0:
        print(f"Matinee discount (10%): -{matinee_discount}")
    if group_discount > 0:
        print(f"Group discount (5%): -{group_discount}")
        
    print(f"TOTAL: {current_price}")
    print("Thank you for your purchase!")
