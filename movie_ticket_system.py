print("=== MOVIE TICKET SYSTEM ===")
day_type=input("Day (weekday/weekend): ")
customer_type=input("Customer type (regular/student/senior): ")
show_time_hours=int(input("Show time hours (1-24 Hours): "))
num_tickets=int(input("Number of tickets (1 or more): "))

if show_time_hours < 1 or show_time_hours > 24 or num_tickets <= 0:
    print("Invalid input")
else:
    if day_type == "weekend":
        base_rate = 300.0
    else:
        base_rate = 200.0
    
    total = base_rate * num_tickets
    current_price = total

    student_discount = 0.0
    senior_discount = 0.0
    matinee_discount = 0.0
    group_discount = 0.0

    if customer_type == "student":
        student_discount = current_price * 0.20
        current_price = current_price - student_discount
    elif customer_type == "senior":
        senior_discount = current_price * 0.30
        current_price = current_price - senior_discount
        
    if show_time_hours < 12:
        matinee_discount = current_price * 0.10
        current_price = current_price - matinee_discount
        
    if num_tickets >= 5:
        group_discount = current_price * 0.05
        current_price = current_price - group_discount

    print("--- RECEIPT ---")
    print(f"Base price: {base_rate} x {num_tickets} = {total}")
    
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
