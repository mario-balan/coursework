import test

# doing this as an exercise, even though I'm not sure if there are
# good reasons for using getters and setters in Python

class Point:
    """Point class for representing and manipulating coordinates in a plane."""

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)


class Rectangle:
    """Rectangle class (left-bottom Point(x,y), width W, height H)"""

    def __init__(self, initP, initW, initH):
        self.position = initP
        self.width = initW
        self.height = initH

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def __str__(self):
        return "position:" + str(self.position) + "; width=" + str(self.width)\
        + "; height=" + str(self.height)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height

    def transpose(self):
        tmp = self.height
        self.height = self.width
        self.width = tmp

# breaking up the conditions (also: python has a ternary conditional):

    def contains(self, point):
        if (point.x < self.position.x and point.y < self.position.y):
            return False
        else:
            return True if point.x < self.width and point.y < self.height else False

# using the pythagorean way:
    def diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

#instantiates a Point:
p = Point(4, 5)
#instantiates 2x2 a Rectangle from previous point:
r = Rectangle (p, 6, 5)
print(r)
r.transpose()
print(r)
print(r.area())
print(r.perimeter())

# for testing 'contains()':
r = Rectangle(Point(0, 0), 10, 5)
print(r)
print(r.contains(Point(0, 0)))
print(r.contains(Point(3, 3)))
print(r.contains(Point(3, 7)))
print(r.contains(Point(3, 5)))
print(r.contains(Point(3, 4.99999)))
print(r.contains(Point(-3, -3)))

#diagonal for the same rectangle:
print(r.diagonal())
