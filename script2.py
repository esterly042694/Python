#importing
import sys #system functions and parameters
from datetime import datetime as dt #import with alias

print(dt.now())
print(sys.version)

my_name = "Ben"
print(my_name[0]) #first item
print(my_name[-1]) #last item

sentence = "This is a sentence."
print(sentence[:4]) 
print(sentence.split())

sentence_split = sentence.split()
sentence_join = " ".join(sentence_split)

print(sentence_join)

quote ="He said,\"give me all your money.\""
print(quote)

too_much_space = "                                     Hello"
print(too_much_space.strip())


print("A" in "Apple") #is "A" in "Apple", yes so returns true.
letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #improoved letter search.


movie = "Lord of the Rings"
print("My favorite movie is {}.".format(movie))


#Dictionaries - Key / value pairs {}

drink = {"White Russian": 7, "Old Fassion":10, "Lemon Drop":8} #drink is key, price is value
print(drink)

employees = {"Finance": ["Bob","Linda","Tina"], "I.T.":["Gene","Louise","Teedy"], "H.R.":["Jimmy", "JR","Mort"]}
print(employees)
employees["Legal"] = ["Mr. Frond"]
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]})
print(employees)

drink["White Russian"] = 8
print(drink)

print(drink.get("White Russian"))


input("Press Enter to continue...")