import customtkinter

def load_poi() -> list:
    # TODO loads data from the file to use it in the dropdown boxes
    pass

poi = load_poi()    # obj that holds all current poi's


class PoiEntry(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Set elements
        self.input = customtkinter.CTkComboBox(self, width=200, values=("1","2","3","4"))
        self.input.grid(row=0, column=0)
        self.add = customtkinter.CTkButton(self, width=1, height=25, corner_radius=200, text="+")
        self.add.grid(row=0, column=1, padx=(10,5), ipadx=0, ipady=0)
        # self.inputDialog = customtkinter.CTkInputDialog(title="Add Bestriebstelle", text="Füge eine Bestriebstelle hinzu.")

        # Set Defaults

        print("init PoiEntry")

    def save_poi():
        # TODO saves data to a file to use it again when the programm is reopened
        pass

    def refresh_poi():
        # TODO refresh current obj to react to the current changes
        pass