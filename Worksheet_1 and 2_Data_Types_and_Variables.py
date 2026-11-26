def ws(n):
    print(f"\n{'=' * 30}\n  WORKSHEET {n}\n{'=' * 30}")

def q(n):
    print(f"\n--- Q{n} ---")


ws(1)

# Q1: Assign two integer variables and print their sum, difference, product, and quotient.
a, b = 20, 4
print(a + b, a - b, a * b, a / b)

# Q2: Store two float numbers, add them, and print the result rounded to two decimal places.
x, y = 3.14159, 2.71828
print(round(x + y, 2))

# Q3: Concatenate two strings stored in separate variables with a space between them and display.
s1, s2 = "Hello", "World"
print(s1 + " " + s2)

# Q4: Repeat a given string five times and print the result.
s = "Python "
print(s * 5)

# Q5: Compare two integers and print boolean results for each comparison (==, !=, >, <, >=, <=).
a, b = 10, 20
print(a == b, a != b, a > b, a < b, a >= b, a <= b)

# Q6: Log Session integer, float, string, and boolean variables, and use the type() function to print each data type.
i, f, s, b = 10, 3.5, "hi", True
print(type(i), type(f), type(s), type(b))

# Q7: Convert a numeric string ("50") to an integer and a float, then print the converted values and their types.
n = "50"
i, f = int(n), float(n)
print(i, type(i))
print(f, type(f))

# Q8: Add an integer (25) and a numeric string ("25") after converting the string explicitly, and print the result.
print(25 + int("25"))

# Q9: Assign two complex numbers, then print their sum, difference, and product.
c1, c2 = 2 + 3j, 1 - 4j
print(c1 + c2, c1 - c2, c1 * c2)

# Q10: Identify valid Python variable names: data1, 1data, _data, data_1, data-1, True, totalSum.
import keyword
for name in ["data1", "1data", "_data", "data_1", "data-1", "True", "totalSum"]:
    print(name, name.isidentifier() and not keyword.iskeyword(name))
# Answer: Valid: data1, _data, data_1, totalSum.
# Invalid: 1data (starts with a digit), data-1 (hyphen not allowed), True (reserved keyword).

# Q11: Assign "Python", 3.14, and True to variables using a single-line assignment, and print each value.
a, b, c = "Python", 3.14, True
print(a, b, c)

# Q12: Swap two variable values in one line and print the values before and after swapping.
a, b = 5, 10
print("Before:", a, b)
a, b = b, a
print("After:", a, b)

# Q13: Assign an integer to a variable, then reassign it to a float and string sequentially, printing type and value after each step.
v = 10
print(type(v), v)
v = 10.5
print(type(v), v)
v = "ten"
print(type(v), v)

# Q14: Define a constant PI = 3.14159 and calculate the circumference of a circle with radius 5, then print the result.
PI = 3.14159
r = 5
print(2 * PI * r)

# Q15: Assign your name, age, and favorite number to variables and display them using an f-string.
name, age, fav = "Varsha", 22, 7
print(f"Name: {name}, Age: {age}, Favorite number: {fav}")

