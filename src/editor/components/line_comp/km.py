import customtkinter

class KmEntry(customtkinter.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, placeholder_text="km,m", width=75, **kwargs)

        # Set elements
        # self.entry = customtkinter.CTkEntry(master, corner_radius=5,placeholder_text="km,m")

        # Set Defaults

        print("init KmEntry")

    def unify():
        # TODO unify , and . from inputs
        pass