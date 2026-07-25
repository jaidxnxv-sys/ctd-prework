# This script stores a name (string) and an age (integer), 
# prints them together, and uses a conditional to print a message based on the age.

# Define variables with different data types
name = "Alice"       # string
age = 20             # integer

# Print both variables in one statement
print(f"Name: {name}, Age: {age}")

# Conditional logic based on the value of 'age'
if age < 13:
    print(f"{name} is a child.")
elif 13 <= age < 18:
    print(f"{name} is a teenager.")
else:
    print(f"{name} is an adult.")
