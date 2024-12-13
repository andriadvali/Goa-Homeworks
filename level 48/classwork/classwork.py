import random
def random_movie():
    list = ["interstellar", "inseption", "შერეკილები"]
    list_of_random_movis = ["მე ბებია ილიკო და ილარიონი", "ცისფერი მთები", "წუნა და წრუწუნა" ]
    for i in range(2):
        random_item = random.choices(list_of_random_movis)
        list.append(random_item)
        list_of_random_movis.remove(random_item)
    return list 

print(random_movie())   