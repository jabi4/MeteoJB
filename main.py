from tkinter import Tk
from screens.mainSreen import MainScreen

class App(Tk):

    def __init__(self):
        super().__init__()
        self.title("Meteo stanica Jasmin")
        self.geometry("400x400")
        self._createScreen()

    def _createScreen(self):
        MainScreen(self)


if __name__ == '__main__':
    app = App()
    app.mainloop()

