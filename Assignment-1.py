#section 1 Set data

name = "Jaiden"
age  = 26
height = 5.6
is_student = True

#display data

print(name,type(name))
print(age,type,(age))
print(height,type(height))
print(is_student,type(is_student))

#type(var)= identify data type

#==========================================


#section 2
#age calculator

# collect and display age and name with greeting message
print("What Is Your Name?")
name = input()

#print("birth year?")
#int(input())
import datetime
age = datetime.datetime.now().year - int(input("Enter your birth year: "))
print(f"Hello {name}. You are approximately {age} years old.")


#====================================================



#section 3 calculator
# get data

in1 = float(input("enter digit:"))
in2 = float(input("enter digit:"))
product = in1 * in2
print(f"{in1} + {in2} = {product}")
#====================================================


#section 4
#formatted receipt

#checkout details

prod_name = "vinyl"
price = 38.50
quantity = 3
#calculate

total = price * quantity

#output

print("====== RECEIPT ======")
print(f"Item: {prod_name}")
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")
print("====================")
print(f"Total: ${total:.2f}")
print("=====================")

#section 5
#profile card

#gather data
hometown = input("Where were you born? ")
hobby = input("What do you do? ")
fact = input("Fun Fact about you? ")

print("=======PERSONAL PROFILE=======")
#name = input("Full Name:")
#frontend
print("====================")
print(f"Name: {name}")
print("====================")


print(f"Hometown: {hometown}")
print(f"Hobby: {hobby}")
print(f"fact: {fact}")
print(f"Age: {age}")



