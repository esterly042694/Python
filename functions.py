quote = "All is fair in love and war."
print(quote.upper()) #makes uppercase
print(quote.lower()) #makes lowercase
print(quote.title()) #makes titlecase
print(len(quote)) #length of quote


name = "Benjamin" #string
age = 26 #int int(30)
gpa = 4.0 #float float(3.7)

print(int(age))
print(int(30.9))

print("My name is " + name + " and I am " + str(age) + " years old.") #convert int to string
age += 1
print(age)

birthday = 1
age += birthday
print(age)
print('\n')

#Functions
print('Here is an example fuction')

def who_am_i(): #this is a function
	name = "Ben"
	age = 26
	print("My name is " + name + " and I am " + str(age) + " years old.")

who_am_i()


def add_one_hundred(num): #adding perameters
	print(num + 100)


add_one_hundred(100)

def add(x,y): #multiple Parameters
	print(x + y)

add(7,7)


def multiply(x,y):
	return x * y

print(multiply(7,7))

def square_root(x): 
	print(x ** .5)

square_root(64)


def nl():
	print('\n')

nl()

#Boolean Expressions (True or False)
print('Boolean Expressions: ')

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool1))

nl()
#Relational and Boolean Operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal to = 7 <= 7

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 > 7) #True

test_not = not True #False

input("Press Enter to continue...")