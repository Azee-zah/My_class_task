# TO CREATE AND DISPLAY
#use the for to create the range
#use tuple() to store
#print out with \n using (*my_tuple, '\n')
Nigerian_dishes = list()
for dish in range(3):
    user_fav_dish = input(f"Enter your fav. dishes here {dish+1}: ")
    Nigerian_dishes.append(user_fav_dish)
fav_nigerian_dishes = tuple(Nigerian_dishes)
print(fav_nigerian_dishes)
print(*fav_nigerian_dishes, sep='\n')
# for item in fav_nigerian_dishes:
#     print(item)
 