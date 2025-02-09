#global vs local scope pt 1
def square(x):
    '''This function returns the square of a number'''
    new_value=x**2
    return new_value
print(square(3))

print(square(5)) 

lexus = 10
def square4(x):
    '''This function returns the square of a number'''
    global lexus
    lexus = lexus **2
    return lexus
print(square4(4))

#nested functions: functions defined inside other functions
def mod2plus5(x1, x2, x3):
    '''This function returns the remainder plus 5 of three variables'''
    new_x1 = x1%2 + 5
    new_x2 = x2%2 + 5
    new_x3 = x3%2 + 5
    return new_x1, new_x2, new_x3
print(mod2plus5(2,3,4))

#lets now solve the problem using nested functionsgit
def mod2plus5_1(x1,x2,x3):
    '''this fuction returns the remainder plus 5 of three variables'''
    def inner(x):
        '''this function returns the reminder plus 5 of a single variable which is x'''
        return x%2 + 5
    return (inner(x1), inner(x2), inner(x3))
print(mod2plus5_1(6,7,8))