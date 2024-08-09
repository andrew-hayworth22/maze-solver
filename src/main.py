from window import Window
from geometry import Point, Line
from maze import Cell

def main():
    window = Window(800, 1000)
    cell = Cell(Point(10, 10), Point(60, 60), window, True, False, True, True)
    cell2 = Cell(Point(60, 10), Point(120, 60), window, False, False, True, True)
    cell.draw()
    cell2.draw()
    window.wait_for_close()

main()