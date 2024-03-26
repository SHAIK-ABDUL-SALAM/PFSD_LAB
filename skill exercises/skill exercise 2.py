# Ex-2-1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number: "))
print(f"Factorial of {number}: {factorial(number)}")

# Ex-2-2
print("First 7 multiples of 7:")
for i in range(1, 8):
    print(7 * i)

# Ex-2-3
def is_right_triangle(a, b, c):
    return a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2

side_a, side_b, side_c = map(float, input("Enter lengths of three sides separated by space: ").split())
if is_right_triangle(side_a, side_b, side_c):
    print("It's a right triangle.")
else:
    print("It's not a right triangle.")

# Ex-2-4
n = int(input("Enter number of asterisks you need: "))
x = 1
for i in range(n):
    print("*" * x)
    x = x + 1

x = n - 1
for i in range(n):
    print("*" * x)
    x = x - 1

# Ex-2-5
bS = input("Enter 4-binary digit numbers: ")
bN = bS.split(',')
dv5 = [binary for binary in bN if int(binary, 2) % 5 == 0]
print(','.join(dv5))
