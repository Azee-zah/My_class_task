# NAME ORGANIZER
#collect the names from the user using input
#convert to lowercase using lower()
# use sort () or sorted for alphabetical order
#display
user_names = input("Type in 5 names here: ").split()
converted = [user_names.lower() for names in user_names]
print(sorted(converted))
print(converted, sep='\n')
 #can not figuire out why the list can not be converted to lower