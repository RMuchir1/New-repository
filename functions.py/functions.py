print("this is my first function in python")

def square():
    value_one = 4**2
    print (value_one)
square()

def devide():
    value_two = 4/2
    print (value_two)
devide()

#funtion parameters
#return a value from a function using the return key word


def square_2(value):
    new_value = value**2
    return new_value
square_2(15)
print(square_2(15))

#doc strings: used to document what a function/describe what the fuction does

def devide_by_six (value):
    '''This function returns the value of a number devided by six'''
    devide_by_six = value/6
    return devide_by_six

#multiple parameters and return values
def multiply_by_hundred (a,b,c):
    '''This function returns the value of two numbers multiplied by 100'''
    value_one = a*100
    value_two = b*100
    value_three = c*100
    return value_one, value_two, value_three
predictions = multiply_by_hundred(10, 20, 30)
print(predictions)

#returning multiple values
def raise_to(valuex, valuey):
    '''This function raises the valuex to the power of valuey and vice versa'''
    trial1 = valuex**valuey
    trial2 = valuey**valuex
    new_tiple = (trial1, trial2)
    return new_tiple
results = raise_to(2, 3)
print(results)
print(type(results))

    
#tuple unpacking: unpacking the values of a tuple into variables and accessing them
even_numbers = (2, 4, 6, 8, 10)
a, b, c, d, e = even_numbers

#scope and user defied functions:not all variables are accessible from all parts of a program
#scope: part of the program where an object or name may be accessible
#global scope: defined in the main body of a script
#local scope: defined inside a function
#built-in scope: names in the pre-defined built-ins module
#variables: names that are used to represent a value or object
#global variables: defined in the main body of a script
#local variables: defined inside a function








