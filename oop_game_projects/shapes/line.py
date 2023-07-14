class Line:
    def __init__(self, coor1, coor2) -> None:
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        dis = ((y2 -y1)**2 - (x2 - x1)**2)**0.5
        print("The distance of the line is {}".format(dis))
        return dis

    
    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        sl = (y2 - y1) / (x2 - x1)
        print("The slope of the line is {}".format(sl))

        return sl
