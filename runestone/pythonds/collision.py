class Point:
    """Point class for representing and manipulating coordinates osn a plane."""

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

class Rectangle:
    """Rectangle class (left-bottom Point(x,y), width W, height H)."""

    def __init__(self, initP, initW, initH):
        self.position = initP
        self.width = initW
        self.height = initH

    def corners(self):
        '''Returns dict: bottom-left, bottom-right, top-left, top-right].'''

        corners = {}
        corners["bottom-left"] = self.position
        corners["bottom-right"] = Point(self.position.x+self.width, self.position.y)
        corners["top-left"] = Point(self.position.x, self.position.y+self.height)
        corners["top-right"] = Point(self.position.x+self.width, self.position.y+self.height)
        return corners

    def doCollide(self, other):
        selfCorners = self.corners();
        otherCorners = other.corners();

        # if one rectangle is above the other:
        if (selfCorners["bottom-left"].y >= otherCorners["top-right"].y or\
        otherCorners["bottom-left"].y >= selfCorners["top-right"].y):
            return False

        # if one rectangle is to the right side of ther other:
        if (selfCorners["bottom-left"].x >= otherCorners["top-right"].x or\
        otherCorners["bottom-left"].x >= selfCorners["top-right"].x):
            return False

        return True

# for testing 'collision()':
r1 = Rectangle(Point(0, 0), 5, 10)

r2 = Rectangle(Point(5, 5), 5, 5)
print(r1.doCollide(r2))

r3 = Rectangle(Point(4, 4), 5, 5)
print(r2.doCollide(r3))

r4 = Rectangle(Point(9, 5), 5, 5)
print(r3.doCollide(r4))
