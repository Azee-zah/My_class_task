# #TUPLE AND INPUT
besties = []
for names in range(5):
    names =input(f"Enter the name of your besties here {names+1}:")
    besties.append(names)
best_friends_names = tuple(besties)
print(best_friends_names[::-1])