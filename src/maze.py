from time import sleep
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


class Maze:
    def __init__(self, window: Window, top_left = Point(10, 10), num_rows = 10, num_cols = 10, cell_size_x = 50, cell_size_y = 50):
        self.__window = window
        self.__top_left = top_left
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y

        self.__create_cells()

    def __create_cells(self):
        self.__cells = []

        start_x = self.__top_left.x
        end_x = self.__top_left.x + (self.__cell_size_x * self.__num_rows)
        curr_x = 0

        start_y = self.__top_left.y
        end_y = self.__top_left.y + (self.__cell_size_y * self.__num_cols)

        for x in range(start_x, end_x, self.__cell_size_x):
            self.__cells.append([])
            for y in range(start_y, end_y, self.__cell_size_y):
                top_left = Point(x, y)
                bottom_right = Point(x + self.__cell_size_x, y + self.__cell_size_y)
                cell = Cell(top_left, bottom_right, self.__window)
                self.__cells[curr_x].append(cell)
            curr_x += 1

        col_idx = 0
        for col in self.__cells:
            for row in range(len(col)):
                self.__draw_cell(row, col_idx)
            col_idx += 1

    def __draw_cell(self, row, col):
        self.__cells[row][col].draw()
        self.__animate()
    
    def __animate(self):
        self.__window.redraw()
        sleep(.05)