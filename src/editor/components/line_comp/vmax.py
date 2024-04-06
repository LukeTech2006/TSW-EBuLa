import customtkinter

class VmaxEntry(customtkinter.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, placeholder_text="Vmax", width=75, **kwargs)

        # Set elements
        # self.entry = customtkinter.CTkEntry(master, corner_radius=5,placeholder_text="test")

        # Set Defaults

        print("init VmaxEntry")