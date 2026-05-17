'''8.
enter n6
 654321
  65432
   6543
    654
     65
'''
n=int(input("input:"))
i=1
while i<=n-1:
    print()
    k=i
    for spc in range(0,k,1):
        print(" ",end="")
    for j in range(n,i-1,-1):
        print(j,end="")
    i=i+1