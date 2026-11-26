def q(n):
    print(f"\n--- Q{n} ---")


# Q1: Given a = 4, b = 5, write expressions to calculate their sum and product in a single line.
q(1)
a, b = 4, 5
print(a + b, a * b)

# Q2: Given an integer n, write an expression that is True if n is odd.
q(2)
n = 7
print(n % 2 == 1)

# Q3: Given a number n, write an expression to get the last digit (units place) of n.
q(3)
n = 1234
print(n % 10)

# Q4: Given temperature in Celsius c, write an expression to convert it to Fahrenheit.
q(4)
c = 37
print(c * 9 / 5 + 32)

# Q5: Given x, write an expression to increment its value by 1.
q(5)
x = 10
print(x + 1)

# Q6: Given x and y, write an expression to calculate their average.
q(6)
x, y = 6, 9
print((x + y) / 2)

# Q7: Given a and b, write an expression for their difference (a-b).
q(7)
a, b = 15, 8
print(a - b)

# Q8: Given n, write an expression that gives double its value.
q(8)
n = 6
print(n * 2)

# Q9: Given n, write an expression for its square root using the ** operator.
q(9)
n = 49
print(n ** 0.5)

# Q10: Given n, write an expression that is True if n is divisible by 5.
q(10)
n = 25
print(n % 5 == 0)