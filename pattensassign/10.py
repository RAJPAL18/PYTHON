'''10.
enter number6
0
0 1
0 1 2
0 1 2 3
0 1 2 3 4'''
n=int(input("input:"))
i=1
while i<=n-1:
    print()
    for j in range(0,i):
        print(j,end=" ")
    i=i+1