# Q16: Calculate and print the quotient and remainder of two integers using // and %.
a, b = 17, 5
print("Quotient:", a // b, "Remainder:", a % b)

# Q17: Use augmented assignment (+=, -=, *=, /=) on a variable initialized as 10, printing its value at each step.
x = 10
x += 5; print(x)
x -= 3; print(x)
x *= 2; print(x)
x /= 4; print(x)

# Q18: Assign and print the string Python's "syntax" is easy, properly using escape characters.
print('Python\'s "syntax" is easy')

# Q19: Perform arithmetic (+, *) with boolean values (True, False) and print the results.
print(True + True, True + False, True * False, True * 5, False * 10)

# Q20: Add an integer (5) to a string ("Hello"), observe the error, and explain why it occurs.
try:
    print(5 + "Hello")
except TypeError as e:
    print("Error:", e)
# Answer: It raises a TypeError. Python is strongly typed and won't guess whether you want
# addition or joining. Fix: convert first, like str(5) + "Hello".

# Q21: Assign a very large integer to a variable and print its value and data type.
big = 12345678901234567890123456789012345678901234567890
print(big, type(big))

# Q22: Assign the same value (100) simultaneously to three variables (a, b, and c), then print each variable.
a = b = c = 100
print(a, b, c)

# Q23: Assign None to a variable, then print its value and type.
n = None
print(n, type(n))

# Q24: Perform arithmetic between integer (10) and float (3.5) variables, then print the result and its type.
r = 10 + 3.5
print(r, type(r))

# Q25: Slice the string "PythonProgramming" into "Python" and "Programming" separately and print both results.
s = "PythonProgramming"
print(s[:6])
print(s[6:])


ws(2)

# Q1: Given the assignment a = b = 10, what happens if you later set b = 20? What is the value of a? Explain why.
# Answer: a stays 10 and b becomes 20. Both names pointed to the same object 10.
# b = 20 moves only b to a new object, so a is untouched.

# Q2: What will be the output and the type of each variable? Explain your answer.
# x = 2
# y = 2.0
# z = "2"
# w = x + int(z)
# v = str(x) + z
x = 2
y = 2.0
z = "2"
w = x + int(z)
v = str(x) + z
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(w, type(w))
print(v, type(v))
# Answer: x is 2 (int), y is 2.0 (float), z is "2" (str).
# w = 2 + 2 = 4 (int), because z is converted to int first.
# v = "2" + "2" = "22" (str), because + joins strings.

# Q3: What is the difference between mutable and immutable data types in Python? Name three types from each category.
# Answer: Mutable objects can be changed in place (list, dict, set).
# Immutable objects can't be changed, and any "change" creates a new object (int, str, tuple).

# Q4: Given x = [1, 2, 3] and y = x, then x[0] = 9. What are the values of x and y? Explain the behavior.
# Answer: Both are [9, 2, 3]. y = x copies the reference, not the list,
# so both names point to the same list. Use y = x.copy() for a separate copy.

# Q5: How does Python treat variable names that have the same value but are of different data types?
# For example, what is the result of 3 == 3.0 and 3 is 3.0?
# Answer: 3 == 3.0 is True because == compares values.
# 3 is 3.0 is False because is compares identity, and an int and a float are different objects.

# Q6: What is the result of the following code? Explain your answer.
# a = (5)
# b = (5,)
# print(type(a))
# print(type(b))
a = (5)
b = (5,)
print(type(a))
print(type(b))
# Answer: a is int, b is tuple. The comma makes the tuple, not the brackets.

# Q7: What happens if you try to use a list as a dictionary key? Why?
# Answer: It raises TypeError (unhashable type: 'list'). Dictionary keys must be hashable,
# meaning their hash never changes. Lists are mutable, so they can't be keys. Tuples can.

# Q8: What is the difference between None, 0, False, and "" in Python? Are they the same or different as variables?
# How does Python treat them in conditional statements?
# Answer: They are different objects with different types (NoneType, int, bool, str).
# All four are falsy in an if condition.
# 0 == False is True because bool is a subclass of int. None == False and "" == False are False.

# Q9: Does Python automatically convert between integer and float types? Show a code example and explain what happens.
a = 5
b = 2.5
c = a + b
print(c, type(c))
# Answer: Yes. In mixed arithmetic Python converts the int to float automatically, so 5 + 2.5 = 7.5 (float).

# Q10: What will be the output and types in this code?
# a = "5"
# b = 5
# c = a * b
# d = b * a
# print(c, d)
a = "5"
b = 5
c = a * b
d = b * a
print(c, d)
print(type(c), type(d))

# Q11: Can variable names start with an underscore (_) or contain special characters like $ or @? Explain the rules.
# Answer: Starting with _ is allowed. $ and @ are not.
# Rules: start with a letter or _, then only letters, digits and _. No keywords. Names are case-sensitive.

# Q12: What is the difference between single quotes ('), double quotes ("), and triple quotes (''' or """) for strings?
# Are they the same data type?
# Answer: All are str. Single and double quotes are interchangeable (use one to hold the other, like "It's").
# Triple quotes allow multi-line strings and docstrings.

# Q13: Explain the difference between an empty list [], an empty tuple (), and an empty dictionary {}
# in terms of their types and mutability.
# Answer: [] is a list (mutable), () is a tuple (immutable), {} is a dict (mutable).
# An empty set is set(), not {}.

# Q14: Given the code:
# x = [1, 2, 3]
# y = x
# x = [4, 5, 6]
# print(y)
# What is the value of y and why?
# Answer: [1, 2, 3]. x = [4, 5, 6] points x to a new list and doesn't change the old one,
# which y still points to.

# Q15: How does variable assignment differ between mutable and immutable objects? Illustrate with an example.
# Answer: Immutable (int): a = 5, b = a, b += 1 creates a new object, so a stays 5 and b is 6.
# Mutable (list): l2 = l1, l2.append(3) changes the one shared list, so both show [1, 2, 3].

# Q16: Explain what happens here:
# x = 1000
# y = 1000
# print(x is y)
# Answer: Python caches small ints (-5 to 256), so is is always True for those.
# For 1000, the result depends on the Python version (it may print True or False).
# Use == to compare values.

# Q17: How do you convert between data types (e.g., string to int, int to float, list to tuple) in Python?
# Show a code example.
print(int("50"))
print(float(5))
print(str(100))
print(tuple([1, 2, 3]))
print(list((1, 2, 3)))

# Q18: What will be printed?
# x = "10"
# y = 2
# print(x * y)
# print(y * x)
# Why?
x = "10"
y = 2
print(x * y)
print(y * x)
# Answer: Both print 1010. str * int repeats the string, it does not multiply to 20.

# Q19: Is type(5) == int always True? Is isinstance(5, int) always True? Explain the difference.
# Answer: Both are True for 5. type() checks the exact type, so type(True) == int is False.
# isinstance() also accepts subclasses, so isinstance(True, int) is True. isinstance is preferred.

# Q20: Can a Python variable change its data type after assignment? Give an example and explain the implications.
# Answer: Yes, this is dynamic typing. Example: v = 10, then v = "ten", then v = [1, 2].
# The type belongs to the object, not the variable name.
# Implication: flexible code, but type errors only show up at runtime.