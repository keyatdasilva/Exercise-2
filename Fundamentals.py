# arithmetic
x = 3 
x += 3 
print(x)
y = 4
y *= 5
print(y)
result = x / y
print(result)
# comparison and logical operators
a = 6
b = 3
a > b 
print(a > b)
b % a 
print (b % a)
c = 5 
c <= a 
print (c <= a)
final_condition = (a > b) or (b % a) and (c <= a)
print(final_condition)

# Question 4
score = int(input("Enter your score (0-100): "))
if score >= 90:
   grade = "A" 
elif score >= 80:
   grade = "B"
elif score >= 70: 
   grade = "C"
elif score >= 60:
   grade = "D"
else: 
   grade = "F" 
print("Your grade is", grade)

# Question 4 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter an operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "Error: You can't divide by zero"
    else:
        result = num1 / num2
else:
    result = "Error: That's not a valid operation"

print("Result:", result)