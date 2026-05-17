'''1. Adjacent Digit Difference Analyzer

A system analyzes differences between consecutive digits in a number.

Write a program to:

Find the difference between every pair of adjacent digits
Display all differences
Count how many differences are even
Find the largest difference
If all differences are same → print Uniform Difference
Else → print Non-Uniform Pattern

Input:
84261

Output:
Differences: 4 2 4 5
Even Differences Count = 3
Max Difference = 5
Non-Uniform Pattern

'''


num = int(input("Enter number: "))

temp = num
rev = 0

# Reverse number
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

prev = rev % 10
rev = rev // 10

even_count = 0
max_diff = 0
same = 1
first_diff = -1

print("Differences:", end=" ")

while rev > 0:

    curr = rev % 10

    diff = prev - curr

    if diff < 0:
        diff = -diff

    print(diff, end=" ")

    if diff % 2 == 0:
        even_count += 1

    if diff > max_diff:
        max_diff = diff

    if first_diff == -1:
        first_diff = diff
    elif first_diff != diff:
        same = 0

    prev = curr
    rev = rev // 10

print()
print("Even Differences Count =", even_count)
print("Max Difference =", max_diff)

if same == 1:
    print("Uniform Difference")
else:
    print("Non-Uniform Pattern")




'''

2. Digit Sum Mirror Checker

A validation system checks symmetry in digit sums.

Write a program to:

Split number into two halves
Find sum of first half digits
Find sum of second half digits
Display both sums
If both sums are equal → print Balanced Number
Else → print Unbalanced Number

Input:
123321

Output:
First Half Sum = 6
Second Half Sum = 6
Balanced Number
'''
num = int(input("Enter number: "))

temp = num
digits = 0

# Count digits
while temp > 0:
    digits += 1
    temp = temp // 10

half = digits // 2

temp = num
power = 1
i = 0

# Find divisor
while i < half:
    power = power * 10
    i += 1

second = temp % power
first = temp // power

sum1 = 0
sum2 = 0

while first > 0:
    sum1 += first % 10
    first = first // 10

while second > 0:
    sum2 += second % 10
    second = second // 10

print("First Half Sum =", sum1)
print("Second Half Sum =", sum2)

if sum1 == sum2:
    print("Balanced Number")
else:
    print("Unbalanced Number")

'''
3.
Digit Neighbor Sum Analyzer

A system analyzes the relationship between a digit and its immediate neighbors.

Write a program to:

Traverse digits from left to right (ignore first and last digit)
For each digit, calculate sum of its adjacent digits
Check if current digit is equal to the sum of its neighbors
Display such digits
Count how many such digits exist
If none found → print No Matching Digit
Else → print Neighbor Sum Pattern Found

Input:
121314

Output:
Matching Digits: 2 3
Count = 2
Neighbor Sum Pattern Found

'''
num = int(input("Enter number: "))

temp = num
rev = 0

# Reverse number
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

a = rev % 10
rev = rev // 10

b = rev % 10
rev = rev // 10

count = 0

print("Matching Digits:", end=" ")

while rev > 0:

    c = rev % 10

    if b == (a + c):
        print(b, end=" ")
        count += 1

    a = b
    b = c

    rev = rev // 10

print()
print("Count =", count)

if count == 0:
    print("No Matching Digit")
else:
    print("Neighbor Sum Pattern Found")

'''
4.Digit Gap Analyzer

A system analyzes the gap between consecutive digits.

Write a program to:

Traverse digits from left to right
Find the absolute difference between current digit and next digit
Display each difference
Count how many differences are greater than 2
Find the maximum difference
If all differences ≤ 2 → print Smooth Number
Else → print Irregular Pattern

Input:
86421

Output:
Differences: 2 2 2 1
Count (>2) = 0
Max Difference = 2
Smooth Number

'''
num = int(input("Enter number: "))

temp = num
rev = 0

# Reverse number
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

prev = rev % 10
rev = rev // 10

count = 0
max_diff = 0

print("Differences:", end=" ")

while rev > 0:

    curr = rev % 10

    diff = prev - curr

    if diff < 0:
        diff = -diff

    print(diff, end=" ")

    if diff > 2:
        count += 1

    if diff > max_diff:
        max_diff = diff

    prev = curr
    rev = rev // 10

print()
print("Count (>2) =", count)
print("Max Difference =", max_diff)

if count == 0:
    print("Smooth Number")
else:
    print("Irregular Pattern")
'''

5.
Tech Number Checker

A number is called a Tech Number if:

It has even number of digits
Split it into two equal halves
Add both halves
Square the sum
If result equals original number → Tech Number

Write a program to:

Count digits
If digits are even, split the number
Find sum of both halves
Square the sum
Display intermediate values
Check and print result

Input:
2025

Output:
First Half = 20
Second Half = 25
Sum = 45
Square = 2025
Tech Number'''

num = int(input("Enter number: "))

temp = num
digits = 0

# Count digits
while temp > 0:
    digits += 1
    temp = temp // 10

if digits % 2 == 0:

    half = digits // 2

    power = 1
    i = 0

    # Find divisor
    while i < half:
        power = power * 10
        i += 1

    second = num % power
    first = num // power

    sum_num = first + second
    square = sum_num * sum_num

    print("First Half =", first)
    print("Second Half =", second)
    print("Sum =", sum_num)
    print("Square =", square)

    if square == num:
        print("Tech Number")
    else:
        print("Not Tech Number")

else:
    print("Not Tech Number")