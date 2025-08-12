#operations in list
list1 = [1, 2, 3]
list2 = [4,5]
result = list1 + list2
print(result)           #using concatenation with list

nums = [1,2]
repeated = nums * 3  # this repeated thrice
print(repeated)  
#indexing
fruits = ["apple" , "banana" , "cherry"] 
print(fruits[0])  #to index the first element
print(fruits[-1])  #to index the last element

#slicing : this is to extract portions from the list
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[::2])
 
 #Membership (for in or not in)
 #this is to help check if an element exist in a list or not
colors = []