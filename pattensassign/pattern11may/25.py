n  = int(input("Enter the number = "))
i=n
while i >=1:
    print()
    s=1
    while s<=(n-i):
        print(" ",end="")
        s +=1
    
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    k=i-1
    while k>=1:
        print(k,end="")
        k=k-1
    i-=1
i=2
while i<=n:
    print()
    s=1
    while s<=(n-i):
        print(" ",end="")
        s +=1
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    k=i-1
    while k>=1:
        print(k,end="")
        k=k-1
    i+=1