from tkinter import Tk, Button, Label, Entry

window = Tk()
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)
window.title('Miles to KM converter')


def calculate():
    miles = input_box.get()
    if len(miles) <= 0:
        miles = "0.0"
    km = 1.609 * float(miles)
    default_value['text'] = round(km, 3)


input_box = Entry(width=15)
calculate_btn = Button(text="calculate", command=calculate)
mile_label = Label(text="miles")
km_label = Label(text='Km')
general_label = Label(text="is equals to ")
default_value = Label(text="0")

input_box.grid_configure(column=1, row=0)
mile_label.grid_configure(column=2, row=0)
general_label.grid_configure(column=0, row=1)
default_value.grid_configure(column=1, row=1)
km_label.grid_configure(column=2, row=1)
calculate_btn.grid_configure(column=1, row=2)

window.mainloop()
