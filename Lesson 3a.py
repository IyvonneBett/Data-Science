# function/methods..Object Oriented programming
# functions are a block of code performing some task
# makes programming easy to understand especially large programs
# used in OOP
# they break your program into small parts
# before doing a faction have two empty lines


def welcome(): # welcome is the name of the function
    print('Welcome to python function')
    print('Thank you')



def adding():
    x = 78
    y = 56
    answer = x + y
    print('Answer is', answer)

# write a python function to add 5 subjects, find total and average


def primary():
    math = 90
    english = 99
    kiswahili = 85
    social = 87
    science = 98
    total = math + english + kiswahili + social + science
    average = total/5
    print('Total marks', total)
    print('Average is', average)


def body_mass_index():
    weight = 54
    height = 1.68
    bmi = weight/(height**2) # or (height*height)
    print('Your bmi is', bmi)
    if bmi <= 17.5:
        print('Underweight')

    elif bmi > 17.5 and bmi <= 22.5:
        print('Normal')

    else:
        print('Overweight')


def looping():
    for p in range(1, 11, +1):
        print('For loop', p)




# call your function
looping()
body_mass_index()


