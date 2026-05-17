n=int(input())
i=1
while i<=n:
    print()
    s=1
    while s<=(n-i):
        print(" ",end="")
        s=s+1
    j=1
    ch=65
    while j<=i:
        print(chr(ch),end="")

        ch=ch+1
        j=j+1
    i=i+1