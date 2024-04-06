import tkinter as tk

# Hauptfenster erstellen
root = tk.Tk()
root.title("Nested Grids Beispiel")

# Frame im Hauptfenster erstellen
main_frame = tk.Frame(root, bg='grey')
main_frame.grid(row=0, column=0, padx=10, pady=10)

# Frame innerhalb des Hauptframes erstellen
inner_frame = tk.Frame(main_frame, bg='white')
inner_frame.grid(row=0, column=0, padx=5, pady=5)

# Widgets im inneren Frame erstellen
for i in range(3):
    for j in range(3):
        button = tk.Button(inner_frame, text=f"Button {i}-{j}")
        button.grid(row=i, column=j, padx=5, pady=5)

# Frame innerhalb des Hauptframes erstellen
inner_frame2 = tk.Frame(main_frame, bg='white')
inner_frame2.grid(row=1, column=1, padx=5, pady=5)

# Widgets im inneren Frame erstellen
for i in range(3):
    for j in range(3):
        button = tk.Button(inner_frame2, text=f"Button {i}-{j}")
        button.grid(row=i, column=j, padx=5, pady=5)

# Hauptfenster anzeigen
root.mainloop()
