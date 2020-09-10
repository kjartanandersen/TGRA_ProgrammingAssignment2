

# class vector holds information about a vector
class Vector:
    def __init__(self, x = 1, y = 1):
        self.x = x                      # x variable of vector
        self.y = y                      # y variable of vector
    
    # overloader for + sign
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # overloader for - sign
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # overloader for * sign
    def __mul__(self, other):
        if isinstance(other, float):
            return Vector(self.x * other, self.y * other)
        return Vector(self.x * other, self.y * other)

# class point holds information about a point
class Point:
    def __init__(self, x = 1, y = 1):
        self.x = x                      # x coordinate of point
        self.y = y                      # y coordiante of point

    # overloader for + sign
    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    # overloader for - sign
    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y

    # overloader for * sign
    def __mul__(self, other):
        return Point(self.x + other.x, self.y + other.y)