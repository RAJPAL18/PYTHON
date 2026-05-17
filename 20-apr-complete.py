'''1. Electricity Department Billing System


The electricity department of a city wants to automate the monthly bill generation process for its customers. The bill is calculated based on slab-wise unit consumption:

* First 100 units are charged at ₹5 per unit
* Next 100 units (101–200) are charged at ₹7 per unit
* Units above 200 are charged at ₹10 per unit

Write a Python program to calculate the total electricity bill based on the number of units consumed.

Input:
Enter units consumed: 250

Output:
Total Electricity Bill: ₹1950'''

unit = int(input("Enter units consumed : "))

if unit<=100:
    bill=unit*5
elif (unit >=101 and unit<=200):
    bill = 500+(unit-100)*7
else:
    bill = 1200+(unit-200)*10

print(bill)

'''2. College Result Processing System


A college wants to generate grades for students automatically based on their marks in an exam. The grading criteria are as follows:

* 90 and above → Grade A
* 75 to 89 → Grade B
* 60 to 74 → Grade C
* 50 to 59 → Grade D
* Below 50 → Fail
Write a Python program to display the grade of a student.

Input:
Enter marks: 67

Output:
Grade: C
'''

marks = int(input("Enter the marks : "))
if marks>=90:
    print("Grade A")
elif (marks<=89 and marks>=75):
    print("Grade B")
elif (marks<=74 and marks>=60):
    print("Grade C")
elif (marks<=59 and marks>=50):
    print("Grade D")
else:
    print("Fail")


'''3. Income Tax Department System

The Income Tax Department needs a system to calculate tax payable by citizens based on their annual income:

* Up to ₹2,50,000 → No tax
* ₹2,50,001 to ₹5,00,000 → 5% tax
* ₹5,00,001 to ₹10,00,000 → 20% tax
* Above ₹10,00,000 → 30% tax

Write a Python program to calculate the tax amount.

Input:
Enter annual income: 800000

Output:
Tax Payable: ₹110000'''

income = int(input("Enter annual income: "))
if income<=2_50_000:
    print("No Tax")
elif (income<=5_00_000 and income>=2_50_001):
    tax = income*0.05
    print()






'''4. E-Commerce Discount Engine


An online shopping platform provides discounts to customers based on their total purchase amount:

* Above ₹5000 → 20% discount
* ₹2000 to ₹5000 → 10% discount
* Below ₹2000 → 5% discount

Write a Python program to calculate the final amount after discount.

Input:
Enter purchase amount: 4500

Output:
Final Amount: ₹4050
'''

amnt = int(input("Enter purchase amount:"))
if amnt<2000:
    dis = amnt*0.05
    print("Final Amount: ",amnt-dis)
elif (amnt>=2000 and amnt<=5000):
    dis = amnt*0.10
    print("Final Amount: ",amnt-dis)
else:
    dis = amnt*0.20
    print("Final Amount: ",amnt-dis)

'''5. Cinema Ticket Booking System


A cinema hall charges ticket prices based on the age of the customer:

* Children (below 12 years) → ₹100
* Adults (12 to 60 years) → ₹200
* Senior citizens (above 60 years) → ₹150

Write a Python program to determine the ticket price.

Input:
Enter age: 10

Output:
Ticket Price: ₹100
'''

age = int(input("Enter age: "))
if age<12:
    print("Ticket Price: ₹100")
elif age>=12 and age<=60:
    print("Ticket Price: ₹200")
else:
    print("Ticket Price: ₹150")

'''6. Company Bonus Distribution System


A company wants to calculate bonuses for employees based on their years of experience:

* More than 10 years → 20% bonus
* 5 to 10 years → 10% bonus
* 2 to 5 years → 5% bonus
* Less than 2 years → No bonus

Write a Python program to calculate the bonus amount.

Input:
Enter salary: 50000
Enter years of experience: 6

Output:
Bonus Amount: ₹5000'''

sal = int(input("Enter salary : "))
year = int(input("Enter years of experience:"))

if year<2:
    print("No Bonus")
elif year>=2 and year<5:
    print("Bonus Amount: ₹",sal*0.05)
elif year<=10 and year>=5:
    print("Bonus Amount: ₹",sal*0.1)
else:
    print("Bonus Amount: ₹",sal*0.2)

'''7. Banking Withdrawal Limit System


A bank wants to set withdrawal limits based on the available account balance:

* Balance less than ₹1000 → Withdrawal not allowed
* ₹1000 to ₹5000 → Maximum withdrawal ₹1000
* Above ₹5000 → Maximum withdrawal ₹5000

Write a Python program to display the withdrawal limit.

Input:
Enter account balance: 3500

Output:
Maximum Withdrawal Limit: ₹1000
'''

amt = int(input("Enter account balance: "))
if amt<1000:
    print("Withdrawal not allowed")
elif amt>=1000 and amt <=5000:
    print("Maximum withdrawal ₹1000")
else:
    print("Maximum withdrawal ₹5000")

'''8. Weather Monitoring System

A weather monitoring system classifies the weather condition based on temperature:

* Below 0°C → Freezing
* 0°C to 20°C → Cold
* 21°C to 35°C → Warm
* Above 35°C → Hot

Write a Python program to classify the weather.

Input:
Enter temperature: 38

Output:
Weather Condition: Hot
'''
tem = int(input("Enter temperature: "))
if tem <0:
    print("Freezing")
