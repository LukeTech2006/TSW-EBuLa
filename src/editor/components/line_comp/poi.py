import customtkinter

def load_poi() -> list:
    # TODO loads data from the file to use it in the dropdown boxes
    pass

poi = load_poi()    # obj that holds all current poi's


class PoiEntry(customtkinter.CTkComboBox):
    def __init__(self, master, **kwargs):
        self.frame = super().__init__(master, values=("1","2","3","4"), width=200, **kwargs)

        # Set elements
        # self.frame = customtkinter.CTkFrame(master)
        # self.input = customtkinter.CTkComboBox(self.frame, corner_radius=5, values=("1","2","3","4"))
        # self.inputDialog = customtkinter.CTkInputDialog(title="Add Bestriebstelle", text="Füge eine Bestriebstelle hinzu.")
        # self.input = customtkinter.CTkEntry(master, corner_radius=5,placeholder_text="Betriebstelle")

        # Set Defaults

        print("init PoiEntry")

    def save_poi():
        # TODO saves data to a file to use it again when the programm is reopened
        pass

    def refresh_poi():
        # TODO refresh current obj to react to the current changes
        pass