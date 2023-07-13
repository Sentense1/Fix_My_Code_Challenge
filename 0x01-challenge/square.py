#!/usr/bin/python3

class Square():
    """
    A class representing a square.
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """
        Initializes a Square object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """
        Calculates the area of the square.

        Returns:
            The area of the square.
        """
        return self.width * self.height

    def Perimeter_Of_My_Square(self):
        """
        Calculates the perimeter of the square.

        Returns:
            The perimeter of the square.
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            The string representation of the square.
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.Perimeter_Of_My_Square())
