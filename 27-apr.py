'''1. Product of Odd Numbers up to N

A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.

Input:
5

Output:
15'''

num = int(input("Enter number = "))

res=1
for i in range(1,num+1):
    if i%2!=0:
        res=res*i

print(res)


'''2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4'''

a,b=map(int,input("Enter the range of number = ").split(" "))
count=0
for i in range(a,b+1):
    if i%7==0:
        count+=1

print(count)


'''3. Display Numbers Ending with 5

A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.

Input:
10 40

Output:
15 25 35'''

a,b=map(int,input("Enter the range of number = ").split(" "))
for i in range(a+1,b):
    if i%5==0:
        if i%10!=0:
            print(i,end=" ")

'''4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145


Output:
Strong Number'''

num = int(input("Enter the number = "))
temp =num
sum=0
while num>0:
    rem=num%10
    num=num//10
    fact=1
    for i in range(1,rem+1):
        fact=fact*i
    sum=sum+fact
if sum==temp:
    print("Strong Number")
else:
    print("Not Strong Number")
    
    
'''5. Harshad Number Checker

A number scanner is installed in a research laboratory where thousands of numeric access codes are tested every day. To identify mathematically balanced codes, the system checks whether the entered number qualifies as a Harshad number. Numbers passing this test are considered valid for the next stage of processing.

A Harshad number is a number that is exactly divisible by the sum of its digits.

Example:
18 → 1 + 8 = 9 and 18 ÷ 9 = 2

Write a program using loops to check whether the entered number is a Harshad number.

Input:
18

Output:
Harshad Number'''

num = int(input("Enter number = "))
temp =num
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10
if num%sum==0:
    print("Harshad Number")
else:
    print("Not Harshad Number")


'''6.'''
n = int(input())

square = n * n

temp_n = n
temp_sq = square

flag = 1

while temp_n > 0:
    if temp_n % 10 != temp_sq % 10:
        flag = 0
    temp_n = temp_n // 10
    temp_sq = temp_sq // 10

if flag == 1:
    print("Automorphic Number")
else:
    print("Not Automorphic Number")

'''7.'''
n = int(input())

temp = n
flag = 0

while temp > 0:
    digit = temp % 10
    if digit == 0:
        flag = 1
    temp = temp // 10

if flag == 1:
    print("Duck Number")
else:
    print("Not Duck Number")


'''8.
Mirror Difference Transaction Verification System
A multinational banking company processes thousands of daily transaction IDs. To detect suspicious patterns and validate system-generated IDs,
 the security software performs a Mirror Difference Verification Test.
For every entered transaction ID:

Reverse the digits of the transaction ID

Find the absolute difference between the original ID and the reversed ID


Count the total number of digits in the difference


Apply the following conditions using if-elif-else:

If the difference is 0, print Perfect Match


Else if the difference is divisible by 9, print Verified


Else print Rejected


Write a program to automate this verification process using loops and conditional statements.
Input:
4215
Output:
Reverse = 5124Difference = 909Digits = 3Verified
Input:
1221
Output:
Reverse = 1221Difference = 0Digits = 1Perfect Match
Input:
1234
Output:
Reverse = 4321Difference = 3087Digits = 4Verified

'''


num = int(input("Enter the  Number = "))
temp = num
rev=0
for i  in range(len(str(num)),0,-1):
	rem=num%10
	rev=rev*10+rem
	num=num//10

dif = temp-rev
if dif<0:
	dif=-(dif)
else:
	dif=dif


ldif = len(str(dif))

if dif==0:
	print("Reverse =",rev)
	print("Difference ",dif)
	print("Digits = ",ldif)
	print("Perfect Match")

elif dif%9==0:
	print("Reverse =",rev)
	print("Difference ",dif)
	print("Digits = ",ldif)
	print("Verified")
else:
	print("Reverse =",rev)
	print("Difference ",dif)
	print("Digits = ",ldif)
	print("Reject")
	
'''9.
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number'''

num = int(input("Enter Number = "))
temp=num
dif=0
rev=0
for i in range(len(str(num)),0,-1):
	rem=num%10
	rev=rev*10+rem
	num=num//10

sum=0
big=0

print("Step Differences: ",end=" ")
while rev>10:
	rem1=rev%10
	rev=rev//10
	rem2=rev%10
	
	dif = abs(rem1-rem2)
	sum=sum+dif
	if dif>big:
		big=dif
	print(dif,end=" ")

t = len(str(temp))

if sum%t==0:
	print("Balance")
else:
	print("Unbalance")
print(sum)
print(big)