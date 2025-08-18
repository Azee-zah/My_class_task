# TUPLE OPERATIONS
# create an empty list
#collect the states from the user using input and append to the list
# convert the list to tuple
#print first state [0] and last [-1]
#check for lagos in the tuple using in
# count the number of states using len()
states = []
for state in range(5):
    n_state = input(f'Enter 5 Nigerian states here {state+1}: ')
    states.append(n_state)
Nigerian_states = tuple(states)
no_of_entered_states = len(Nigerian_states)
print(Nigerian_states[0])
print(Nigerian_states[-1])
print("Lagos" in Nigerian_states)
print(no_of_entered_states)
