n=int(input("enter number =  "))
num=1
i=1
while i<=n:
    print()
    print(" "*(n-i) , end="")
    j=1
    while j<=i:
        print(num,end=" ")
        num+=1
        j+=1
    i+=1
        