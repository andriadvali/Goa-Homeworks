#homework;1
num = 0

for i in range(10):
    num += i
    print(num)

for i in range(1,10):
    num /= i
    print(num)

for i in range(10):
    num -= i
    print(num)

for i in range(10):
    num *= i
    print(num)

#homework;2
# >, >=, <, <=, ==, !=

print(5 > 2)
print(5 >= 2)
print(5 < 2)
print(5 <= 2)
print(5 != 2)

#homework;3

number = 3
if number == 3:
    print("სწორია")
else:
    print("არასწორია")

#homework;4
for i in range(0,20,2):
    print(i) 

#homework;5
correct_password = "andria"

user_input = input("Enter password here: ")

while user_input != correct_password:
    user_input = input("Enter password here: ")
    if user_input == correct_password:
        print("correct password")
    else:
        print("Incorrect password")
         
#homework;6
age = int(input("Enter you age here: "))

if age < 18:
    print("You are kid!!!")
elif age == 18:
    print("You are 18 years old!!!")
else:
    print("You are adult!!!")
