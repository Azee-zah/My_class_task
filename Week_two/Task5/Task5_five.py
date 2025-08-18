#MODIFY TUPLE INDIRECTLY
user_items = input("Enter three items on your shopping list: ").split()
shopping_list = tuple(user_items)
list_of_shopping_list = list(shopping_list)
print(list_of_shopping_list)
additional_item1 = ["rice"]
# for items in list_of_shopping_list:
#     list_of_shopping_list.append("oil", "yam")
# user_items2 = input("Enter two new items: ")
# new_list = list_of_shopping_list.append(additional_item1)
# print(new_list)
updated_list = tuple(list_of_shopping_list)
print("|".join(updated_list))
#figure out later