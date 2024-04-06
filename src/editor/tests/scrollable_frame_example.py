import customtkinter
# from PIL import Image

# # setting path
# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(parent_dir)
 
# # importing
# from editor.components.examples.ScrollableLabelButtonFrame import ScrollableLabelButtonFrame
# from editor.components.examples.ScrollableCheckBoxFrame import ScrollableCheckBoxFrame
# from editor.components.examples.ScrollableRadiobuttonFrame import ScrollableRadiobuttonFrame

from components.examples.ScrollableCheckBoxFrame import ScrollableCheckBoxFrame
from editor.components.examples.ScrollableLabelButtonFrame import ScrollableLabelButtonFrame
# from components.examples.ScrollableRadiobuttonFrame import ScrollableRadiobuttonFrame

from src.editor.components.examples.ScrollableRadiobuttonFrame import ScrollableRadiobuttonFrame

# from ..components.examples.ScrollableCheckBoxFrame import ScrollableCheckBoxFrame
# from ..components.examples.ScrollableLabelButtonFrame import ScrollableLabelButtonFrame
# from ..components.examples.ScrollableRadiobuttonFrame import ScrollableRadiobuttonFrame

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("CTkScrollableFrame example")
        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)

        # create scrollable checkbox frame
        self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self, width=200, command=self.checkbox_frame_event,
                                                                 item_list=[f"item {i}" for i in range(50)])
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=15, pady=15, sticky="ns")
        self.scrollable_checkbox_frame.add_item("new item")

        # create scrollable radiobutton frame
        self.scrollable_radiobutton_frame = ScrollableRadiobuttonFrame(master=self, width=500, command=self.radiobutton_frame_event,
                                                                       item_list=[f"item {i}" for i in range(100)],
                                                                       label_text="ScrollableRadiobuttonFrame")
        self.scrollable_radiobutton_frame.grid(row=0, column=1, padx=15, pady=15, sticky="ns")
        self.scrollable_radiobutton_frame.configure(width=200)
        self.scrollable_radiobutton_frame.remove_item("item 3")

        # create scrollable label and button frame
        # current_dir = os.path.dirname(os.path.abspath(__file__))
        self.scrollable_label_button_frame = ScrollableLabelButtonFrame(master=self, width=300, command=self.label_button_frame_event, corner_radius=0)
        self.scrollable_label_button_frame.grid(row=0, column=2, padx=0, pady=0, sticky="nsew")
        for i in range(20):  # add items with images
            # self.scrollable_label_button_frame.add_item(f"image and item {i}", image=customtkinter.CTkImage(Image.open(os.path.join(current_dir, "test_images", "chat_light.png"))))
            self.scrollable_label_button_frame.add_item(f"image and item {i}")

    def checkbox_frame_event(self):
        print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")

    def radiobutton_frame_event(self):
        print(f"radiobutton frame modified: {self.scrollable_radiobutton_frame.get_checked_item()}")

    def label_button_frame_event(self, item):
        print(f"label button frame clicked: {item}")
        if item == "image and item 1":
            self.scrollable_radiobutton_frame.add_item("new new")


if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    app = App()
    app.mainloop()