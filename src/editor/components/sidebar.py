import customtkinter

from components.settings_panel import SettingPanel

class Sidebar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(master, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.add_poi)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.settings_panel = SettingPanel(self.sidebar_frame)

        # set default values
        self.sidebar_button_3.configure(state="disabled", text="Disabled CTkButton")

    def sidebar_button_event(self):
        print("sidebar_button click")
        print(list(self.test.children.keys()).count())
        # print(list(self.test.children.keys()) list(self.test.children.keys()).count())
        self.test.children.pop()
    
    def add_poi(self):
        print("add_poi")
        # self.test2 = customtkinter.CTkLabel(self.test, text="test")
        # self.test2.pack()

        # self.test3 = customtkinter.CTkButton(self.test, text="del")
        # self.test3.pack()
        # # self.test3
        # self.test3.configure(command= lambda: self.test_del(self.test3,self.test2))

        # print(type(self.test.children))
        # print(self.test.children)
        pass