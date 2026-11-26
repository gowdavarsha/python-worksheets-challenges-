def q(n):
    print(f"\n--- Q{n} ---")


# Q1: How does Python handle integer overflow, and what happens if you assign a value greater than what a C/C++ int would allow?
# Answer: Python ints have no fixed size and grow with memory, so there is no overflow.
# A C/C++ 32-bit int overflows past 2147483647.

# Q2: Explain the difference between mutable and immutable data types in Python, with practical examples.
s = "hello"
t = s.upper()
print(s, t)
l = [1, 2, 3]
l.append(4)
print(l)
tup = (1, 2, 3)
try:
    tup[0] = 9
except TypeError as e:
    print("Error:", e)
# Answer: Mutable objects change in place (list.append). Immutable objects can't change:
# s.upper() returns a new string, and tup[0] = 9 raises TypeError.

# Q3: What is the output and data type of the expression: 3 + 4.0 * 2 // 3? Explain each step.
step1 = 4.0 * 2
step2 = step1 // 3
step3 = 3 + step2
print(step1, step2, step3)
print(3 + 4.0 * 2 // 3, type(3 + 4.0 * 2 // 3))

# Q4: How does Python's dynamic typing affect performance and debugging in large applications?
# Answer: Flexible and quick to write, but slower at runtime because types are checked while running.
# Type bugs show up only when that line runs. Large projects use type hints and tools like mypy.

# Q5: Describe the difference between is and == when comparing variables. Provide an example where they behave differently.
# Answer: == compares values, is compares identity (same object).
# Example: a = [1, 2, 3] and b = [1, 2, 3] are separate lists with equal values,
# so a == b is True and a is b is False.

# Q6: Can you modify a string in place in Python? If not, explain why with reference to data types.
# Answer: No. Strings are immutable, so s[0] = "H" raises TypeError.
# Build a new string instead, like "H" + s[1:].

# Q7: Given the code below, what is the final value and type of x after all assignments?
# x = 3
# x += 2.0
# x = str(x)
# x += '1'
x = 3
x += 2.0
x = str(x)
x += '1'
print(x, type(x))

# Q8: Why does the following code throw an error, and how can you fix it?
# age = 20
# print("Age: " + age)
age = 20
try:
    print("Age: " + age)
except TypeError as e:
    print("Error:", e)
print("Age: " + str(age))
print("Age:", age)
print(f"Age: {age}")
# Answer: Python can't join a str and an int (TypeError).
# Fixes: str(age), a comma in print, or an f-string.

# Q9: What is typecasting? Provide examples where implicit and explicit type conversions may cause bugs.
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
print(int(3.9))
print(bool("False"))
try:
    int("3.5")
except ValueError as e:
    print("Error:", e)
# Answer: Typecasting is converting one data type to another.
# Implicit bug: 0.1 + 0.2 = 0.30000000000000004, so == 0.3 is False.
# Explicit bugs: int(3.9) gives 3 (chops, no rounding), int("3.5") raises ValueError, bool("False") is True.

# Q10: How does Python treat Boolean values as integers? Show an example where this is useful.
answers = [True, False, True, True]
print(True + True)
print(sum(answers))
# Answer: True is 1 and False is 0 (bool is a subclass of int).
# Useful for counting: sum(answers) counts the Trues.

# Q11: Explain the concept of interning in Python strings and its effect on variable comparison.
# Answer: Python reuses one copy of some strings, so two variables with the same short string
# can be the same object (is gives True). Strings built at runtime may not be interned,
# so == is True but is can be False. Always use == to compare strings.

# Q12: What is the significance of the id() function when working with variables of immutable and mutable types?
# Answer: id() gives the object's memory identity. Immutable: changing the value gives a new id.
# Mutable: in-place changes keep the same id. The same id means the same object.

# Q13: Why can't variable names start with a number in Python? What are some other restrictions on variable names?
# Answer: The parser would confuse something like 1var with a number.
# Other rules: only letters, digits and _, no keywords, and names are case-sensitive.

# Q14: Describe what happens in memory when you do:
# a = [1, 2, 3]
# b = a
# b[0] = 10
# print(a)
# Answer: One list object is created. b = a adds a second name for the same list.
# b[0] = 10 changes that one list, so print(a) shows [10, 2, 3].

# Q15: How are global and local variables managed in Python functions? Provide an example that demonstrates a UnboundLocalError.
count = 10

def change():
    global count
    count += 1

def broken():
    try:
        count += 1
    except UnboundLocalError as e:
        print("Error:", e)

change()
print(count)
broken()
# Answer: A function can read a global. If it assigns to the name, Python treats it as local for the whole function.
# count += 1 without global reads a local with no value yet, so UnboundLocalError. Fix: global count.

# Q16: Can two different variables refer to the same object in Python? How can you check this?
# Answer: Yes, with b = a. Check with a is b or id(a) == id(b). == only checks values.

# Q17: When would you use the None data type? Give an example of a good use case.
def find_user(name):
    users = {"varsha": 22, "anil": 30}
    return users.get(name)

result = find_user("ravi")
print(result)
if result is None:
    print("User not found")
# Answer: None means "no value". Use it when a function may find nothing (dict.get on a missing key),
# or as a safe default argument (items=None). Check it with is None.

# Q18: Is it possible to store a function in a variable? Demonstrate how and why you might do this.
def greet(name):
    return "Hello, " + name

say = greet
print(say("Varsha"))

def square(x):
    return x * x

def apply(fn, value):
    return fn(value)

print(apply(square, 4))
# Answer: Yes, functions are objects. say = greet (no brackets) stores it, say("Varsha") calls it.
# Why: pass functions as arguments, store them in dicts, or choose behaviour at runtime.

# Q19: How does Python's handling of large integers differ from other languages like Java or C++?
# Answer: Python ints grow as needed with no overflow, limited only by memory.
# Java int (32-bit), long (64-bit) and C++ int overflow, so Java needs BigInteger.

# Q20: What is the difference between single quotes (') and double quotes (") in Python string assignment?
# Answer: No difference, both give str. Use one to hold the other ("It's", 'He said "hi"'),
# or escape with \'.
