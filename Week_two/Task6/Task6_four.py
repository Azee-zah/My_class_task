# CREATING UNIQUE VOTERS REGISTRATION SYSTEM
# collect voter names using input and store in a set()
#counted the number of elements in the set using len()
the_voters = set()
for names in range (3):
    voters_name = input(f"Enter your full name here {names+1}: ")
    if names in the_voters:
        print(f" warning : '{names}' already exist, please enter another name")
    else: the_voters.add(voters_name)
no_of_unique_voters = len(the_voters)
print(no_of_unique_voters)

#could not achieve displaying warning sign