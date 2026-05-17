'''1. Sum of First N Natural Numbers

A teacher wants to reward students by giving points daily. On day 1, a student gets 1 point, day 2 → 2 points, and so on. This follows a natural number sequence.
Write a program to calculate the total points earned after n days by summing all natural numbers up to n using loops.

Input: n = 10
Output: Total Points = 55'''
n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Total Points =", total)

'''2.Factorial of a Number

In project scheduling, tasks are dependent on previous tasks, and the total number of ways to arrange them is calculated using factorial. Factorial of a number n is the product of all numbers from 1 to n.
Write a program to calculate the factorial of a given number using loops.

Input: n = 5
Output: Total Ways = 120'''
n = int(input("Enter n: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Total Ways =", fact)

'''3. Multiplication Table

A shopkeeper wants to calculate bulk pricing for a product. If one item costs ₹n, then cost for multiple quantities can be calculated using multiplication.
Write a program to print the multiplication table of a given number up to 10 using loops.

Input: n = 6'''
n = int(input("Enter number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

'''4. Reverse a Number

A security system stores OTP codes in reverse format for encryption to increase data safety. Reversing a number means extracting digits and rebuilding it in reverse order.
Write a program to reverse a given integer using loops.

Input: 1234
Output: 4321'''
num = int(input("Enter number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed =", rev)

'''5. Palindrome Check

A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
Write a program to check whether a given number is a palindrome using loops.

Input: 121
Output: Palindrome'''
num = int(input("Enter number: "))
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


'''
6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

Input: 153
Output: Armstrong
'''
num1 = int(input("Enter number: "))
temp = num1
sum=0

while num1>0:
    rem=num1%10
    sum=sum+rem**3
    num1=num1//10
if sum==temp:
    print("Armstrong")
else:
    print("Not Armstrong")


'''7. Count Even Digits

A data analyst is analyzing numeric IDs and needs to determine how many digits in the ID are even.
Write a program to count the number of even digits in a given number using loops.

Input: 123456
Output: Even digits count = 3'''
num = int(input("Enter number: "))
count = 0

while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        count += 1
    num //= 10

print("Even digits count =", count)

'''8.Count Odd Digits

A banking system flags IDs with too many odd digits for further verification.
Write a program to count the number of odd digits in a given number using loops.

Input: 123456
Output: Odd digits count = 3'''
num = int(input("Enter number: "))
count = 0

while num > 0:
    digit = num % 10
    if digit % 2 != 0:
        count += 1
    num //= 10

print("Odd digits count =", count)



'''*10. Even Numbers Between Two Numbers*
A teacher wants to assign only even roll numbers for a special activity. The system should display all even numbers between two given numbers.
Write a program to *display all even numbers between two numbers using loops*.

Input: 10, 20
Output: 10 12 14 16 18 20'''

m,n = map(int,input("Enter two numver to get even numbers between them = ").split(","))
for i in range(m,n+1,2):
    print(i,end=" ")

'''*11. Count Occurrence of a Digit*
A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to *count how many times a given digit appears in a number using loops*.

Input: Number = 122312, Digit = 2
Output: 3'''

n= int(input("Enter number = "))
d= (input("Enter digit ="))
count=0

for i in str(n):
    if i==d:
        count+=1

print("The number",n,"has occurance of",d,"=",count)


'''*12. Multiplication of Digits*
A puzzle game calculates a score by multiplying all digits of a number together. After calculating the score, the game also checks whether the final score is even or odd to assign a bonus.
Write a program to *find the product of all digits of a number using loops and then check whether the result is even or odd*.

Input: 1234
Output: 24
Even  '''

n = int(input("Enter n: "))
fact = 1

for i in str(n):
    fact *= int(i)


print(fact)
if fact%2==0:
    print("Even")
else:
    print("Odd")

'''*13. Number Range Display System (if-elif with loops)*
A number analysis tool processes two input values and displays numbers between them based on their relationship.

* If the first number is less than the second, display numbers in ascending order
* If the first number is greater than the second, display numbers in descending order
* If both numbers are equal, display "Both numbers are same"

Write a program using *if-elif-else and loops* to implement this logic.

Input: 5, 10
Output: 5 6 7 8 9 10

Input: 10, 5
Output: 10 9 8 7 6 5

Input: 7, 7
Output: Both numbers are same'''

m,n= map(int,input("ENter Number Range = ").split(","))

if m<n:
    for i in range(m,n+1):
        print(i,end=" ")
elif m>n:
    for i in range(m,n-1,-1):
        print(i,end=" ")
else:
    print("Both numbers are same")

'''14.Floor Movement System (Elevator)
An elevator system takes the current floor and destination floor as input.

If current floor < destination → move upward and display floors
If current floor > destination → move downward and display floors
If both are same → display "Already on the same floor"

Write a program using if-elif-else and loops to simulate elevator movement.

Input: 1, 5
Output: 1 → 2 → 3 → 4 → 5

Input: 7, 3
Output: 7 → 6 → 5 → 4 → 3

Input: 4, 4
Output: Already on the same floor'''

m,n= map(int,input("ENter current floor & destination floor = ").split(","))

if m<n:
    for i in range(m,n+1):
        print(i,end="→")
elif m>n:
    for i in range(m,n-1,-1):
        print(i,end="→")
else:
    print("Already on the same floor")









# PYTHON LOOP CONVERSION PROGRAMS

'''1. SUM OF FIRST N NATURAL NUMBERS
Theory:
Natural numbers are 1,2,3,4...
We add all numbers from 1 to n

Example:
Input:
5

Output:
Total Points = 15'''


n = int(input("Enter n: "))
total = 0


# for i in range(1, n+1):
#     total += i


i = 1
while i <= n:
    total += i
    i += 1

print("Total Points =", total)



'''
2. FACTORIAL OF A NUMBER
Theory:
Factorial means multiplication from 1 to n
Example:
5! = 5×4×3×2×1 = 120

Input:
5

Output:
Total Ways = 120'''


n = int(input("Enter n: "))
fact = 1


# for i in range(1, n+1):
#     fact *= i


i = 1
while i <= n:
    fact *= i
    i += 1

print("Total Ways =", fact)



'''
3. MULTIPLICATION TABLE
Theory:
Print multiplication table from 1 to 10

Input:
6

Output:
6 x 1 = 6
...
6 x 10 = 60'''

n = int(input("Enter number: "))


# for i in range(1,11):
#     print(n,"x",i,"=",n*i)


i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1



'''
4. REVERSE A NUMBER
Theory:
Extract last digit and create reverse

Input:
1234

Output:
Reversed = 4321'''

num = int(input("Enter number: "))
rev = 0

temp = num
count = 0

while temp > 0:
    count += 1
    temp = temp // 10


# while num > 0:
#     digit = num % 10
#     rev = rev*10 + digit
#     num = num//10


for i in range(count):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed =", rev)



'''
5. PALINDROME NUMBER
Theory:
If number and reverse are same → Palindrome

Input:
121

Output:
Palindrome'''

num = int(input("Enter number: "))
temp = num
rev = 0

x = num
count = 0

while x > 0:
    count += 1
    x = x // 10


# while num > 0:
#     digit = num % 10
#     rev = rev*10 + digit
#     num = num//10


for i in range(count):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")



'''
6. ARMSTRONG NUMBER
Theory:
Sum of cube of digits = original number

Example:
153 = 1³ + 5³ + 3³

Input:
153

Output:
Armstrong
'''
num = int(input("Enter number: "))
temp = num
sum = 0

x = num
count = 0

while x > 0:
    count += 1
    x = x // 10


# while num > 0:
#     rem = num % 10
#     sum += rem**3
#     num = num//10


for i in range(count):
    rem = num % 10
    sum += rem ** 3
    num = num // 10

if sum == temp:
    print("Armstrong")
else:
    print("Not Armstrong")



'''
7. COUNT EVEN DIGITS
Theory:
Count digits divisible by 2

Input:
123456

Output:
Even digits count = 3

'''
num = int(input("Enter number: "))
count = 0

x = num
digits = 0

while x > 0:
    digits += 1
    x = x // 10


# while num > 0:
#     digit = num % 10
#     if digit % 2 == 0:
#         count += 1
#     num = num//10


for i in range(digits):

    digit = num % 10

    if digit % 2 == 0:
        count += 1

    num = num // 10

print("Even digits count =", count)


'''

8. COUNT ODD DIGITS
Theory:
Count digits not divisible by 2

Input:
123456

Output:
Odd digits count = 3
'''

num = int(input("Enter number: "))
count = 0

x = num
digits = 0

while x > 0:
    digits += 1
    x = x // 10


# while num > 0:
#     digit = num % 10
#     if digit % 2 != 0:
#         count += 1
#     num = num//10


for i in range(digits):

    digit = num % 10

    if digit % 2 != 0:
        count += 1

    num = num // 10

print("Odd digits count =", count)



'''
9. EVEN NUMBERS BETWEEN TWO NUMBERS
Theory:
Print all even numbers between two values

Input:
10,20

Output:
10 12 14 16 18 20'''

m, n = map(int, input("Enter range = ").split(","))
# for i in range(m, n+1, 2):
#     print(i,end=" ")


i = m

while i <= n:
    print(i, end=" ")
    i += 2

print()




'''10. NUMBER RANGE DISPLAY
Theory:
If first number smaller → ascending
If greater → descending

Input:
5,10

Output:
5 6 7 8 9 10'''

m, n = map(int, input("Enter range = ").split(","))

if m < n:

  
    # for i in range(m,n+1):
    #     print(i,end=" ")

    i = m
    while i <= n:
        print(i, end=" ")
        i += 1

elif m > n:

    
    # for i in range(m,n-1,-1):
    #     print(i,end=" ")

    i = m
    while i >= n:
        print(i, end=" ")
        i -= 1

else:
    print("Both numbers are same")

print()




'''11. ELEVATOR SYSTEM
 Theory:
If current floor smaller → move up
If bigger → move down

 Input:
 1,5

Output:
 1→2→3→4→5'''


m, n = map(int, input("Enter floors = ").split(","))

if m < n:

    
    # for i in range(m,n+1):
    #     print(i,end="→")

    i = m
    while i <= n:
        print(i, end="→")
        i += 1

elif m > n:

    
    # for i in range(m,n-1,-1):
    #     print(i,end="→")

    i = m
    while i >= n:
        print(i, end="→")
        i -= 1

else:
    print("Already on same floor")