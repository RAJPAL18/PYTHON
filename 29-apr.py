'''1. Triple Operation Prime Verification System

A cybersecurity company generates a security score from entered access code.

Write a program to:
- Find sum of digits of the number
- Reverse the number
- Find absolute difference between original number and reverse
- Add digit sum and difference
- Check whether final result is Prime or Not Prime

Input:
4215

Output:
Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime'''
import math
num = int(input("Enter a number: "))
temp=num
rev=0
sum=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    sum=sum+rem
    num=num//10

dif=abs(temp-rev)
final = sum+dif
print("Sum of Digits = ",sum)
print("Reverse = ", rev)
print("Difference = ",dif)
print("Final Result = ",final)
for i in range(2,int(math.sqrt(final))+1):
    if final%i==0:
        print("Not Prime")
        break

'''2. Multi Stage Prime Lock System

A smart locker opens only if final derived number is prime.

Write a program to:

- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not

Input:
234

Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime'''
import math
num = int(input("Enter a number: "))
temp=num

sum=0
mul=1
while num>0:
    rem=num%10
    mul=mul*rem
    sum=sum+rem
    num=num//10
dif=abs(mul-sum)
count=0
for i in str(dif):
    count+=1
final=dif+count
print("Sum = ",sum)
print("Product = ",mul)
print("Difference = ",dif)
print("Digits = ",count)

print("Final Result = ",final)
for i in range(2,int(math.sqrt(final))+1):
    if final%i==0:
        print("Not Prime")
        break
    else:
        print("Prime")
        break



'''3. Perfect Number Reward System

A gaming company rewards users if entered number is a Perfect Number.

(Perfect Number = sum of proper factors equals number)

Write a program using for-else loop to:

- Find sum of proper factors
- If sum equals number print Reward Unlocked
- Else print Try Again

Input:
6

Output:
Reward Unlocked'''

num = int(input("Enter a number: "))

sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i


    if sum==num:
        print("Reward Unlocked")
        break
else:
    print("Try Again")

'''Unique Digit Security Scanner

A smart locker accepts only numbers whose all digits are unique.

Write a program using for-else loop to:

- Check every digit
- If any repeated digit found reject
- Else accept

Input:
57294

Output:
Valid Unique Code
'''
num = int(input("Enter Number = "))

temp = num

for i in range(10):   # check digits 0 to 9
    count = 0
    temp = num

    while temp > 0:
        d = temp % 10
        if d == i:
            count += 1
        temp //= 10

    if count > 1:
        print("Invalid Code")
        break
else:
    print("Valid Unique Code")

'''5 Number Stability Analyzer

A science lab studies whether digits are in increasing order.

Write a program using for-else loop:

- If every next digit is greater than previous print Stable Number
- Else Unstable Number

Input:
12359

Output:
Stable Number'''
num = int(input("Enter Number = "))

prev = num % 10
num //= 10

for _ in range(10):   # max digits safety
    if num == 0:
        break

    curr = num % 10

    if curr >= prev:
        print("Unstable Number")
        break

    prev = curr
    num //= 10

else:
    print("Stable Number")


'''Next Prime Cabin Number Generator

A luxury hotel gives only prime numbered cabins to VIP guests.

Manager enters the last allotted cabin number.
System must find the next available prime cabin number.

Write a program using loops.

Input:
24

Output:
Next Prime Cabin = 29'''
num = int(input("Enter last cabin number = "))
n = num + 1

while True:
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    if count == 2:   # prime number condition
        print("Next Prime Cabin =", n)
        break

    n += 1

'''7.Alternate Digit Prime Checker

A math lab adds alternate digits from right side.

Write a program to:

- Find sum of alternate digits
- Check whether sum is Prime or Not

Input:
12345

Output:
Alternate Sum = 9
Not Prime'''
num = int(input("Enter Number = "))

temp = num
alt_sum = 0
count = 0


while temp > 0:
    d = temp % 10
    if count % 2 == 0:
        alt_sum += d
    count += 1
    temp //= 10

print("Alternate Sum =", alt_sum)

# Check prime
if alt_sum < 2:
    print("Not Prime")
else:
    factors = 0
    for i in range(1, alt_sum + 1):
        if alt_sum % i == 0:
            factors += 1

    if factors == 2:
        print("Prime")
    else:
        print("Not Prime")

'''8.ATM Note Counter

A bank ATM dispenses ₹100 notes.

Write a program to:

- Read withdrawal amount
- Count how many ₹100 notes needed using loop

Input:
700

Output:
Notes = 7'''
amount = int(input("Enter withdrawal amount = "))

notes = 0

while amount >= 100:
    amount -= 100
    notes += 1

print("Notes =", notes)


'''9.Bike Service Kilometer Checker

A bike needs service every 3000 km.

Write a program to:

- Read travelled kilometers
- Print every service checkpoint till entered km

Input:
10000

Output:
3000 6000 9000'''
km = int(input("Enter travelled kilometers = "))

i = 3000

while i <= km:
    print(i, end=" ")
    i += 3000

'''10.Lift Mode Operation – Advanced Smart Elevator System

A smart building elevator works in multiple intelligent modes based on the mode number entered by the control panel.  
The system must automatically execute floor movement instructions using loops.

Write a program:

- If mode = 1  
  Normal Up Mode activated.  
  Read current floor and destination floor.  
  Print all floors from current to destination in ascending order.

- Else if mode = 2  
  Down Mode activated.  
  Read current floor and destination floor.  
  Print all floors from current to destination in descending order.

- Else if mode = 3  
  Energy Saving Mode activated.  
  Read destination floor.  
  Lift starts from ground floor (0) and stops only on alternate floors till destination.

- Else  
  Emergency Mode activated.  
  Print "Emergency Alarm" 4 times using loop.

Input:
3
6

Output:
0 2 4 6


Input:
1
2
7

Output:
2 3 4 5 6 7


Input:
2
8
3

Output:
8 7 6 5 4 3


Input:
5

Output:
Emergency Alarm
Emergency Alarm
Emergency Alarm
Emergency Alarm'''
mode = int(input("Enter mode = "))

if mode == 1:
    print("Normal Up Mode activated")
    curr = int(input("Enter current floor = "))
    dest = int(input("Enter destination floor = "))

    for i in range(curr, dest + 1):
        print(i, end=" ")

elif mode == 2:
    print("Down Mode activated")
    curr = int(input("Enter current floor = "))
    dest = int(input("Enter destination floor = "))

    for i in range(curr, dest - 1, -1):
        print(i, end=" ")

elif mode == 3:
    print("Energy Saving Mode activated")
    dest = int(input("Enter destination floor = "))

    for i in range(0, dest + 1, 2):
        print(i, end=" ")

else:
    print("Emergency Mode activated")

    for i in range(4):
        print("Emergency Alarm")