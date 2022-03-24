from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Vialidad app")

content = ttk.Frame(root)
frame = ttk.Frame(content, width=500, height=500)

# data input labels
car_id_lb = ttk.Label(content, text="Placa")
app_id_lb = ttk.Label(content, text="Folio")

# strings
folio = StringVar()
placa = StringVar()

# data entry
car_id_ent = ttk.Entry(content, textvariable=placa)
app_id_ent = ttk.Entry(content, textvariable=folio)



# grid configuration
content.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=4, rowspan=3)
car_id_lb.grid(column=0, row=1, sticky=(N,W))
app_id_lb.grid(column=0, row=2, sticky=(N,W))
car_id_ent.grid(column=1, row=1, sticky=(N,W))
car_id_ent.grid(column=1, row=2, sticky=(N,W))


root.mainloop()
