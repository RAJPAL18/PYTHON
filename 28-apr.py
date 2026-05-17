'''1. Prime Security Code Checker

A high-security research lab uses numeric passcodes to unlock restricted doors. To improve security,
 only prime numbers are accepted because they have exactly two factors and are harder to predict using common patterns.

When an employee enters a code, the system must verify whether the number is prime. If yes, access is granted; otherwise, access is denied.

Write a program to check whether the entered number is Prime or Not Prime.

Input:
29

Output:
Prime Number
'''
import math
num = int(input("Enter Number = "))
x=0
if num<=1:
    print("Not Prime")
else:
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            x=1
            break
if x==1:
    print("Not Prime Number")
else:
    print("Prime Number")


'''2. Next Prime ID Generator

A multinational company auto-generates employee IDs in numeric sequence.
 Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17'''
num = int(input("Enter Number = "))
n = num + 1

while True:
    x = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            x += 1
    
    if x == 2:
        print("Next Prime =", n)
        break
    
    n += 1

'''3. Composite Number Detector

A product testing company labels batch numbers as risky if they have more than two factors. Such numbers are known as composite numbers and indicate repeated grouping patterns.

The quality control officer enters a batch number, and the software checks whether it is Composite or Not.

Write a program to check whether a number is Composite or Not.

Input:
12

Output:
Composite Number'''
n = int(input("Enter number = "))

if n <= 1:
    print("Neither Prime nor Composite")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Composite Number")
            break
    else:
        print("Not Composite (Prime Number)")


'''4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31
'''

import math
num = int(input("Enter Number = "))
x=0
if num<=1:
    print("Not Prime")
else:
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            x=1
            break
if x==1:
    print("Not Prime Number")
    n = num - 1

    while n>1:
        y = 0
    
        for i in range(1,n+1):
            if n % i == 0:

                y += 1
    
        if y == 2:
            print("previous Prime =", n)
            break
    
        n -= 1
else:
    print("Prime Number")
    n = num + 1

    while True:
        y = 0
    
        for i in range(1, n + 1):
            if n % i == 0:

                y += 1
    
        if y == 2:
            print("Next Prime =", n)
            break
    
        n += 1


'''5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3'''

num = int(input("Enter Number = "))
n = num + 1

while True:
    x = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            x += 1
    
    if x == 2:
        print("Next Prime ID =", n)
        gap = n- num
        print("Gap = ",gap)
        break
    
    n += 1


'''6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2'''


n = int(input("Enter number = "))

fact = 0
small = 0

for i in range(1, n + 1):
    if n % i == 0:
        fact += 1
        
        if i > 1 and small == 0:
            small = i  
            
if n <= 1:
    print("Neither Prime nor Composite")
elif fact > 2:
    print("Composite Number")
else:
    print("Not Composite (Prime Number)")

print("Total Factors =", fact)

print("Smallest factor other than 1 =", small)

'''.
 Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number'''

num = int(input("Enter number = "))
sum=0
x=0
while num>0:
	rem=num%10
	sum+=rem
	num=num//10
print("Sum",sum)
for i in range(2,sum//2):
	if sum%i==0:
		x=1
		break
if x==0:
	print("Lucky Number")
else:
	print("Normal Number")
'''8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime'''


num = int(input("Enter number = "))
sum=0
x=0
lar=0
sml=9
while num>0:
	rem=num%10
	if rem>lar:
		lar = rem
	if rem<sml:
		sml=rem
			
	
	num=num//10
print("Largest =",lar)
print("Smallest =" ,sml)
sum=lar+sml
print("Sum =",sum)
for i in range(2,sum//2):
	if sum%i==0:
		x=1
		break
if x==0:
	print("Prime Number")
else:
	print("Composite Number")
     

'''Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime'''

num = int(input("Enter number = "))
x,y=0,0
while num>0:
    rem = num%10
    if rem%2==0:
        x+=1
    else:
        y+=1
    num=num//10
dif=abs(x-y)
print("Even count = ",x)
print("Odd count = ",y)
print("Difference = ",dif)

if dif <= 1:
    print("Not Prime")
else:
    count = 0
    for i in range(1, dif + 1):
        if dif % i == 0:
            count += 1

    if count == 2:
        print("Prime")
    else:
        print("Not Prime")


