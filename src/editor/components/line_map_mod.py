import customtkinter

from components.line_comp.vmax import VmaxEntry
from components.line_comp.km import KmEntry
from components.line_comp.poi import PoiEntry
# from components.line_comp. import 

class LineMapMod(customtkinter.CTkScrollableFrame):
    def __init__(self, master, item_count:int = 5, **kwargs):
        self.super = super().__init__(master, **kwargs)
        # self.main_frame.grid(row=0, column=1, pady=(0, 10))

        self.item_list = []     # List for all Line Elements

        # Set elements
        # self.main_frame = master
        # self.main_frame = customtkinter.CTkScrollableFrame(master,width=500,height=500)

        # Set Defaults
        # self.main_frame.grid_columnconfigure((0,1,2,4,5), weight=1, uniform="line")
        # self.main_frame.grid_rowconfigure(0, weight=1, uniform="line")

        # Other init things
        for i in range(item_count):
            self.addLine()

    def addLine(self):
        frame = customtkinter.CTkFrame(self)
        frame.grid(row=len(self.item_list), column=0, padx=10,pady=0)
        print(len(self.item_list))

        item_VmaxEntry = VmaxEntry(frame)
        # item_VmaxEntry.
        item_VmaxEntry.grid(row=0, column=1, pady=10, padx=10)

        item_KmEntry = KmEntry(frame)
        item_KmEntry.grid(row=0, column=2, pady=10, padx=10)

        item_PoiEntry = PoiEntry(frame)
        item_PoiEntry.grid(row=0, column=3, pady=10, padx=10)
        
        # self.item_list.append((frame,item_VmaxEntry,item_KmEntry))
        self.item_list.append(frame)


    def removeLine(self):
        pass
