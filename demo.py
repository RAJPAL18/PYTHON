a = int(input("Enter the starting number = "))
b= int(input("Enter the ending number = "))


for i in range(a,b+1):
    temp=i
    su=0
    p=len(str(i))
    while temp>0:
        d = temp%10
        su = su+d**p
        temp=temp//10
        
    if i==su:
        print(i)