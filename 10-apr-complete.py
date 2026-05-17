'''========================================
Assignment 1: Time Converter
========================================

An event management company is developing a scheduling system. One of the key tasks is converting the duration of events from total seconds (which their sensor system records) into a more human-readable format of hours, minutes, and seconds.

Write a Python program that:
- Accepts the total event duration in seconds as input.
- Calculates how many hours, minutes, and seconds it corresponds to.
- Displays the output in the format:
  Hours: x, Minutes: y, Seconds: z

Sample Input:
Total event duration in seconds: 3672

Sample Output:
Hours: 1, Minutes: 1, Seconds: 12

'''
time = int(input("Enter the time in seconds :"))
hour=time//3600
hrem=time%3600
min = hrem//60
sec=hrem%60

print(f"Hours: {hour}, Minutes: {min}, Seconds: {sec}")


'''========================================
Assignment 2: Lifetime Calculator
========================================

You are developing a feature for a health and wellness mobile app that helps users understand how long they've been alive in a more tangible way.

Write a Python program that:
- Accepts the user’s age in years as input.
- Calculates the approximate number of:
  Days lived (1 year = 365 days)
  Hours lived
  Minutes lived
- Displays the output in the format:

You've lived approximately:
Days: xxx
Hours: yyy
Minutes: zzz

Sample Input:
Enter your age in years: 18

Sample Output:
You've lived approximately:
Days: 6570
Hours: 157680
Minutes: 9460800

'''

age = int(input("Enter the age in years :"))
day = age*365
hours = day*24
minutes = hours*60
print(f"You've lived approximately:\n\tDays\t: {day}\n\tHours\t: {hours}\n\tMinutes\t: {minutes}")


'''========================================
Assignment 3: Split the Bill
========================================

You and your friends went out to eat. The bill was quite high and you want to split it evenly.

Write a Python program that:
- Accepts the total bill amount.
- Accepts the number of friends.
- Displays how much each person should pay.

Example:
Total bill = 1250
Friends = 5
Each should pay = 250.0'''

total = float(input("Enter the total bil amount : "))
no = int(input("Enter the number of friends : "))

each = total/no

print(f"\tTotal bill = {total}\n\tFriends = {no}\n\tEach should pay = {each} ")

'''========================================
Assignment 4: Travel Fare Calculator
========================================

A cab company charges ₹15 per kilometer.

Write a Python program that:
- Accepts the number of kilometers traveled.
- Calculates the total fare.
- Displays the result.

Example:
Distance = 20 km
Total fare = ₹300'''

km=int(input("Enter number of kilometers traveled. : "))
fare = km*15
print(f"Distance = {km}\nTotal fare = ₹{fare}")


'''========================================
Assignment 5: Shopping Tax Calculator
========================================

Your shopping cart total doesn’t include tax. A 12% GST is applied.

Write a Python program that:
- Accepts the cart total amount.
- Calculates 12% tax.
- Displays the tax and final total amount.

Example:
Cart = ₹2000
Tax = ₹240
Total = ₹2240'''

amnt=int(input("Enter the cart total amount : "))
tax= (12*amnt)/100

print(f"Cart = ₹{amnt}\nTax = ₹{tax}\nTotal = ₹{amnt+tax}")

'''========================================
Assignment 6: Smart Coin Machine
========================================

You insert an amount into a vending machine. It returns coins using the largest denominations possible (₹10 and ₹5).

Write a Python program that:
- Accepts the total amount.
- Calculates how many ₹10 coins and ₹5 coins will be dispensed.
- Displays the result.

Example:
Amount = ₹35
Output = ₹10 x 3, ₹5 x 1'''

amt = int(input("enter the amount :"))

ten=amt//10
rem=amt%10
five=rem//5

print("Amount :",amt)
print(f"₹10 x {ten}\n₹5 x {five}")



'''========================================
Assignment 7: Temperature Converter
========================================

A weather application needs to convert temperature from Celsius to Fahrenheit.

Write a Python program that:
- Accepts temperature in Celsius as input.
- Converts it to Fahrenheit using the formula:
  F = (C × 9/5) + 32
- Displays the result.

Example:
Celsius = 25
Fahrenheit = 77.0'''

temp = int(input("Enter the temperature in Celsius : "))
fah = (temp * 9/5) + 32

print(f"Celsius = {temp}\nFahrenheit = {fah}")


'''========================================
Assignment 8: Simple Interest Calculator
========================================

A bank wants to help customers calculate the simple interest on their savings.

Write a Python program that:
- Accepts principal amount, rate of interest, and time (in years) as input.
- Calculates the simple interest using the formula:
  SI = (P × R × T) / 100
- Displays the simple interest.

Example:
Principal = 1000
Rate = 5
Time = 2
Simple Interest = 100.0'''

p,r,t = map(int,input("Enter the principal amount, rate of interest, and time (in years) : ").split())

si=(p*r*t)/100

print(f"Principal = {p}\nRate = {r}\nTime = {t}\nSimple Interest = {si}")