from window import Window
from geometry import Point, Line
from maze import Cell, Maze

def main():
    window = Window(520, 520)

    maze = Maze(window=window)
    maze.solve()

    window.wait_for_close()

main()