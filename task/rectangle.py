from dataclasses import dataclass


@dataclass
class Rectangle:
    # my attributes will be coordinates of upper left corner and bottom right corner
    def __init__(self, upper_left_x, upper_left_y, bottom_right_x, bottom_right_y):
        self.upper_left_x = upper_left_x
        self.upper_left_y = upper_left_y
        self.bottom_right_x = bottom_right_x
        self.bottom_right_y = bottom_right_y

    def contains(self, other: "Rectangle") -> bool:
        # Checking if other rectangle is in self rectangle
        if (other.upper_left_x > self.upper_left_x and other.bottom_right_x < self.bottom_right_x and
                other.upper_left_y < self.upper_left_y and other.bottom_right_y > self.bottom_right_y):

            return True
            # Rectangle contains another rectangle
        # Checking if other rectangle contains rectangle
        if (other.upper_left_x < self.upper_left_x and other.bottom_right_x > self.bottom_right_x and
                other.upper_left_y > self.upper_left_y and other.bottom_right_y < self.bottom_right_y):
            return True
            # Another rectangle contains rectangle
        else:
            return False
            # Rectangle does not contain another rectangle

    def intersect(self, other: "Rectangle") -> bool:
        # Checking bottom right coordinates
        if (self.upper_left_x < other.bottom_right_x < self.bottom_right_x or
                self. upper_left_y > other.bottom_right_y > self.bottom_right_y):

            return True
            # Rectangles intersect
        # Checking upper left coordinates
        if (self.bottom_right_x < other.upper_left_x < self.upper_left_x or
                self.bottom_right_y < other.upper_left_y < self.upper_left_y):
            return True
            # Rectangles intersect
        else:
            return False
            # Rectangles do not intersect
