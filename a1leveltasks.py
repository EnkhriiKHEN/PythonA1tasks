# Ask the user for a number and print whether it’s odd or even.
import random
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

print("Thanks!")

# Take two numbers and an operator (+, -, *, /) from the user and calculate the result.
a = int(input("enter a:"))
operator = str(input("Choose operator (+, -, *, /): "))
b = int(input("enter b:"))

if operator == "+":

    print("a+b=", a+b)

if operator == "-":
    print("a-b=", a-b)

if operator == "/":
    print("a/b=", a/b)

if operator == "*":
    print("a*b=", a*b)


# using calculator
def calculator(a, b, operator):
    operations = {
        "+": a + b,
        "-": a - b,
        "*": a * b,
        "/": a / b
    }
    return operations.get(operator, "Invalid operator")


a = int(input("Enter a: "))
op = input("Choose operator (+, -, *, /): ")
b = int(input("Enter b: "))

print("Result:", calculator(a, b, op))

# Create a list of numbers and print the sum using a loop.

a = [2, 4, 4, 5, 6, 7, 7, 8, 9]
total = 0   # use total instead of sum

for num in a:     # loop through each element
    total += num  # add element to total

print("Sum =", total)

# take a string input and print it backwards.
str = str(input("your fav food?:"))[::-1]print(str)

# Ask for a word and count how many vowels (a, e, i, o, u) it has.

word = input("Enter a word: ")

vowels = "aeiou"
count = 0

for letter in word.lower():   # convert to lowercase so "A" also works
    if letter in vowels:
        count += 1

print("Number of vowels:", count)

# Find Maximum in List Given a list of numbers, find the largest number without using max().

a = [5, 6, 7, 11, 8, 9, 0]
largest = max(a)
print("largest:", largest)

# Print the first 10 numbers in the Fibonacci sequence using a loop.
n = 10   # how many numbers want
a, b = 0, 1

print("Fibonacci sequence:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b   # update values'''
# Generate a random number between 1 and 20. Let the user guess until they get it right.


# generate random number between 1 and 20
secret_number = random.randint(1, 20)

print("I'm thinking of a number between 1 and 20.")

guess = None
while guess != secret_number:
    guess = int(input("Take a guess: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("🎉 Correct! The number was", secret_number)

# Given a list with repeated elements, create a new list with only unique elements.
numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]
unique = []

for num in numbers:
    if num not in unique:   # add only if not already in list
        unique.append(num)

print("Original list:", numbers)
print("Unique list:", unique)


# reate a dictionary with 3-5 items (like name, age, city). Print keys, values, and items.
# create dictionary
person = {
    "name": "Alice",
    "age": 21,
    "city": "Ulaanbaatar"
}

# print keys
print("Keys:", person.keys())

# print values
print("Values:", person.values())

# print items (key + value pairs)
print("Items:", person.items())
