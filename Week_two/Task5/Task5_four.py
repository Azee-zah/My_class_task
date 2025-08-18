# TUPLE UNPACKING
# collect the necessary data from the users using input
# store in a tuple() and unapck into a variable
# display output
first_name = input("Enter your first name here: ")
age = input("How old are you? ")
favorite_color = input("what is your favourite colour? ")
home_town = input("Tell us your home town: ")
user_profile =(first_name, age, favorite_color, home_town)
first_name, age, favorite_color, home_town =user_profile
print(f"Name:\t{first_name}\nAge:\t{age}\nColor:\t{favorite_color}\nHome:\t{home_town}")