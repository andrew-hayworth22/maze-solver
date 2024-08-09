from window import Window
from geometry import Point, Line
from maze import Cell

def main():
    window = Window(800, 1000)
    cell = Cell(Point(10, 10), Point(60, 60), window, True, False, True, True)
    cell2 = Cell(Point(60, 10), Point(120, 60), window, False, True, True, False)
    cell3 = Cell(Point(60, 60), Point(120, 120), window, True, True, False, False)
    cell.draw()
    cell2.draw()
    cell3.draw()
    cell.draw_move(cell2)
    cell2.draw_move(cell3)
    window.wait_for_close()

main()