elif tem>=0 and tem<=20:
    print("Cold")
elif  tem>=21 and tem<=35:
    print("Warm")
else:
    print("Hot")


'''9. Student Attendance Eligibility System

A college determines whether a student is eligible to sit for exams based on attendance percentage:

* 75% and above → Eligible
* 60% to 74% → Eligible with warning
* Below 60% → Not eligible

Write a Python program to check eligibility.

Input:
Enter attendance percentage: 58

Output:
Status: Not Eligible
'''

atd = int(input("Enter attendance percentage: "))
if atd>=75:
    print(" Eligible")
elif atd<=74 and atd>=60:
    print("Eligible with warning")
else:
    print("Not Eligible")


'''10. Mobile Data Plan Advisor


A telecom company suggests the most suitable data plan based on a user’s daily data usage:

* More than 3GB/day → Premium Plan
* 1GB to 3GB/day → Standard Plan
* Less than 1GB/day → Basic Plan

Write a Python program to recommend a plan.

Input:
Enter daily data usage: 0.8

Output:
Recommended Plan: Basic Plan'''

data= float(input("Enter daily data usage: "))
if data > 3:
    print("Premium Plan")
elif data>=1 and data<=3:
    print("Standard Plan")
else:
    print(" Basic Plan")


'''11. Railway Ticket Fare System


A railway system calculates ticket fare based on distance and travel class:

* Distance ≤100 km:
  Sleeper → ₹100, AC → ₹200
* Distance 101–500 km:
  Sleeper → ₹300, AC → ₹600
* Distance >500 km:
  Sleeper → ₹500, AC → ₹1000

Write a Python program to calculate ticket fare.

Input:
Enter distance: 350
Enter class: AC

Output:
Total Fare: ₹600
'''

dist = int(input("Enter distance: "))
clas = input("Enter class (Sleeper/AC):")

if dist<=100:
    if clas =="sleeper":
        print("Total Fare: ₹100")
    else:
         print("Total Fare: ₹200")

elif dist>100 and dist <=500:
    if clas =="sleeper":
        print("Total Fare: ₹300")
    else:
         print("Total Fare: ₹600")

else:
    if clas =="sleeper":
        print("Total Fare: ₹500")
    else:
         print("Total Fare: ₹1000")
'''12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680'''


bil = int(input("Enter bill amount: "))

if bil<=1000:
    fb = bil*0.05
    print("Final Bill Amount: ₹",fb+bil)

elif bil>1000 and bil<=5000:
    if bil>3000:
        fb = (bil*0.12)+200
        print("Final Bill Amount: ₹",fb+bil)

    else:
        fb = (bil*0.12)
        print("Final Bill Amount: ₹",fb+bil)
else:
    fb=(bil*0.18)+200
    print("Final Bill Amount: ₹",fb+bil)



'''13. Employee Performance Appraisal System


A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
  If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 18000
Enter rating: 4

Output:
Revised Salary: ₹23600
'''

srly = int(input("Enter salary:"))
rat = int(input("Enter Rating(1-5):"))

if rat >4:
    if srly<20000:
        rs= srly + (srly*0.25) +2000
        print("Revised Salary: ₹",rs)
    else:
        rs= srly + (srly*0.25)
        print("Revised Salary: ₹",rs)
elif rat<5 and rat>3:
     if srly<20000:
        rs= srly + (srly*0.20) +2000
        print("Revised Salary: ₹",rs)
     else:
        rs= srly + (srly*0.20)
        print("Revised Salary: ₹",rs)
elif rat>2 and rat<4:
    rs= srly + (srly*0.10)
    print("Revised Salary: ₹",rs)

elif rat>1 and rat<3:
    rs= srly + (srly*0.05)
    print("Revised Salary: ₹",rs)
else:
    print("No hike")
    print("Revised Salary: ₹",srly)


'''14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000'''

cc = input("Enter course category (Programming/Design/Marketing) : ")
ut = input("Enter user type (student/Working Professional/others):")

if cc=="programming":
    if ut=="student":
        cf = 5000-(5000*0.2) 
    elif ut=="working professional":
        cf = 5000-(5000*0.1)
    else:
        cf = 5000
elif cc=="design":
     if ut=="student":
        cf = 4000-(4000*0.2)
     elif ut=="working professional":
        cf = 4000-(4000*0.1)
     else:
        cf = 4000
else:
     if ut=="student":
        cf = 3000-(3000*0.2)
     elif ut=="working professional":
        cf = 3000-(3000*0.1)
     else:
        cf = 3000


print(cf)


'''15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220'''

vt = input("Enter the Vehicle type (Bike/Car/Bus) : ")
hour = int(input("Enter the Hours parked : "))
if vt=="bike" or vt =="Bike":
   if hour<=5:
      fee = hour*10
   else:
      fee = (hour*10)+100
elif vt=="car" or vt=="Car":
   if hour<=5:
      fee = hour*20
   else:
      fee = (hour*20)+100
else:
   if hour<=5:
      fee = hour*50
   else:
      fee = (hour*50)+100

print("Total Parking Fee: ₹",fee)
    