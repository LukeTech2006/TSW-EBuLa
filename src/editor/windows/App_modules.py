# import tkinter
import tkinter.messagebox
import customtkinter

from components.sidebar import Sidebar
from components.line_map_mod import LineMapMod

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("EBULA Editor - Map Modules")
        self.geometry(f"{1250}x{750}")

        # configure grid layout (4x4)
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure((2, 3), weight=0)
        # self.grid_rowconfigure((0, 1, 2), weight=2)
        self.grid_columnconfigure((0,1,2,3,4,5), weight=0)
        self.grid_rowconfigure((0,1,2,3,4,5), weight=0)

        # self.sidebar = Sidebar(self,width=500)

        # create checkbox and switch frame
        # self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        # self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        # self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
        # self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
        # self.checkbox_3 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="n")

        # set default values
        # self.checkbox_3.configure(state="disabled")
        # self.checkbox_1.select()

        # self.test = customtkinter.CTkScrollableFrame(self)
        # self.test.grid(row=1, column=1, pady=20, padx=20)


        self.line = LineMapMod(self,15)
        self.line.grid(row=1, column=1, pady=10, padx=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()