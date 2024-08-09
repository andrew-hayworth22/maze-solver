from geometry import Point, Line
from window import Window

class Cell:
    def __init__(self, top_left_point: Point, bottom_right_point: Point, window: Window, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.__top_left_point = top_left_point
        self.__bottom_right_point = bottom_right_point
        self.center_point = Point((top_left_point.x + bottom_right_point.x) / 2, (top_left_point.y + bottom_right_point.y) / 2)
        self.__window = window
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
    
    def draw(self):
        if self.has_left_wall:
            self.__window.draw_line(Line(self.__top_left_point, Point(self.__top_left_point.x, self.__bottom_right_point.y)))
        if self.has_right_wall:
            self.__window.draw_line(Line(self.__bottom_right_point, Point(self.__bottom_right_point.x, self.__top_left_point.y)))
        if self.has_top_wall:
            self.__window.draw_line(Line(self.__top_left_point, Point(self.__bottom_right_point.x, self.__top_left_point.y)))
        if self.has_bottom_wall:
            self.__window.draw_line(Line(self.__bottom_right_point, Point(self.__top_left_point.x, self.__bottom_right_point.y)))

    def draw_move(self, to_cell, undo = False):
        color = "red"
        if undo:
            color = "gray"

        line = Line(self.center_point, to_cell.center_point, fill_color=color)
        self.__window.draw_line(line)