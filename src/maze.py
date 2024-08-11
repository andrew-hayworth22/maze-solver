import random
from time import sleep
from geometry import Point, Line
from window import Window

class Cell:
    def __init__(self, top_left_point: Point, bottom_right_point: Point, window: Window = None, has_left_wall = True, has_right_wall = True, has_top_wall = True, has_bottom_wall = True):
        self._top_left_point = top_left_point
        self._bottom_right_point = bottom_right_point
        self._window = window

        self.center_point = Point((top_left_point.x + bottom_right_point.x) / 2, (top_left_point.y + bottom_right_point.y) / 2)
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.visited = False
    
    def __repr__(self):
        return f"Cell(top_left_point={self._top_left_point}, bottom_right_point={self._bottom_right_point}, left_wall={self.has_left_wall}, right={self.has_right_wall}, top={self.has_top_wall}, bottom={self.has_bottom_wall})"
    
    def draw(self):
        if self._window is None:
            return

        line_color = "black"
        bg_color = "white"

        self._window.draw_line(Line(self._top_left_point, Point(self._top_left_point.x, self._bottom_right_point.y), fill_color=line_color if self.has_left_wall else bg_color))
        self._window.draw_line(Line(self._bottom_right_point, Point(self._bottom_right_point.x, self._top_left_point.y), fill_color=line_color if self.has_right_wall else bg_color))
        self._window.draw_line(Line(self._top_left_point, Point(self._bottom_right_point.x, self._top_left_point.y), fill_color=line_color if self.has_top_wall else bg_color))
        self._window.draw_line(Line(self._bottom_right_point, Point(self._top_left_point.x, self._bottom_right_point.y), fill_color=line_color if self.has_bottom_wall else bg_color))

    def draw_move(self, to_cell, undo = False):
        color = "red"
        if undo:
            color = "gray"

        line = Line(self.center_point, to_cell.center_point, fill_color=color)
        self._window.draw_line(line)


class Maze:
    def __init__(self, window: Window = None, seed = None, top_left = Point(10, 10), num_rows = 10, num_cols = 10, cell_size_x = 50, cell_size_y = 50):
        self._window = window
        self._top_left = top_left
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        if seed is not None:
            random.seed(seed)

        self._cells = []
        self.__create_cells()

    def __repr__(self):
        return f"Maze(window={self._window}, top_left={self._top_left}, num_rows={self._num_rows}, num_cols={self._num_cols}, cell_size(x,y)={self._cell_size_x},{self._cell_size_y}"

    def __create_cells(self):
        start_x = self._top_left.x
        end_x = self._top_left.x + (self._cell_size_x * self._num_cols)
        curr_x = 0

        start_y = self._top_left.y
        end_y = self._top_left.y + (self._cell_size_y * self._num_rows)

        for x in range(start_x, end_x, self._cell_size_x):
            self._cells.append([])
            for y in range(start_y, end_y, self._cell_size_y):
                top_left = Point(x, y)
                bottom_right = Point(x + self._cell_size_x, y + self._cell_size_y)
                cell = Cell(top_left, bottom_right, self._window)
                self._cells[curr_x].append(cell)
            curr_x += 1
        
        col_idx = 0
        for col in self._cells:
            for row in range(len(col)):
                self.__draw_cell(row, col_idx)
            col_idx += 1
        
        self.__break_entrance_and_exit()
        self.__break_walls(0, 0)
        self.__reset_visited()

    def __draw_cell(self, row, col):
        self._cells[col][row].draw()
        self.__animate()
    
    def __animate(self):
        if self._window is None:
            return

        self._window.redraw()
        sleep(.05)
    
    def __break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self.__draw_cell(0, 0)

        self._cells[self._num_cols-1][self._num_rows-1].has_right_wall = False
        self.__draw_cell(self._num_rows-1, self._num_cols-1)
    
    def __break_walls(self, col, row):
        self._cells[col][row].visited = True
        self.__draw_cell(row, col)

        directions = [('top', 0, -1), ('right', 1, 0), ('bottom', 0, 1), ('left', -1, 0)]
        random.shuffle(directions)

        for direction in directions:
            direction_name = direction[0]
            next_col = col + direction[1]
            next_row = row + direction[2]

            if 0 <= next_col < self._num_cols and 0 <= next_row < self._num_rows and not self._cells[next_col][next_row].visited:
                if direction_name == 'top':
                    self._cells[col][row].has_top_wall = False
                    self._cells[next_col][next_row].has_bottom_wall = False
                elif direction_name == 'right':
                    self._cells[col][row].has_right_wall = False
                    self._cells[next_col][next_row].has_left_wall= False
                elif direction_name == 'bottom':
                    self._cells[col][row].has_bottom_wall = False
                    self._cells[next_col][next_row].has_top_wall= False
                else:
                    self._cells[col][row].has_left_wall = False
                    self._cells[next_col][next_row].has_right_wall= False

                self.__break_walls(next_col, next_row)

    def __reset_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False