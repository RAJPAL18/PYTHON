'''Assignment 1: Speed Calculator

Write a Python program that:

Accepts distance (in km) and time (in hours).
Calculates speed.

Input:
Distance = 120
Time = 2

Output:
Speed = 60 km/h
----------------------------------------'''

dis = int(input("Enter the distance in km : "))
t = int(input("Enter the Time in hours : "))
spd = dis/t
print(f"The speed = {spd} km/h ")

'''Assignment 2: Salary Calculator

Write a Python program that:

Accepts daily wage and number of days.
Calculates total salary.

Input:
Daily wage = 500
Days = 26

Output:
Salary = 13000
----------------------------------------------'''

wage,day = map(int,input("Enter the Daily wage & number of days : ").split())
print("The Salary = ",wage*day )

'''Assignment 3: Electricity Bill Calculator

Write a Python program that:

Accepts number of units.
Calculates bill (₹6 per unit).

Input:
Units = 100

Output:
Bill = 600'''

unit = int(input("Enter the Number of units : "))

print(" Bill = ₹ ",unit*6)


'''Assignment 4: Area of Rectangle

Write a Python program that:

Accepts length and breadth.
Calculates area.

Input:
Length = 10
Breadth = 5

Output:
Area = 50
------------------------------------------------'''
len = int(input("Enter the lenth of Rectangle : "))
br = int(input("Enter the Breadth of Rectangle : "))
print(f"The area of Rectangle of {len} lenth & {br} breadth is = ",len*br)



'''Assignment 5: Average Marks Calculator

Write a Python program that:

Accepts marks of 3 subjects.
Calculates average.

Input:
Marks = 80, 90, 70

Output:
Average = 80.0
------------------------------------------------------------'''

x,y,z = map(int,input("Enter the Marks of 3 subjects : ").split())

print(f"The avearge of {x},{y} & {z} is = ",(x+y+z)/3)


'''Assignment 6: Discount Calculator

Write a Python program that:

Accepts total amount.
Calculates 10% discount and final price.

Input:
Amount = 1000

Output:
Discount = 100
Final = 900'''

ttl = int(input("Enter the Total Amount : "))
dis = (ttl*10)/100

print(f"Discount on {ttl} = {dis}")
print("Final amount = ",ttl-dis)


'''Assignment 7: Circle Area Calculator

Write a Python program that:

Accepts radius.
Calculates area of circle.

Input:
Radius = 7

Output:
Area = 153.86
------------------------------------------------------------------------'''
r = float(input("Enter the radius of circle : "))
print(f"The area of radius {r} is ",3.14*r*r)

'''Assignment 8: Data Storage Converter

Write a Python program that:

Accepts value in MB.
Converts into GB.

Input:
MB = 2048

Output:
GB = 2.0'''

mb = int(input("Enter the values in MB : "))
gb=mb/1024
print(f"The value of {mb} MB is = {gb} GB")


'''Assignment 9: Fuel Cost Calculator

Write a Python program that:

Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.

Input:
Distance = 100
Mileage = 20
Petrol Price = 100

Output:
Cost = 500
'''

d = float(input("Enter the distance (km) : "))
m = float(input("Enter the mileage (km/litre) : "))
pp = float(input("Enter the petrol price : ₹"))

print("The cost = ₹ ",(d/m)*pp)

'''Assignment 10: Percentage Calculator

Write a Python program that:

Accepts total marks and obtained marks.
Calculates percentage.

Input:
Total = 500
Obtained = 400

Output:
Percentage = 80%'''

tm = float(input("Enter the total marks : "))
om = float(input("Enter the obtained marks : "))

per = (om/tm)*100

print(f"The percentage of {om} out of {tm} = {per} %")



'''Assignment 11: Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2
Seconds = 30

Output:
Total Seconds = 3750'''

h = int(input("Enyter the hours : "))
m = int(input("Enyter the minutes : "))
sec = int(input("Enyter the seconds : "))

totl = h*3600+m*60+sec

print("Total time = ",totl)

'''Assignment 12: Change Return System

Write a Python program that:

Accepts amount.
Calculates ₹100, ₹50, ₹10 notes.

Input:
Amount = 380

Output:
₹100 x 3
₹50 x 1
₹10 x 3'''

amt = int(input("enter the amount :"))

hun=amt//100
trem=amt%100
five=trem//50
frem=trem%50
ten=frem//10

print("Amount :",amt)

print(f"₹100 x {hun}\n₹50 x {five}\n₹10 x {ten}")


'''Assignment 13: Compound Interest Calculator

Write a Python program that:

Accepts principal, rate, and time.
Calculates compound interest.

Input:
Principal = 1000
Rate = 10
Time = 2

Output:
Amount = 1210.0
Compound Interest = 210.0'''

p = int(input("Enter the Principal Amount : "))
R = int(input("Enter the rate of interest : "))
t = int(input("Enter the time : "))
amt = int(p*((1+R/100)**t))

print("The total amount = ", amt)
print("The compound interest = ",(amt-p))


'''ssignment 14: Simple Profit or Loss Calculator

Write a Python program that:

Accepts cost price and selling price.
Calculates profit/loss and percentage.

Input:
Cost Price = 1000
Selling Price = 1200

Output:
Profit = 200
Profit % = 20.0'''

cp= int(input("Enter the cost price : "))
sp = int(input("Enter the selling price :"))

p=sp-cp
pper = (p/cp)*100
print("Profit = ",p)
print("Profit % = ",pper)


'''Assignment 15: Average Speed for Multiple Trips

Write a Python program that:

Accepts distance1, time1, distance2, time2.
Calculates average speed.

Input:
Distance1 = 60
Time1 = 1
Distance2 = 40
Time2 = 1

Output:
Average Speed = 50 km/h'''

d1,t1  = map(int,input("Enter the Distance 1 & time 1 : ").split())

d2,t2  = map(int,input("Enter the Distance 2 & time 2 : ").split())

avgr = (d1+d2)/(t1+t2)

print(f"The Average speed = {round(avgr,2)} km/h")