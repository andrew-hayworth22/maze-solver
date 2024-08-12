from window import Window
from geometry import Point, Line
from maze import Cell, Maze


def main():
    # Update these values to configure your maze
    rows = 10
    columns = 10

    window = Window((rows * 50)+20, (columns * 50)+20)

    maze = Maze(window=window, num_rows=rows, num_cols=columns)
    maze.solve()

    window.wait_for_close()

main()