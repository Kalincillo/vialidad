from tkinter import *
from tkinter import ttk

root = Tk()

content = ttk.Frame(root)
frame = ttk.Frame(content)

# data input labels
car_id_lb = ttk.Label(content, text="Placa")
app_id_lb = ttk.Label(content, text="Folio")

# data entry
car_id_ent = ttk.Entry(content)


# grid configuration
content.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=4, rowspan=3)
car_id_lb.grid(column=0, row=1)
app_id_lb.grid(column=0, row=2)
car_id_ent.grid(column=1, row=1)


root.mainloop()
