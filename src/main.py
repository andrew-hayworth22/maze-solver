from window import Window
from geometry import Point, Line
from maze import Cell, Maze, DEFAULT_ROWS, DEFAULT_COLS, DEFAULT_CELL_SIZE_X, DEFAULT_CELL_SIZE_Y


def main():
    # Update these values to configure your maze
    rows = DEFAULT_ROWS
    columns = DEFAULT_COLS
    cell_size_x = DEFAULT_CELL_SIZE_X
    cell_size_y = DEFAULT_CELL_SIZE_Y

    window = Window((rows * 50)+20, (columns * 50)+20)

    maze = Maze(window=window, num_rows=rows, num_cols=columns, cell_size_x=cell_size_x, cell_size_y=cell_size_y)
    maze.solve()

    window.wait_for_close()

main()