'''WAP to find out all the leap years between two entered years'''

a = int(input("Enter the first year = "))
b = int(input("Enter the second year = "))
i=a
while i<=b:
    if i%100==0:
        if i%400==0:
            print(i)
    else:
        if i%4==0:
            print(i)
    i+=1
