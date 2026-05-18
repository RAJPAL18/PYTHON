'''1.
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username
'''

s = input("Enter Username = ")
n=len(s)
x=0


for ch in s:
    if ch==" ":
        x=0
        break

    else:
        if s[0]>="a" and s[0]<="z" or s[0]>="A" and s[0]<="Z":

            if ch>="a" and ch<="z" or ch>="A" and ch<="Z" or ch>="0" and ch<="9" or ch=="_":
                if ch!=" ":
                    if n>=5 and n<=12:
                        x=1
                    else:
                        x=0
                        break
   
if x==1:
    print("Valid Username")
else:
    print("Not Valid Username")
    
