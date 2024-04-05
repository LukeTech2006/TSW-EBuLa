# import tkinter
import tkinter.messagebox
import customtkinter

from App_main import App as main

class App(main):
    def __init__(self):
        super().__init__()
        

if __name__ == "__main__":
    app = App()
    app.mainloop()