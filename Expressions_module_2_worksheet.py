def q(n):
    print(f"\n--- Q{n} ---")


# Q1: Calculate the Square of a Number
# Write an expression to calculate the square of a number.
# Sample Input: n = 7
q(1)
n = 7
print(n ** 2)

# Q2: Evaluate a Quadratic Expression
# Given values for x, a, b, and c, write an expression to compute ax² + bx + c.
# Sample Input: a = 2, b = 3, c = 4, x = 5
q(2)
a, b, c, x = 2, 3, 4, 5
print(a * x ** 2 + b * x + c)

# Q3: Find the Remainder (Modulo Operation)
# Write an expression to get the remainder when one number is divided by another.
# Sample Input: num = 29, divisor = 6
q(3)
num, divisor = 29, 6
print(num % divisor)

# Q4: Check if a Number is Positive, Negative, or Zero (Conditional Expression)
# Use a single line expression to print whether a number is positive, negative, or zero.
# Sample Input: num = -8
q(4)
num = -8
print("Positive" if num > 0 else "Negative" if num < 0 else "Zero")

# Q5: Get the Absolute Value
# Write an expression to get the absolute value of a number.
# Sample Input: n = -12
q(5)
n = -12
print(abs(n))

# Q6: Swap Two Numbers Without Using a Third Variable
# Swap two variables' values using a single line of code.
# Sample Input: a = 15, b = 8
q(6)
a, b = 15, 8
print("Before:", a, b)
a, b = b, a
print("After:", a, b)

# Q7: Calculate the Average of Three Numbers
# Write an expression to find the average of three numbers.
# Sample Input: x = 5, y = 8, z = 10
q(7)
x, y, z = 5, 8, 10
print((x + y + z) / 3)

# Q8: Use the Ternary Operator to Find the Minimum of Two Numbers
# Use a single expression to find the smaller of two numbers.
# Sample Input: a = 20, b = 13
q(8)
a, b = 20, 13
print(a if a < b else b)

# Q9: Bitwise OR and XOR
# Write expressions to calculate the result of bitwise OR and bitwise XOR between two numbers.
# Sample Input: x = 9, y = 5
q(9)
x, y = 9, 5
print("OR:", x | y)
print("XOR:", x ^ y)

# Q10: Check if a Number is Divisible by Both 2 and 3
# Write a single expression that evaluates to True if a number is divisible by both 2 and 3, otherwise False.
# Sample Input: num = 18
q(10)
num = 18
print(num % 2 == 0 and num % 3 == 0)

# Q11: Find the Largest of Three Numbers Using Only Expressions
# Without using if, elif, or any function, write an expression to find the largest of three given numbers.
# Sample Input: a = 14, b = 27, c = 19
q(11)
a, b, c = 14, 27, 19
print(a * ((a >= b) & (a >= c)) + b * ((b > a) & (b >= c)) + c * ((c > a) & (c > b)))

# Q12: Check if a Number is a Power of Two
# Write a single Boolean expression to check if a number is a power of two.
# Sample Input: n = 32
q(12)
n = 32
print(n > 0 and (n & (n - 1)) == 0)

# Q13: Find the Second Largest of Three Numbers
# Write an expression (no functions, no if) to get the second largest value among three numbers.
# Sample Input: a = 20, b = 12, c = 18
q(13)
a, b, c = 20, 12, 18
big = a * ((a >= b) & (a >= c)) + b * ((b > a) & (b >= c)) + c * ((c > a) & (c > b))
small = a * ((a <= b) & (a <= c)) + b * ((b < a) & (b <= c)) + c * ((c < a) & (c < b))
print(a + b + c - big - small)

# Q14: Toggle a Specific Bit in an Integer
# Given a number and a bit position, write an expression to toggle (flip) that bit.
# Sample Input: n = 12, bit_position = 2
q(14)
n, bit_position = 12, 2
print(n ^ (1 << bit_position))

# Q15: Count the Number of 1 Bits in an Integer (No Loops)
# Write an expression (using built-in functions) to count how many 1s are in the binary representation of a number.
# Sample Input: n = 29
q(15)
n = 29
print(bin(n).count("1"))

# Q16: Find the Sign of a Number as -1, 0, or 1 (Using Only Expressions)
# Write a single expression that gives -1 for negative numbers, 0 for zero, and 1 for positive numbers.
# Sample Input: n = -56
q(16)
n = -56
print((n > 0) - (n < 0))

# Q17: Check If a Number is a Multiple of 4 but Not of 8
# Write an expression that is True only if a number is divisible by 4 but not by 8.
# Sample Input: n = 12
q(17)
n = 12
print(n % 4 == 0 and n % 8 != 0)

# Q18: Rotate Bits Left by k Positions
# Given a number (assume 8 bits) and a value k, write an expression to rotate its bits to the left by k positions.
# Sample Input: n = 150, k = 2
q(18)
n, k = 150, 2
print(((n << k) | (n >> (8 - k))) & 0xFF)

# Q19: Find the Difference Between the Largest and Smallest of Three Numbers (Using Only Expressions)
# Write an expression to find the difference between the largest and the smallest of three numbers.
# Sample Input: a = 8, b = 27, c = 14
q(19)
a, b, c = 8, 27, 14
big = a * ((a >= b) & (a >= c)) + b * ((b > a) & (b >= c)) + c * ((c > a) & (c > b))
small = a * ((a <= b) & (a <= c)) + b * ((b < a) & (b <= c)) + c * ((c < a) & (c < b))
print(big - small)

# Q20: Set the nth Bit of a Number
# Write an expression that sets the nth bit of a given integer to 1 (leave other bits unchanged).
# Sample Input: n = 9, bit_position = 3
q(20)
n, bit_position = 9, 3
print(n | (1 << bit_position))
