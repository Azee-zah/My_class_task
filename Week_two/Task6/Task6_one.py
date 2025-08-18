#collect the fruits name from users using input
# store the fruit as a set using set() or {}
# display using print()
user_fruits = input("Enter five of your favourites fruits here: ").split()
fav_fruits = set(user_fruits)
print(fav_fruits)

fav_fruit = set()
for fruit in range(5):
    user_fav_fruit = input(f"Enter your favourite fruits here {fruit+1}: ")
    fav_fruit.add(user_fav_fruit)
print(fav_fruit)