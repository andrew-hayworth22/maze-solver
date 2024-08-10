import unittest
from geometry import Point
from maze import Maze

class TestMaze(unittest.TestCase):
    def test_init_point_default(self):
        default_point = Point(10, 10)
        maze = Maze()

        self.assertEqual(default_point, maze._top_left)

    def test_init_point(self):
        point = Point(50, 50)
        maze = Maze(top_left=point)

        self.assertEqual(point, maze._top_left)

    def test_init_cells_default(self):
        default_rows, default_columns = 10, 10
        maze = Maze()

        self.assertEqual(default_rows, maze._num_rows)
        self.assertEqual(default_rows, len(maze._cells[0]))
        self.assertEqual(default_columns, maze._num_cols)
        self.assertEqual(default_columns, len(maze._cells))
    
    def test_init_cells_square(self):
        rows, columns = 20, 20
        maze = Maze(num_rows=rows, num_cols=columns)

        self.assertEqual(rows, maze._num_rows)
        self.assertEqual(rows, len(maze._cells[0]))
        self.assertEqual(columns, maze._num_cols)
        self.assertEqual(columns, len(maze._cells))

    def test_init_cells_rectangle(self):
        rows, columns = 30, 20
        maze = Maze(num_rows=rows, num_cols=columns)

        self.assertEqual(rows, maze._num_rows)
        self.assertEqual(rows, len(maze._cells[0]))
        self.assertEqual(columns, maze._num_cols)
        self.assertEqual(columns, len(maze._cells))

    def test_init_cell_size_default(self):
        default_cell_x, default_cell_y = 50, 50
        maze = Maze(cell_size_x=default_cell_x, cell_size_y=default_cell_y)

        self.assertEqual(default_cell_x, maze._cell_size_x)
        self.assertEqual(default_cell_y, maze._cell_size_y)

        cell_width = maze._cells[0][0]._bottom_right_point.x - maze._cells[0][0]._top_left_point.x
        cell_height = maze._cells[0][0]._bottom_right_point.y - maze._cells[0][0]._top_left_point.y
        self.assertEqual(default_cell_x, cell_width)
        self.assertEqual(default_cell_y, cell_height)

    def test_init_cell_size_square(self):
        cell_x, cell_y = 100, 100
        maze = Maze(cell_size_x=cell_x, cell_size_y=cell_y)

        self.assertEqual(cell_x, maze._cell_size_x)
        self.assertEqual(cell_y, maze._cell_size_y)

        cell_width = maze._cells[0][0]._bottom_right_point.x - maze._cells[0][0]._top_left_point.x
        cell_height = maze._cells[0][0]._bottom_right_point.y - maze._cells[0][0]._top_left_point.y
        self.assertEqual(cell_x, cell_width)
        self.assertEqual(cell_y, cell_height)

    def test_init_cell_size_rect(self):
        cell_x, cell_y = 150, 50
        maze = Maze(cell_size_x=cell_x, cell_size_y=cell_y)

        self.assertEqual(cell_x, maze._cell_size_x)
        self.assertEqual(cell_y, maze._cell_size_y)

        cell_width = maze._cells[0][0]._bottom_right_point.x - maze._cells[0][0]._top_left_point.x
        cell_height = maze._cells[0][0]._bottom_right_point.y - maze._cells[0][0]._top_left_point.y
        self.assertEqual(cell_x, cell_width)
        self.assertEqual(cell_y, cell_height)