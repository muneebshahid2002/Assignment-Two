# Write a program to check whether a person is eligible to vote or not?
# voting_age = 18
# age = int(input("Enter your age: "))

# if age >= voting_age:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")
    
# Write a program to check char is vowel or not.
# char = input("Enter a character: ")

# if char in 'aeiouAEIOU':
#     print("Vowel")
# else:
#     print("Consonant")
 
        
# Write a program to check the number is positive or negative. User input.
# num = int(input("Enter a number: "))

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# Write a program to check whether a number is odd or even?

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Write a program to display the grade of the user in subject A, ask user marks obtained out of 100
# marks = int(input("Enter your marks in subject A (out of 100): "))

# if marks >= 90:
#     print("Grade: A")
# elif marks >= 80:
#     print("Grade: B")
# elif marks >= 70:
#     print("Grade: C")
# elif marks >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")

# Write a program to check whether a number is divisible by 7
# number = int(input("Enter a number: "))

# if number % 7 == 0:
#     print(f"{number} is divisible by 7")
# else:
#     print(f"{number} is not divisible by 7")


# Write a program to check if year is leap year.
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# Write a program to ask user its name and check whether name consists of 5 or more letters

# name = input("Enter your name: ")

# if len(name) >= 5:
#     print(f"{name} consists of 5 or more letters")
# else:
#     print(f"{name} consists of less than 5 letters")

# Write a program that accepts 3 inputs from user. input 1 and input 2 should be numbers and the third input should be mathematical operator. 
# Perform operation accordingly
# for example
# input1 is 5 and input2 is 10 and input3 is +
# then output should be 15
# input1 is 5 and input2 is 10 and input3 is *
# then output should be 50


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# operator = input("Enter mathematical operator (+, -, *, /): ")

# if operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2
# elif operator == "/":
#     if num2 == 0:
#         print("Division by zero is not allowed")
#     else:
#         result = num1 / num2
# else:
#     print("Invalid operator")

# if operator not in ("/", 0):  # Print result only for valid operations (excluding division by zero)
#     print(f"Result: {result}")



# Write a program that accepts 1 input from user and check if the number is divisible by 2 and 3 both.
# for example
# input1 is 10
# output should be "10 is only divisible by 2"
# input1 is 9
# output should be "9 is only divisible by 3"
# input1 is 12
# output should be "12 is divisible by 2 and 3"


# number = int(input("Enter a number: "))

# divisibility_message = ""
# if number % 2 == 0:
#     divisibility_message += "divisible by 2"
# if number % 3 == 0:
#     if divisibility_message:
#         divisibility_message += " and "
#     divisibility_message += "divisible by 3"

# if not divisibility_message:
#     print(f"{number} is not divisible by 2 or 3")
# else:
#     print(f"{number} is {divisibility_message}")


# Write a program that accepts 2 inputs from user and check which number is largest.
# for example:
# input1 is 5 and input2 is 10
# output should be 10 as this number is larger than 5


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if num1 > num2:
#     print(f"{num1} is larger")
# elif num1 < num2:
#     print(f"{num2} is larger")
# else:
#     print("Both numbers are equal")



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