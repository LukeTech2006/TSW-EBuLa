# import tkinter
import tkinter.messagebox
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("EBULA Editor - Map Modules")
        self.geometry(f"{1250}x{750}")

        # # configure grid layout (4x4)
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure((2, 3), weight=0)
        # self.grid_rowconfigure((1, 2), weight=2)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.frame_main = customtkinter.CTkScrollableFrame(self, )

        # self.test = customtkinter.CTkScrollableFrame(self)
        # self.test.grid(row=1, column=1, pady=20, padx=20)

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")
        print(list(self.test.children.keys()).count())
        # print(list(self.test.children.keys()) list(self.test.children.keys()).count())
        self.test.children.pop()
    
    def add_poi(self):
        print("add_poi")
        self.test2 = customtkinter.CTkLabel(self.test, text="test")
        self.test2.pack()

        self.test3 = customtkinter.CTkButton(self.test, text="del")
        self.test3.pack()
        # self.test3
        self.test3.configure(command= lambda: self.test_del(self.test3,self.test2))

        print(type(self.test.children))
        print(self.test.children)
        pass

    def test_del(self, del1:customtkinter.CTkBaseClass, del2:customtkinter.CTkBaseClass):
        print("test del")
        del1.destroy()
        del2.destroy()
        print(self.test.children)

if __name__ == "__main__":
    app = App()
    app.mainloop()