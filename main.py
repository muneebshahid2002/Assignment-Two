# Write a program to check whether a person is eligible to vote or not?
voting_age = 18
age = int(input("Enter your age: "))

if age >= voting_age:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
    
# Write a program to check char is vowel or not.
char = input("Enter a character: ")

if char in 'aeiouAEIOU':
    print("Vowel")
else:
    print("Consonant")
 
        
# Write a program to check the number is positive or negative. User input.
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Write a program to check whether a number is odd or even?

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Write a program to display the grade of the user in subject A, ask user marks obtained out of 100
marks = int(input("Enter your marks in subject A (out of 100): "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Write a program to check whether a number is divisible by 7
number = int(input("Enter a number: "))

if number % 7 == 0:
    print(f"{number} is divisible by 7")
else:
    print(f"{number} is not divisible by 7")


# Write a program to check if year is leap year.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Write a program to ask user its name and check whether name consists of 5 or more letters

name = input("Enter your name: ")

if len(name) >= 5:
    print(f"{name} consists of 5 or more letters")
else:
    print(f"{name} consists of less than 5 letters")

# Write a program that accepts 3 inputs from user. input 1 and input 2 should be numbers and the third input should be mathematical operator. 
# Perform operation accordingly
# for example
# input1 is 5 and input2 is 10 and input3 is +
# then output should be 15
# input1 is 5 and input2 is 10 and input3 is *
# then output should be 50


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter mathematical operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Division by zero is not allowed")
    else:
        result = num1 / num2
else:
    print("Invalid operator")

if operator not in ("/", 0):  # Print result only for valid operations (excluding division by zero)
    print(f"Result: {result}")



# Write a program that accepts 1 input from user and check if the number is divisible by 2 and 3 both.
# for example
# input1 is 10
# output should be "10 is only divisible by 2"
# input1 is 9
# output should be "9 is only divisible by 3"
# input1 is 12
# output should be "12 is divisible by 2 and 3"


number = int(input("Enter a number: "))

divisibility_message = ""
if number % 2 == 0:
    divisibility_message += "divisible by 2"
if number % 3 == 0:
    if divisibility_message:
        divisibility_message += " and "
    divisibility_message += "divisible by 3"

if not divisibility_message:
    print(f"{number} is not divisible by 2 or 3")
else:
    print(f"{number} is {divisibility_message}")


# Write a program that accepts 2 inputs from user and check which number is largest.
# for example:
# input1 is 5 and input2 is 10
# output should be 10 as this number is larger than 5


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is larger")
elif num1 < num2:
    print(f"{num2} is larger")
else:
    print("Both numbers are equal")



# Write a program that accepts 3 input from user and check which number is largest.
# for example:
# input1 is 5 and input2 is 10 and input3 is 15
# output should be 15 as this number is larger than 5 and 10
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

largest = max(num1, num2, num3)
if largest == num1:
    print(f"{num1} is largest")
elif largest == num2:
    print(f"{num2} is largest")
else:
    print(f"{num3} is largest")



# Write a python program that accept user an input. The valid input should be of following
# - GREEN or gREEN or green etc 
# - RED or red or rEd etc 
# - YELLOW or yellow or yELlOw etc
# program should display the following message on checking above input
# Car is allowed to go
# Car has to wait
# Car has to stop
# invalid input


color = input("Enter a color (green, red, yellow): ")
color = color.lower()

if color in ("green", "red", "yellow"):
    if color == "green":
        print("Car is allowed to go")
    elif color == "red":
        print("Car has to stop")
    else:
        print("Car has to wait")
else:
    print("Invalid input")
    
    

#  Comparing Two Numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print("First number is greater")
elif num2 > num1:
    print("Second number is greater")
else:
    print("Both numbers are equal")


# Password Strength Checker

password = input("Enter your password: ")

if len(password) < 6:
    print("Weak password")
elif 6 <= len(password) <= 12:
    print("Moderate password")
else:
    print("Strong password")


#  Calculate Bonus

salary = float(input("Enter employee's salary: "))
years_of_service = int(input("Enter years of service: "))

if years_of_service < 5:
    print("No bonus")
elif 5 <= years_of_service <= 10:
    print("Bonus amount:", salary * 0.1)
else:
    print("Bonus amount:", salary * 0.2)


#  Apply Discount

purchase_amount = float(input("Enter total purchase amount: "))

if purchase_amount < 100:
    print("No discount")
elif 100 <= purchase_amount <= 500:
    print("Final amount after 10% discount:", purchase_amount * 0.9)
else:
    print("Final amount after 20% discount:", purchase_amount * 0.8)


# Categorize Age Group

age = int(input("Enter person's age: "))

if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
else:
    if age < 65:
        print("Adult")
    else:
        print("Senior")


# Eligibility for Discount based on Membership

is_member = input("Are you a member? (yes/no): ").lower() == 'yes'
purchase_amount = float(input("Enter total purchase amount: "))

if is_member:
    if purchase_amount >= 50:
        print("Eligible for 10% discount")
    else:
        print("Eligible for 5% discount")
else:
    if purchase_amount >= 100:
        print("Eligible for 5% discount")
    else:
        print("No discount")


#  ATM Machine Program with Conditions

affiliated_card = True  # Assuming user has an affiliated card
age = int(input("Enter your age: "))
is_senior_citizen = age >= 60
is_govt_employee = False  # Assuming user is not a government employee
grade = int(input("Enter your grade: "))

if is_govt_employee or is_senior_citizen or (affiliated_card and age < 60):
    print("Transaction approved")
    if grade < 18:
        print("Additional charge of Rs. 10 applied.")
else:
    print("Transaction denied")
