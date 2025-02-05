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
