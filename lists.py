#Lists - Have brackets []

movies = ["Lord of the Rings", "The Hangover", "The Purge", "The Hobbit"]

print(movies[0]) #number -1 for position in list
print(movies[1])
print(movies[1:3]) #2nd position and 4th
print(movies[1:]) #2nd position on
print(movies[:1]) #everything before 2nd position
print(movies[-1]) #last item

print(len(movies))
movies.append("JAWS") #append adds to list at the END
print(movies)

movies.pop() #removes the LAST item from the list
print(movies)

movies.pop(0) #removes the FIRST item because of (0) position is specified
print(movies)


input("Press Enter to continue...")