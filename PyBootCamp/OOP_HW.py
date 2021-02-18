class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        print(pow(pow(self.coor2[1] - self.coor1[1], 2) + pow(self.coor2[0] - self.coor1[0], 2), 0.5))
        # tuple-unpacking
        # x1,y1 = self.coor1
        # x2,y2 = self.coor2
        # print(((y2-y1)**2+(x2-x1)**2)**0.5)

    def slope(self):
        print((self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0]))
        # tuple-unpacking
        # x1,y1 = self.coor1
        # x2,y2 = self.coor2
        # print((y2-y1)/(x2-x1))


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
li.distance()
li.slope()


class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.raidus = radius

    def volume(self):
        print((22 / 7) * self.raidus * self.raidus * self.height)

    def surface(self):
        print((2 * (22 / 7) * self.raidus * self.height) + (2 * (22 / 7) * self.raidus * self.raidus))


c = Cylinder(2, 3)
c.volume()
c.surface()
