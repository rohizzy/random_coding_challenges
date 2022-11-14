class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, newWidth):
        self.width = newWidth

    def set_height(self, newHeight):
        self.height = newHeight

    def get_area(self):
        return self.height + self.width

    def get_perimeter(self):
        return self.height*2 + self.width*2

    def get_diagonal(self):
        return (self.height**2 + self.width**2)**0.5

    def get_picture(self):
        out = ''
        for row in range(self.height):
            out += '*'*self.width + '\n'
        return out

    def get_amount_inside(self, shape):
        if self.width > shape.width and self.height > shape.height:
            wide = self.width // shape.width
            tall = self.height // shape.height

        if wide == 0 and tall > 0:
            return tall
        elif tall == 0 and wide > 0:
            return wide
        elif wide > 0 and tall > 0:
            return wide * tall
        else:
            return 0

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __repr__(self):
        return f'Square(side={self.width})'

    def set_width(self, newWidth):
        self.width = newWidth
        self.height = newWidth

    def set_height(self, newHeight):
        self.height = newHeight
        self.width = newHeight

rect1 = Rectangle(5,10)
rect2 = Square(2)

print(rect1.get_picture())
print(rect2.get_picture())
print(rect1.get_amount_inside(rect2))