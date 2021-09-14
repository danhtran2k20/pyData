class Rectangle:
    def __init__(self, width, height):
        """Create Rectangle with width and height"""
        self.height = height
        self.width = width

    def __str__(self):
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        strPicture = ""
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        for _ in range(self.height):
            for _ in range(self.width):
                strPicture += "*"
            strPicture += "\n"
        return strPicture

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)


class Square(Rectangle):
    def __init__(self, side):
        """Create Rectangle with width and height"""
        self.side = self.height = self.width = side

    def __str__(self):
        return f"{self.__class__.__name__}(side={self.side})"

    def set_side(self, side):
        self.side = self.height = self.width = side

    def set_height(self, side):
        self.set_side(side)

    def set_width(self, side):
        self.set_side(side)



rect = Rectangle(3, 6)
sq = Square(9)

# rect.set_width(7)
# rect.set_height(8)
actual = str(rect)
print("str(rect):", str(rect))
# expected = "Rectangle(width=7, height=8)"
# assertEqual(actual, expected, 'Expected string representation of rectangle after setting new values to be "Rectangle(width=7, height=8)"')
sq.set_side(2)
print("sq.set_side(2)")
actual = str(sq)
print(actual)
# expected = "Square(side=2)"
# assertEqual(actual, expected, 'Expected string representation of square after setting new values to be "Square(side=2)"')
sq.set_width(4)
print("sq.set_width(4)")
actual = str(sq)
print(actual)
# expected = "Square(side=4)"
# assertEqual(actual, expected, 'Expected string representation of square after setting width to be "Square(side=4)"')
