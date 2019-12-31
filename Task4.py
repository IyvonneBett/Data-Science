# states height, width,colour
# behavior: perimeter, area

class Square:
    def __init__(self, height, width, colour):
        self.height = height
        self.width = width
        self.colour = colour

    def find_perimeter(self):
        total = 2*self.height + 2*self.width
        print('The perimeter is', total)

    def find_area(self):
        area = self.height * self.width
        print('The area is', area)
        print('The square is',self.colour, 'in colour')


object = Square(height=4, width=3 ,colour='red')
object.find_perimeter()
object.find_area()



