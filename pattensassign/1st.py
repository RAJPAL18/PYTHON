a= int(input("Enter the first number"))
b= int(input("ENter the second number = "))
i = a
sum=0
while i<=b:
    if i%9==0:
        sum+=i
    i+=1
print(sum)
