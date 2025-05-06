def add_five(a):
    return a+5

print(add_five(10))

func2 = add_five
print(func2(10))
print(func2(20))

try:
    result = 10 / 0
except:
    print("შეცდომა არ მოხდა")

