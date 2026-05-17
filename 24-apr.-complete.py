'''1.'''

n = int(input("Enter number: "))
mx = "0"
for i in str(n):
    if i>ma:
        ma=i

print(mx)

'''2.'''


n = int(input("Enter number: "))
mn= "9"
for i in str(n):
    if i<mn:
        mn=i

print(mn)

'''3.'''
num = int(input("Enter a number: "))

while num >= 10:
    num = num // 10

print("First digit = ", num)

'''4.'''



m,n = map(int,input("Enter two numver to get mutliple of 3 between them = ").split(","))
for i in range(m,n+1):
    if i%3==0:
        print(i,end=" ")

'''5.'''
num = int(input("Enter a number: "))
count=0

for i in range(1, num + 1):
    if num % i == 0:
        count+=1
print(count)

'''6.'''
num = int(input("Enter a number: "))
sum=0

for i in range(1, num + 1):
    if num % i == 0:
        sum+=i
print(sum)

'''7. Power of a Number A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power. Write a program to calculate n raised to power p using loops. Input: 2 5 Output: 32'''
n, p = map(int, input("Enter number and power: ").split())
result = 1

for i in range(p):
    result = result * n

print(result)

'''8. Count Multiples of 5 Between Two Numbers A supermarket gives coupons to customers whose token numbers are multiples of 5. The manager enters a token range and wants to know how many eligible token numbers exist. Write a program to count numbers divisible by 5 between two given numbers using loops. Input: 1 20 Output: Count = 4'''
a, b = map(int, input("Enter range: ").split())
count = 0

for i in range(a, b + 1):
    if i % 5 == 0:
        count += 1

print("Count =", count)

'''9. Neon Number LED Unlock Game You're programming a new LED display game. The game level unlocks only when a neon number is entered. A neon number is a number where the sum of the digits of its square is equal to the number itself. Example: 9 → 9² = 81 → 8 + 1 = 9 Accept a number from the player. Check whether it is a neon number using loops. If true, display: Glowing Success! You've found the Neon Number! Otherwise display: Try again! Not quite glowing yet. Input: 9
Output: Glowing Success! You've found the Neon Number! '''

n = int(input("Enter number: "))
square = n * n
sum_digits = 0

while square > 0:
    digit = square % 10
    sum_digits += digit
    square = square // 10

if sum_digits == n:
    print("Glowing Success! You've found the Neon Number!")
else:
    print("Try again! Not quite glowing yet.")

'''10. Student ID Validity Checker (Count Odd Digits) A school management system assigns numeric IDs to students. The administration wants to verify IDs by checking how many odd digits are present in each ID number. IDs with more odd digits are sent for manual review. Write a program to count the number of odd digits in a given student ID using loops. Input: 572943 Output: Odd Digits Count = 3'''

n = int(input("Enter number: "))
count = 0

while n > 0:
    digit = n % 10
    if digit % 2 != 0:
        count += 1
    n = n // 10

print("Odd Digits Count =", count)