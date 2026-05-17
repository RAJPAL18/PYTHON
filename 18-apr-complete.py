
'''1. A bank wants to automate its loan approval process. The system should take salary, 
credit score, and number of existing loans as input. If the salary is greater than or equal to 30000, 
then it should check the credit score. If the credit score is greater than or equal to 750,
 the loan should be approved. Otherwise, it should check the number of existing loans. 
If the existing loans are less than 2, the loan should be conditionally approved; otherwise, it should be rejected. 
If the salary is less than 30000, the loan should be rejected. Display the final loan status.

Input:
Salary = 40000
Credit Score = 720
Existing Loans = 1

Output:
Loan Status = Conditional Approval'''


salary = int(input("Enter Salary: "))
cscore = int(input("Enter Credit Score: "))
existing_loans = int(input("Enter Number of Existing Loans: "))

if salary >= 30000:
    if cscore >= 750:
        print("Loan Status = Approved")
    else:
        if existing_loans < 2:
            print("Loan Status = Conditional Approval")
        else:
            print("Loan Status = Rejected")
else:
    print("Loan Status = Rejected")



'''2. An e-commerce website provides discounts based on the cart value and user type. 
The system should take cart value and user type (premium or regular) as input.
 If the cart value is greater than or equal to 5000, then check the user type. If the user is premium,
 apply a 20% discount; otherwise, apply a 10% discount. If the cart value is less than 5000, 
then check if it is greater than or equal to 2000. If yes, apply a 5% discount; otherwise, 
no discount is applied. Display the final payable amount.

Input:
Cart Value = 6000
User Type = Premium

Output:
Final Amount = 4800'''
cart_value = float(input("Enter Cart Value: "))
user_type = input("Enter User Type (Premium/Regular): ")

if cart_value >= 5000:
    if user_type.lower() == "premium":
        discount = 0.20 * cart_value
    else:
        discount = 0.10 * cart_value
else:
    if cart_value >= 2000:
        discount = 0.05 * cart_value
    else:
        discount = 0

final_amount = cart_value - discount

print("Final Amount =", final_amount)


'''3. A smart electricity monitoring system categorizes usage levels for better energy management. 
The system should take the number of units consumed as input. If the units are greater than or equal to 100, then check further.
 If the units are greater than or equal to 300, assign "High Usage". Otherwise, check again. 
If the units are greater than or equal to 200, assign "Moderate Usage"; otherwise, assign "Normal Usage".
 If the units are less than 100, assign "Low Usage". Display the usage category.

Input:
Units = 220

Output:
Usage Category = Moderate Usage'''
units = int(input("Enter Units Consumed: "))

if units >= 100:
    if units >= 300:
        print("Usage Category = High Usage")
    else:
        if units >= 200:
            print("Usage Category = Moderate Usage")
        else:
            print("Usage Category = Normal Usage")
else:
    print("Usage Category = Low Usage")


'''4. A gym provides personalized plans based on age, weight, and fitness goal. 
The system should take age, weight, and goal (weight loss or muscle gain) as input.
 If the age is greater than or equal to 18, then check the weight. If the weight is greater than or
 equal to 80, then check the goal. If the goal is "weight loss", assign "Cardio Plan"; otherwise, assign 
"Strength Plan". If the weight is less than 80, assign "General Fitness Plan". If the age is less than 18, display
 "Not Allowed". Display the recommended plan.

Input:
Age = 25
Weight = 85
Goal = weight loss

Output:
Plan = Cardio Plan'''
age = int(input("Enter Age: "))
weight = float(input("Enter Weight: "))
goal = input("Enter Goal (weight loss/muscle gain): ")

if age >= 18:
    if weight >= 80:
        if goal == "weight loss":
            print("Plan = Cardio Plan")
        else:
            print("Plan = Strength Plan")
    else:
        print("Plan = General Fitness Plan")
else:
    print("Not Allowed")


