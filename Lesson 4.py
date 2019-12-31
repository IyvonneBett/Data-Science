# OOP object oriented programming
# real world object has states and behaviours
# vehicle : states: age, colour, mileage ,weight, type, size, make
# behaviours : what does it do? moves, carries, sounds
# what are classes? can contain states and behaviours


class Triangle: # define the states below

    def __init__(self, base, height, colour): # define the states/properties/attributes
        # we add these states to self
        self.base = base
        self.height = height
        self.colour = colour

     # do behaviors/functions
    def find_area(self): # self knows the base height and colour
        area = 0.5 * self.base * self.height
        print('The area is', area)
        print('The triangle is', self.colour)

# create a real object
object = Triangle(base= 5, height=4, colour= 'blue')
object.find_area()












