from window import Window
from geometry import Point, Line

def main():
    window = Window(800, 1000)
    line = Line(Point(50, 60), Point(100, 120))
    window.draw_line(line)
    window.wait_for_close()

main()