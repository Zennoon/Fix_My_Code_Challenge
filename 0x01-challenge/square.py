#!/usr/bin/python3
"""
Contains a square class
"""


class Square():
    """
    Represents a real-life Square (but doesn't necessitate all sides 4 sides
    equal)
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initializes a new instance"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Calculates area"""
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """Calculates perimeter"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Informal string representation of the instance"""
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
