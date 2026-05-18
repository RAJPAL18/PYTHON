'''4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID'''
s=input("Enter Employee ID:")
l=len(s)
x=0

if l>=8:
    if s[0]=="E" and s[1]=="M" and s[2]=="P":
        for i in range(l):
            if s[3:]>="0" and s[3:]<="9":
                x=1
else:
    x=0
            
if x==1:
    print("Valid Username")
else:
    print("Not Valid Username")