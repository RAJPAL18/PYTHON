'''1. Smart Voting & ID Verification System
   A government system verifies whether a citizen can vote and whether they have a valid ID.

* If age ≥ 18 → Eligible to vote
* If ID proof is available → Allowed inside booth

Input:
Enter age: 22
Do you have ID (yes/no): yes

Output:
Eligible to vote
Allowed inside booth'''

age=int(input("Enter your age  : "))
id  = input("Do you have ID (yes/no):")

if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible")

if id=="yes":
    print("Allowed inside booth")
else:
    print("Not Allowed inside booth")


'''2. Student Performance Analyzer
   A school wants to evaluate students based on marks.

* If marks ≥ 40 → Pass
* If marks ≥ 75 → Distinction

Input:
Enter marks: 80

Output:
Pass
Distinction'''

marks = int(input("Enter the marks :"))
if marks>=40:
    print("Pass")
else:
    print("Fail")

if marks>=75:
    print("Distinction")


'''3. E-Commerce Offer Engine
   An online store provides multiple offers independently:

* If cart value ≥ 500 → Free delivery
* If cart value ≥ 1000 → 10% discount coupon

Input:
Enter cart value: 1200

Output:
Free delivery applied
Discount coupon unlocked'''

cart = int(input("Enter cart value:"))

if cart>=500:
    print("Free delivery applied")
else:
    print("No Free delivery")

if cart>=1000:
    print("Discount coupon unlocked")


'''4. Gym Membership Eligibility Checker
   A gym checks multiple conditions:

* If age ≥ 18 → Allowed for gym
* If BMI > 25 → Suggest weight loss program

Input:
Enter age: 25
Enter BMI: 27'''
age1=int(input("Enter age:"))
bmi= int(input("Enter BMI:"))

if age1>=18:
    print("Allowed for gym")
else:
    print("Not Allowed for gym")

if bmi >25:
    print("Enroll in weight loss program")


'''5. Banking Security System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password

Input:
Enter username: admin
Enter password: secure123

Output:
Valid user
Strong password'''

usr=input("Enter username:")
pas = input("Enter password:")

if usr=="admin":
    print("Valid user")
else:
    print("Invalid user")

if len(pas)>=8:
    print("Strong password")
else:
    print("Weak password")


'''6. Weather Monitoring System
   A system checks weather conditions:

* If temperature ≥ 30 → Hot day
* If humidity ≥ 70 → High humidity alert

Input:
Enter temperature: 32
Enter humidity: 75

Output:
Hot day
High humidity alert'''

temp = int(input("Enter temperature:"))
hum = int(input("Enter humidity:"))

if temp>=30:
    print("Hot day")
else:
    print("Not Hot day")

if hum>=70:
    print("High humidity alert")


'''7. Salary Benefits System
   A company provides benefits:

* If salary ≥ 30000 → Eligible for PF
* If salary ≥ 50000 → Eligible for bonus

Input:
Enter salary: 55000

Output:
PF applicable
Bonus applicable
'''

sal = int(input("Enter salary:"))

if sal>=30000:
    print("PF applicable")
else:
    print("PF not applicable")

if sal>=50000:
    print("Bonus applicable")


'''8. Number Property Checker
   A system evaluates number properties:

* If number % 2 == 0 → Even number
* If number % 5 == 0 → Divisible by 5

Input:
Enter number: 20

Output:
Even number
Divisible by 5
'''

num = int(input("Enter number:"))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd  number")

if num % 5==0:
    print("Divisible by 5")


'''9. Library Access System
   A library checks:

* If membership is active → Entry allowed
* If books issued < 3 → Can issue more books

Input:
Membership active (yes/no): yes
Books issued: 2

Output:
Entry allowed
Can issue more books'''

mem=input("Membership active (yes/no):")
book = int(input("Books issued:"))

if mem == "yes":
    print("Entry allowed")
else:
    print("Entry not allowed")

if book<3:
    print("Can issue more books")



'''10. Online Exam System
    System evaluates exam conditions:

* If marks ≥ 40 → Pass
* If attendance ≥ 75 → Eligible for certificate

Input:
Enter marks: 60
Enter attendance: 80

Output:
Pass
Eligible for certificate'''

mark1=int(input("Enter marks:"))
atnd = int(input("Enter attendance: "))

if mark1>=40:
    print("Pass")
else:
    print("Fail")

if atnd>=75:
    print("Eligible for certificate")