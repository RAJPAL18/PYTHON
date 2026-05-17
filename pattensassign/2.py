'''WAP to print Square, Cube and Square Root of all numbers from 1 to N'''
import math
n = int(input("Enter the number = "))
i=1
while i<=n:
    print(i,"Square = ",i*i,"Cube = ", i**3," Square Root = ", math.sqrt(i) )
    i+=1
    