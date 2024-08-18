#homework1:
for i in range(0,101,5):
    print(i)
#homework2:
number = 5
guess = int(input("Enter number: "))

while True:
    guess = int(input("Enter number: "))
    if number == guess:
        print("Correct")
    else:
        print("Incorrect")
#homework3:
number = int(input("Enter number: "))

if number % 2 == 0:
    print("ეს რიცხვი არის ლუწი")
else:
    print("ეს რიცხვი არის კენტი")
#homework4:
age = int(input("Enter your age: "))

if age > 0 and age < 12:
    print("ბავშვი")
elif age >= 13 and age <= 19:
    print("თინეიჯერი")
elif age >= 20 and age <= 64:
    print("ზრდასრული")
else:
    print("პენსიონერი")
#homework5:
number = int(input("Enter number here: "))

if number == 0:
    print("ეს რიცხვი არის 0")
elif number < 0:
    print("ეს რიცხვი არის უარყოფითი")
else:
    print("ეს რიცხვი არის დადებით")
#homework6:
age = int(input("Enter your age here: "))
experience = int(input("Enter your experience: "))


if age >= 22 and experience > 1:
    print("გილოცავთ აგიყვანეთ მასწავლებლად")
else:
    print("სამწუხაროდ ვერ აგიყვანეთ მასწავლებლად")