'''5. An ATM system processes withdrawal requests. The system should take account balance,
 withdrawal amount, and PIN status (correct or incorrect) as input. If the balance is 
greater than or equal to the withdrawal amount, then check the withdrawal limit. 
If the withdrawal amount is less than or equal to 10000, then check the PIN.
 If the PIN is correct, display "Transaction Successful"; otherwise, display "Invalid PIN". 
If the withdrawal amount exceeds 10000, display "Limit Exceeded". If the balance is less than the
 withdrawal amount, display "Insufficient Balance".

Input:
Balance = 20000
Withdrawal Amount = 8000
PIN = correct

Output:
Transaction Successful'''
balance = float(input("Enter Account Balance: "))
withdrawal = float(input("Enter Withdrawal Amount: "))
pin_status = input("Enter PIN Status (correct/incorrect): ")

if balance >= withdrawal:
    if withdrawal <= 10000:
        if pin_status.lower() == "correct":
            print("Transaction Successful")
        else:
            print("Invalid PIN")
    else:
        print("Limit Exceeded")
else:
    print("Insufficient Balance")



'''6. A movie theatre calculates ticket prices based on age, show time, and day type.
 The system should take age, show time (morning/evening), and day type (weekday/weekend) as input. 
If the age is less than 18, then check the show time. If the show time is morning, ticket price is 100; otherwise, ticket price is 150.
 If the age is 18 or above, then check the show time. If the show time is evening, 
then check the day type. If it is weekend, ticket price is 300; otherwise, 250.
 If the show time is not evening, ticket price is 200. Display the ticket price.

Input:
Age = 25
Show Time = evening
Day = weekend

Output:
Ticket Price = 300'''

age = int(input("Enter Age: "))
show_time = input("Enter Show Time (morning/evening): ")
day = input("Enter Day Type (weekday/weekend): ")

if age < 18:
    if show_time == "morning":
        print("Ticket Price = 100")
    else:
        print("Ticket Price = 150")
else:
    if show_time == "evening":
        if day == "weekend":
            print("Ticket Price = 300")
        else:
            print("Ticket Price = 250")
    else:
        print("Ticket Price = 200")



'''7. A company calculates employee bonuses based on experience,
 performance rating, and salary. The system should take experience (in years), rating, and salary as input. 
If the experience is greater than or equal to 5, then check the rating. If the rating is greater than or equal to 4, then check the salary.
 If the salary is less than 50000, assign a 20% bonus; otherwise, assign a 10% bonus. If the rating is less than 4, assign a 5% bonus.
 If the experience is less than 5, no bonus is given. Display the bonus amount.

Input:
Experience = 6
Rating = 4
Salary = 40000

Output:
Bonus = 8000'''

experience = int(input("Enter Experience (in years): "))
rating = float(input("Enter Performance Rating: "))
salary = float(input("Enter Salary: "))

if experience >= 5:
    if rating >= 4:
        if salary < 50000:
            bonus = 0.20 * salary
        else:
            bonus = 0.10 * salary
    else:
        bonus = 0.05 * salary
else:
    bonus = 0

print("Bonus =", bonus)


'''8. A warehouse management system needs to identify the highest stock level among six different storage units to prioritize dispatch.
 The system should take the quantity of items stored in six units as input. It should compare all six values using nested conditions
 and determine which unit has the maximum stock. Display the highest stock value among all six units.

Input:
Unit1 = 120
Unit2 = 450
Unit3 = 300
Unit4 = 275
Unit5 = 500
Unit6 = 390

Output:
Highest Stock = 500'''

u1 = int(input("Enter Unit1: "))
u2 = int(input("Enter Unit2: "))
u3 = int(input("Enter Unit3: "))
u4 = int(input("Enter Unit4: "))
u5 = int(input("Enter Unit5: "))
u6 = int(input("Enter Unit6: "))

max_stock = u1

if u2 > max_stock:
    max_stock = u2

if u3 > max_stock:
    max_stock = u3

if u4 > max_stock:
    max_stock = u4

if u5 > max_stock:
    max_stock = u5

if u6 > max_stock:
    max_stock = u6

print("Highest Stock =", max_stock)
