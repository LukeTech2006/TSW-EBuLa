import customtkinter

from editor.funcs.settings import change_appearance_mode_event, change_scaling_event

class SettingPanel(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Set elements
        self.appearance_mode_label = customtkinter.CTkLabel(master, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(master, values=["Light", "Dark", "System"],
                                                                        command=change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(master, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(master, values=["80%", "90%", "100%", "110%", "120%"],
                                                                command=change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # Set Defaults
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")