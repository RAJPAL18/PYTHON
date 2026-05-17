n=int(input())
i=1
while i<=n:
    print()
    s=1
    while s<=(n-i):
        print(" ",end="")
        s=s+1
    j=i
    while j>=1:
        print(j,end="")
        j=j-1
    i=i+1