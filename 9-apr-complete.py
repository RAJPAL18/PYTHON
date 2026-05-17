''' 1. Hello & Name Printer
Write a program to print:
Hello
Your Name'''

print("Hello")
print("My name is Rajpal Rajput")

print("--------------------END 1--------------------------")


# 2. PROGRAM TO DISPLAY MENU

print("====== Welcome To Coffee shop ======")
print("1.Espresso \t $3 \n2.Latte \t $5\n3.Cappuccino \t $5")
print("====================================")


print("--------------------END 2--------------------------")

# Display Resume

print("======Resume======")
print("Name : Alice Johson \nEmail : alice@example.com\nSkils:\n\tJava \n\tHTML & CSS \n\tProblem Solving\nExperience:2 years at XYZ ltd ")

print("--------------------END 3--------------------------")

#print Star pattern

print("******")
print("******")
print("******")

print("--------------------END 4--------------------------")

# Print Special Characters

print("@","#","$","%","^","&","*")

print("--------------------END 5--------------------------")

'''6. Print User Details
Take input:
- Name
- Age
- City
Display them properly.'''

name = input("Enter the name : ")
age= int(input("Enter the age :"))
city = input("Enter the city :")
print(f"My name is {name},\nMy age is {age},\nI live in {city}")

print("--------------------END 6--------------------------")

'''7. Full Name Display
Take first name and last name as input and display:
Full Name: John Doe
'''
first = input("Enter your first name :")
last = input("Enter your last name :")
print("Full namr is {} {}".format(first,last))

print("--------------------END 7--------------------------")

'''8. Simple Input Display
Take two numbers as input and print them on separate lines.
'''
num1,num2 = (input("enter the number :").split())
print(num1)
print(num2)

print("--------------------END 8--------------------------")

'''9. Three Inputs Display
Take three values from user and print each on new line.'''

x,y,z =(input("enetr the values").split())
print(x)
print(y)
print(z)


print("--------------------END 9--------------------------")

'''10. Input and Echo
Take input from user and print:
You entered: <input>'''

a = input("Enter the input ")
print("you have entered",a)

print("--------------------END 10--------------------------")

'''11. Greeting Message
Take name as input and print:
Hello <name>
Welcome to Python
'''

name1=input("Enter the name")
print(f"Hello {name1} \nWelcome to Python")

print("--------------------END 11--------------------------")

'''12. Favorite Things
Take input:
- Favorite food
- Favorite color
Display:
I like <food> and my favorite color is <color>'''

favfood = input("Enter your Favorite food :")
favcolor = input("Enter your Favorite color :")
print(f"I like {favfood} and my favorite color is {favcolor}")

print("--------------------END 12--------------------------")


'''13. College Details
Take input:
- College Name
- Course
- Year
Display in proper format.
'''
clgname=input("enter your college name :")
cour = input("enter your course name :")
year = input("enter your year :")

print(f"My college name is {clgname},\nI am pursuing {cour},\nI am in {year} year")

print("--------------------END 13--------------------------")

'''14. Email Display
Take email as input and print:
Your email is: <email>'''

email = input("Enter your email address")
print(f"Your email is {email}")

print("--------------------END 14--------------------------")

'''15. Bio Data
Take input:
- Name
- Age
- Phone
Display:
--- Bio Data ---
Name  :
Age   :
Phone :'''


Name=input("Enter your name :")
Age = input("Enter your age :")
Phone = input("Enter your number")

print("---------Bio Data---------")
print(f"Name :\t{Name}\nAge :\t{Age}\nPhone :\t{Phone}")

print("--------------------END 15--------------------------")
