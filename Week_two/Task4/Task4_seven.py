#LIST MANIPULATION
#list of five cities
#index the city to be replaced = new city
#use .pop() to remove 
# .append() only adds to the end of the list hence we use insert()
#display
list_of_cities = ["Lagos", "Benin", "chicago", "Ibadan", "FCT"]
print(list_of_cities)
another_city = input("Enter a new city to replace the third city: ")
list_of_cities[2] = another_city
print(list_of_cities)
list_of_cities.pop()
print(list_of_cities)
new_city = "Abeokuta"
list_of_cities.insert(0, new_city)
print(list_of_cities)