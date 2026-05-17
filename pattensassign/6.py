'''
a
ab
abc
abcd
abcde'''
n=int(input("Enter the number = "))
i=1

while i<=n:
    print()
    j=1
    a=97
    while j<=i:
        print(chr(a),end="")
        a=a+1
        j=j+1
    i=i+1