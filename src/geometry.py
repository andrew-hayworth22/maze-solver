

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

class Line:
    def __init__(self, point_1, point_2, width=2, fill_color="black"):
        self.point_1 = point_1
        self.point_2 = point_2
        self.width = width
        self.fill_color = fill_color
    
    def __repr__(self):
        return f"Line(point_1={self.point_1}, point_2={self.point_2}, width={self.width}, fill_color={self.fill_color}"

    def draw(self, canvas):
        canvas.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=self.fill_color, width=self.width)