from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk('Maze Solver')
        self.__root.protocol('WM_DELETE_WINDOW', self.close)

        self.__canvas = Canvas(self.__root, bg='white', width=width, height=height)
        self.__canvas.pack()

        self.running = False
    
    def __repr__(self):
        return f"Window(root={self.__root}, canvas={self.__canvas}, running={self.running})"

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True

        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False

    def draw_line(self, line):
        line.draw(self.__canvas)