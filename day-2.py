# list-ordered collections
from operator import truediv
from traceback import print_stack

'''
ab = ['a','b','c']
print(ab)
print(ab[1]) #index call
#(index-1)=last item in the list
print(ab[-1])
#element change
ab[1] = 'd'
print(ab)
#add a new element(always add in last position)
ab.append('e') 
print(ab)
#inserting elements into a list(at any position)
ab.insert(2,'f')
print(ab)
#Removing element from a list
del ab[1]
print(ab)
#pop method - remove the last element of a list
popped_ab = ab.pop() #which element is remove in the list that,s indicate
print(popped_ab)
print(ab) #show the list

#when you want to delete an item from a list and not use that item in any way,use the del statement;
#if you want to use an item as you remove it, use the pop() method.

popped_ab = ab.pop(1)
print(ab)
#Removing a item by value
ab.remove('c')
print(ab)
'''

'''
cars = ['bmw','audi','toyota','subaru']
#sorting a list permanently
cars.sort()
print(cars)
#reverse alphabetical order
cars.sort(reverse = True)
print(cars)
'''
'''
#Sorted() function can accept a reverse = True agrment
cars = ['bmw','audi','toyota','subaru']
print("Here is the orginal list: ")
print(cars)
print("\n Here is the sorted list: ")
print(sorted(cars))
print("Here is the orginal list again: ")
print(cars)
'''

'''
#printing a list in  a reverse order
cars = ['bmw','audi','toyota','subaru']
cars.reverse()
print(cars)
print(len(cars))
#Python counts the items in a list starting with one.
'''
'''
#for loop
magicians =['abir','anu','adil','saham']
for magician in magicians:
    
    print("They are the: ",magician)
else:
    print("The for loop is over")
'''

'''
#While loop
current_number =1
while current_number <=10:
    print(current_number)
    current_number+=1
'''

'''
#input function
message = input("Tell me something and I will repeat it back to you")
print(message)

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\n What is your first name? "

name = input(prompt)
print("\n Hello, {name}!")
'''

'''
#if statement
cars = ['bmw','audi','toyota','subaru']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
'''
'''
#checking for equality(==)
car1 = 'bmw'
car2 ='audi'
print(car1 == car2)

#checking for Inequality(!=)
requested_topping = 'Mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#Numerical Comparisons
Age =10
print(Age<21)
print(Age>=21)

#Checking Multiple Conditions
age1 = 22
age2 = 30
age = age1>20 and age2<35
print(age)
age = age1>25 or age2<35
print(age)
'''
'''
#checking whether a value is in a list
name = ['Abir','Anu','Adil','Saham']
print('Saham' in name)
print('Alamin' in name)


#checking whether a value is not in a list
banner_user = ['andrew','carolina','david']
user = 'marie'
if user not in banner_user:
    print("{user.title()},you can post a response if you wish")
'''
'''
#if-elif-else statement
age = 19
if age>=30:
    print("You are old enough to vote")
elif age<=25:
    print("you are selected as a candidate")
else:
    print("Sorry,you are too young to vote")
'''

'''
#Checking that list is not empty
r =[]
if r:
    print('\n')

else:
    print("Are you sure you want a plain? ")
'''

'''
# Using multiple lists
available_toppings = ['mushrooms', 'olives',
                      'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(requested_topping)
    else:
        print('sorry')

print("\n Finished making your pizza.")
'''
'''
#Using the range function
for value in range(0,5):
    print(value)

#Using range to make a list of Numbers
num = list(range(1,6))
print(num)

#**
squares =[]
for value in range(1,11):
    squares.append(value**2)
print(list(squares))

#**
even = list(range(2,11,2))
print(even)
'''
'''
#Simple statistics with a list of numbers
Digit = [1,23,3,44,5,5,5,5,5,5]
print(min(Digit))
print(max(Digit))
print(sum(Digit))
'''
'''
#using int() to accept Numerical Input
height = input("How tall are you, in inches? ")
height = int(height)

if height>= 48:
    print("\n you are tall enough to ride!")
else:
    print("\nYou will be able to ride when you are a little older.")
'''
'''
#A while statement can have  an optional else clause
number = 23
running = True
while running:
    guess = int(input("Enter an integer: "))

    if guess == number:
        print("Congratulation,you guessed it. ")
        running = False
    elif guess < number:
        print("No,it is a little higher than that.")
    else:
        print("No, it is a little lower than that.")
else:
    print("The while loop is over.")

print("Done")
'''
'''
#The break statement(else block is not executed)
while True:
    s = input("Enter something: ")
    if s == 'quit':
        break
    print("Length of  a string is", len(s))
print("Done")
'''
'''
#The continue statement
while True:
    s = input("Enter something: ")
    if s == 'quit':
        break
    if len(s)<3:
        print("Too small")
        continue
    print("Input is of sufficient length")
'''
'''
#List comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)
'''
'''
#Slicing a List
players = ['Abir','Niloy','Anik','Alamin','Rafi']
print(players[0:2])
print(players[:2]) #slice start at the beginning
print(players[2:]) 
print(players[-3:]) #recall negative index
print(players[:-3]) 
'''
'''
#looping through a slice
players = ['Niloy','Mehedi','Shawon','Rudro','Abir']
print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())
'''
'''
#Copying a list
my_foods = ['pizza','cake','icecream','burger']
#friends_food = my_foods[:]

my_foods.append('Momos')

friends_food = my_foods[:]

print("My favourite foods are: ")
print(my_foods)

print("My Friends favourite foods are: ")
print(friends_food)
'''
'''
#tuple
dimensions =(200,50,20,10)
print(dimensions[0])
print(dimensions[1])

#If we want to define a tuple with  one element, you need to include a comma
my_f = (3,)
print(my_f[0])

#Looping through all values in a Tuple
dimensions =(200,50,20,10)
for dimension in dimensions:
    print(dimension)

'''
'''
#Writing over a Tuple
dimensions =(200,50,20,10)
print("orginal dimension: ")
for dimension in dimensions:
    print(dimension)

dimensions =(49,44,393,45)
print("Modified Dimensions: ")
for dimension in dimensions:
    print(dimension)
'''
'''
#Dictionaries
alien = {'color':'green','points':5}
print(alien)
new_point = alien['points']
print("you just earned {new_point} points!")
#adding new key value pairs
alien['x_position'] = 0
alien['y_position'] =25
print(alien)
#Starting with an empty dictionary
alien = {}
alien['color'] = 'green'
alien['points']= 5
print(alien)
#Modifying values in a Dictionary
alien = {'color':'red'}
print(alien['color'])
'''
'''
alien = {'color':'green','points':5}
#removing key-value pair
del alien['points']
print(alien)
'''
'''
#Dictionaries of similar objects
fav_lan = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
for name, language in fav_lan.items():
    print({name.title()},'favourite language is ',{language.title()})
'''
'''
#looping through all the keys in a Dictionary
fav_lan = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
for name in fav_lan.keys():
    print(name.title())

#looping through all the values in a Dictionary
for language in fav_lan.values():
    print(language.title())
'''
'''
#A list of dictionaries

a1 = {'color':'red','point':5}
a2 = {'color':'green','point':10}
a3 = {'color':'blue','point':20}
a = [a1,a2,a3]
#print(a)
for i in a:
    print(i) 
'''
fav_lan = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
}

for name, languages in fav_lan.items():
    print({name.title()},'s fav language are:')
for language in languages:
    print( {language.title()})
