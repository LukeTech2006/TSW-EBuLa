import tkinter as tk
import customtkinter as ctk

from components.line_comp.vmax import VmaxEntry
from components.line_map_mod import LineMapMod

# Hauptfenster erstellen
root = ctk.CTk()
root.title("Nested Grids Beispiel mit CustomTkinter")

# Frame im Hauptfenster erstellen
main_frame = ctk.CTkFrame(root, bg_color='red', corner_radius=30,fg_color="purple")
main_frame.grid(row=0, column=0, padx=10, pady=10)

# Frame innerhalb des Hauptframes erstellen
inner_frame = ctk.CTkFrame(main_frame, bg_color='green', corner_radius=30)
inner_frame.grid(row=0, column=0, padx=5, pady=5)

# Widgets im inneren Frame erstellen
for i in range(3):
    for j in range(3):
        # button = ctk.CTkButton(inner_frame, text=f"Button {i}-{j}")
        button = VmaxEntry(inner_frame)
        button.grid(row=i, column=j, padx=5, pady=5)

# Frame innerhalb des Hauptframes erstellen
inner_frame2 = ctk.CTkFrame(main_frame, bg_color='white', corner_radius=30)
inner_frame2.grid(row=1, column=1, padx=5, pady=5)

# Widgets im inneren Frame erstellen
for i in range(3):
    for j in range(3):
        # button = ctk.CTkButton(inner_frame2, text=f"Button {i}-{j}")
        button = LineMapMod(inner_frame2)
        button.grid(row=i, column=j, padx=5, pady=5)

# Hauptfenster anzeigen
root.mainloop()
