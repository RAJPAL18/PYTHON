'''9.
    1
   10
  101
 1010
10101
'''
n=int(input("input"))
i=1
while i<=n:
    print()
    k=n
    l=i
    for j in range(k,l,-1):
        print(" ",end="")
    for m  in range(1,i+1,1):
        if m%2==0:
            print("0",end="")
        else:
            print("1",end="")
    i=i+1