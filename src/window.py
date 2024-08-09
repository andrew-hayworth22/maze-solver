from tkinter import Tk, BOTH, Canvas

class WindowItr:
    def redraw(self):
        pass

    def wait_for_close(self):
        pass

    def close(self):
        pass

    def draw_line(self, line):
        pass

class Window(WindowItr):
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

class WindowTest(WindowItr):
    def redraw(self):
        return super().redraw()
    
    def wait_for_close(self):
        return super().wait_for_close()
    
    def close(self):
        return super().close()
    
    def draw_line(self, line):
        return super().draw_line(line)