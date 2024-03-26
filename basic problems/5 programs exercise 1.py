'''
#question number 1
numbers = [float(x) for x in input("Enter numbers separated by space: ").split()]
if not numbers:
    print("List is empty, cannot calculate average")
total = sum(numbers)
average = total / len(numbers)

result = average
print(f"The average is: {result}")

'''
'''
#question number 2
user_integer = int(input("Enter an integer: "))
print(f"You entered: {user_integer}")
input_string = input("Enter a string: ")
s=len(input_string)
q=int(s)
print(q)
'''

'''
#question number 3
# Adding two complex numbers
complex_num1 = 2 + 3j
complex_num2 = 1 - 5j
sum_complex = complex_num1 + complex_num2
print(f"Sum of complex numbers: {sum_complex}")

# Adding two float numbers
float_num1 = 3.14
float_num2 = 2.71
sum_float = float_num1 + float_num2
print(f"Sum of float numbers: {sum_float}")

# Adding two integer numbers
int_num1 = 5
int_num2 = 10
sum_int = int_num1 + int_num2
print(f"Sum of integer numbers: {sum_int}")

'''
'''
#question number 4
integer_value = 42
float_value = float(integer_value)
print(f"Converted float value: {float_value}"  )

'''

'''
#question number 5
# Adding string and integer using explicit conversion
string_value = "42"
integer_value = 10
sum_result = int(string_value) + integer_value
print(f"Sum of string and integer: {sum_result}")

'''

'''
#question number 6
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number: "))
result = factorial(number)
print(f"The factorial of {number} is: {result}")

'''

'''
#question numnber 7

# Displaying the first 7 multiples of 7
for i in range(1, 8):
    multiple = 7 * i
    print(f"Multiple {i}: {multiple}")
    
    
'''

'''
#question number 8

def is_right_triangle(side1, side2, side3):
    sides = [side1, side2, side3]
    sides.sort()  # Sorting the sides in ascending order

    # Using the Pythagorean theorem to check for a right triangle
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

# Accepting lengths of three sides from the user
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Checking if it is a right triangle
if is_right_triangle(side1, side2, side3):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
    
    
'''






