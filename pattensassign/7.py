'''
    *
    **
   *
  **
 ***
**'''

n= int(input("Enter the number = "))
i=1
while i<=n:
    print()
    s=1
    while s<=(n-i):
        print(" ",end="")
        s=s+1
    dn=1
    while dn<=i:
        print("*",end="")
        dn=dn+1
    i=i+1
