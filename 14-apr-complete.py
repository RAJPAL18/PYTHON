'''Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75'''

tba,gst,sc = map(int,input("Enter the Total bill amount ,GST %, Service charge  ").split(","))
num =  int(input("Enter the number of students : "))


final = ((tba*(gst+sc))/100)+tba
pp = final/num

print(f"Final Price = {final}\nEach Person Pays = {pp}")


'''Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0'''


mp,dp,ir,m = map(int,input("Enter Mobile price,Down payment,Interest rate,Months : ").split(","))
rp=mp-dp
i=(rp*10)/100
print("Remaining Amount = ",rp)
print("Total with Interest = ",rp+i)
print("Monthly EMI = ",(rp+i)/m)


'''Assignment 3: Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2
'''
'''Assignment 3: Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2
'''
m1,m2,m3,m4,m5=map(int,input("Enter the Marks of 5 subjects : ").split(","))
print("Total = ",(m1+m2+m3+m4+m5))
print("Average = ",(m1+m2+m3+m4+m5)/5)
print("Percentage = ",((m1+m2+m3+m4+m5)/500)*100)


'''Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km'''

speed= int(input("Enter the speed in km/h : "))
h,min= map(int,input("Enter the time in hour & minutes HH:MM : ").split(":"))

ttltime = h*60+min

tim = ttltime/60
print("Total Time = ",tim,"hours")
print("Total Distance = ",tim*speed,"km")



'''Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5'''

ms,wd,wpr=map(int,input("Enter Monthly salary,Working days,Working hours per day : ").split(","))

print("Salary per day = ",ms/wd)
print("Salary per hour =",ms/(wd*wpr))

'''Assignment 6: Data Storage Conversion

A user wants to convert data from GB into MB and KB.

Input:
Data = 5 GB

Expected Output:
In MB = 5120.0
In KB = 5242880.0
'''
gb= float(input("enter data in GB : "))
print("In MB = ",gb*1024)
print("In KB = ",gb*1024*1024)

'''Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67'''

ov = float(input("Enter the overs : "))
run = int(input("Enter the runs : "))
chov = ov*10
x=chov%10
chov=chov//10
ttl = chov*6+(x/6)

print("Total Balls = ",ttl)
print("Run Rate = ",run/ov)

'''Assignment 8: Compound Interest

A person invests money in a bank that provides compound interest annually.

Input:
Principal = 10000
Rate = 5%
Time = 2 years

Expected Output:
Amount after interest = 11025.0
'''
p = int(input("Enter the Principal Amount : "))
R = int(input("Enter the rate of interest : "))
t = int(input("Enter the time : "))
amt = int(p*((1+R/100)**t))

print("The total amount  = ", amt)
print("The compound interest = ",(amt-p))



'''Assignment 9: Petrol Cost Calculation

You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

Input:
Distance = 450 km
Mileage = 15 km/litre
Petrol price = 110/litre

Expected Output:
Petrol Used = 30.0 litres
Total Cost = 3300.0'''

d = float(input("Enter the distance (km) : "))
m = float(input("Enter the mileage (km/litre) : "))
pp = float(input("Enter the petrol price : ₹"))

print("Petrol Used = ",(d/m),"litres")
print("The cost = ₹ ",(d/m)*pp)


'''Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4'''

time = int(input("Enter the time in seconds :"))
hour=time//3600
hrem=time%3600
min = hrem//60
sec=time%60

print(f"Hours: {hour}, Minutes: {min}, Seconds: {sec}")

'''A billing system applies nested calculations with discounts and extra charges using brackets and unary operators.

Input:
50 + (10 * (+(2**3))) / 4 - (-6 % 4)
'''

a= 50 + (10 * (+(2**3))) / 4 - (-6 % 4)
print(a)

'''Assignment 12: Expression Evaluation

A gaming score system calculates bonus points using exponent and applies penalties using unary negative values and brackets.

Input:
100 - (20 * (3**2)) + (40 / (+5)) - (-3)'''

b=100 - (20 * (3**2)) + (40 / (+5)) - (-3)
print(b)


'''Assignment 13: Expression Evaluation

A shopping application applies offers using exponent and grouped calculations with unary adjustments.

Input:
25 + (5 * (6**2) // 3) - (-(8 % 5)) + (+2)'''

c= 25 + (5 * (6**2) // 3) - (-(8 % 5)) + (+2)
print(c)

'''Assignment 14: Expression Evaluation

A travel fare calculator computes total fare using grouped operations, power calculations, and unary adjustments.

Input:
(80 / (4 * 2)) * (+(2**2)) + 15 - (-(9 % 2))'''

d=(80 / (4 * 2)) * (+(2**2)) + 15 - (-(9 % 2))
print(d)


'''Assignment 15: Expression Evaluation

An electricity billing system uses nested brackets, exponent-based scaling, and unary corrections.

Input:
60 + (12 * (2**3) // (+(4))) - (-(10 % 3))'''

e = 60 + (12 * (2**3) // (+(4))) - (-(10 % 3))
print(e)


'''Assignment 16: Expression Evaluation

A performance evaluation system calculates final score using grouped operations, exponent, division, and unary adjustments.

Input:
45 + (15 * (2**2)) - (20 / (+(5))) + (-(7 % 3))'''

f=45 + (15 * (2**2)) - (20 / (+(5))) + (-(7 % 3))
print(f)