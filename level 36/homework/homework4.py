lists = [123,123,123,12,31,23,124,1234,2345,34,62,4,1365,13,6]

min_number = min(lists)

number = int(input("Enter random number here: "))

if min_number > number:
    print("Lower than minimum")
elif number > min_number:
    print("Bigger than minimum")