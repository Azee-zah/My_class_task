# shopping list manager
shopping_list = []
for item in range(3):
    user_list = input(f"Enter your items here {item+1}: ")
    shopping_list.append(user_list)
print(f"{shopping_list}")