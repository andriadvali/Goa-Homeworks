car_name = {
    # "key" : "value",
    1 : "mwrcwdes",
    False : "brabus",
    "name_2" : "ho ho ho"
}
print("-----.get-----")
print(car_name.get(1))
print(car_name.get(False))
print(car_name.get("name_2"))
print("-----.get-----")


print("-----in-----")
if "name_2" in car_name:
    print(f"შენი მანქანის სახელიარის{car_name['name_2']}")




if "ho ho ho" not in car_name:
    print(f"ყოჩაღ!! შენ სწორად განოიცანი სახელი")

print("-----in-----") 

#andriaarakhami@gmail.com