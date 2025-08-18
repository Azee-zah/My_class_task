#WORD ANALYZER
#collect the word using input ()
# length of word using len()
#use islower(), isupper() and istitle() to check for case
#use [::-1] to reverse the word
user_word = input("Enter a nice word here: ")
print(len(user_word))
print(user_word.islower())
print(user_word.isupper())
print(user_word.istitle())
print(user_word[::-1])