# A python programme designed to get the sum of two numbers
print(4+5)
print(11+5)
# program to get the difference between two numbers
print(15-5)
# program to carry out modula operations
a=10
b=3
print(a%b)
# create the student_age variable with a value of their age
student_age = 20
print (student_age)
print(type(student_age))
# integers
student_age = 20
print(student_age)
print(type(student_age))
# float
student_age = 20.5
print(type(student_age))
# string
student_name = "ryan"
print(student_name)
print(type(student_name))
# boolean:true or false values which are case sensitive
present_studentA = True
present_studentB = False
print(present_studentA)
print(type(present_studentA))
print(present_studentB)
print(type(present_studentB))
# list
c= a+b
d= (a%b)
print(student_age,d)
print (c+d)
#methods: a function that is only available to a specific data type 
my_university = "University of Nairobi"
# replace some words in the string
# synatax: .replace("word to replace", "new word")
print(my_university.replace("Nairobi", "Warwick"))
print(my_university)
#change case
my_sirname = "Kamau"
print(my_sirname.upper())
print(my_sirname.lower())
#split
my_course = "Data Science"
print(my_course.split())
print(my_course.split("a"))
#join
my_course = "Data Science"
print(" ".join(my_course))
print(" ".join(my_course.split()))
# creating an multi-line string
my_sentence = '''I am a student at the University of Nairobi
I can swim and code using python
i Have a passion for data science'''
print(my_sentence.split)
print(my_sentence.split("and"))
#lists
# a list is a collection of items
item0 = "liam"
item1 = "leo"
item2 = "kennedy"
item3 = "kamau"
item4 = "keith"
item5 = "wayne"
item6 = "james"
print(item1), print(item2), print(item3)
# create a list
my_students = ["liam", "leo", "kennedy", "kamau", "keith", "wayne", "james"]
print(my_students)
print(my_students[0], my_students[2], my_students[4])
# change an item in the list
my_students[0] = "michael"
print(my_students)
#dictionaries: a collection of items that have a key and a value
# create a dictionary
person = {"name": "ryan", "age": 20, "occupation": "student"}
print(person)
student_name = [my_students]
student_age = [20, 21, 22, 23, 24, 25, 26]

#sets: a collection of unique items
# create a set
student_ethnicity = {"caucasian", "african", "asian", "hispanic", "latino", "middle eastern"}
print("stedent_ehtnicity")
# add an item to the set
student_ethnicity.add("samoan")
print(student_ethnicity)
# remove an item from the set
student_ethnicity.remove("african")
#converting a list to a set
Student_ethnicity_set = set(my_students)
print("student_ethnicity_set")
#tuples: a collection of items that are ordered and unchangeable
# create a tuple
class_locations = ("Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret")
print(class_locations)
# access an item in the tuple
print(class_locations[4])
#replace an item in the tuple
# Assignment: write a summary of data structures 
# (lists, dictionaries, sets and tuples) in python
# focussing on their immutaability, mutability and
#compare if two is equal two three
print(2==3)
print("michael" < "ryan")
Sales_target = 350
sales_made = 300
# compare sales made to the sales target
#if sales made is greater than or equal to the sales target
if sales_made > Sales_target:
    print("You have met your target")
elif sales_made < Sales_target:
    print("You have not met your target")
# create a new list
prices = [90.9, 30.3, 80.4, 3.3, 0.2]
print(prices[2]>prices[0])
#for value in sequence: action
for price in prices:print(price)
if price>10:
    print("price is greater than 10")
elif price<100:
    print("price is less than 100")
elif price>5:
    print("price is greater than 5")  
for price in range (6,14):
    print(price)
#bulding a counter
attendance = 0
for i in range(6,14):
    attendance += 1
print(attendance)
stock = 10
number_of_purchases = 0
while number_of_purchases < stock:
    number_of_purchases += 1
    print(stock - number_of_purchases)
#create a new list
names = ["liam", "leo", "kennedy", "kamau", "keith", "wayne", "james"]
names.append("coventry")
print(names)
if "coventry" not in names:
    print("coventry is not in the list") 
    if "coventry" not in names:
        print("coventry is not in the list")
    else:
        print("coventry is in the list")        
#create dictionary

expensive_product = []

shopping_list = {"apples": 20.5, "bananas": 24, "oranges": 7, "grapes": 30, "mangoes": 6, "pears": 8}
for key, val in shopping_list.items():
    if val>=20:
        expensive_product.append(key)
print(expensive_product)

#covert dictionary files to a list
items_in_shopping_list = list(shopping_list.items())
for items in items_in_shopping_list:
    print(items)
#intialize list to store expensive products
expensive_products = []
#loop through the dictionary
while shopping_list:
    #create a list of keys to avoid modifying the dictionary after interaction
    keys_to_remove=[]
    for key, val in shopping_list.items():
        if val>=20:
            expensive_products.append(key)
            keys_to_remove.append(key)
    #remove the keys after the iteration
    for key in keys_to_remove:
        shopping_list.pop(key)
#move to the next item
print(expensive_products)
# create new list
items_2 = {33.9 , 2.4 , 4.98 , 55 , 2 , 34}
#truncate the longer list to match the shorter list
min_length = min(len(keys), len(values))
keys = keys[:min_length]
values = values[:min_length]
#using zip() to combine keys and values
keys = list(shopping_list.keys())
values = list(items_2)
combined = zip(keys,values)
print(list(combined))











    

