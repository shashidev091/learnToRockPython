from tkinter import Tk, Label, Button, Entry

window = Tk()

window.title('Shashi\'s GUI app')
window.minsize(width=500, height=300)
my_label = Label(text="I am Groot")


def button_clicked():
    print('Button_clicked')
    my_label["text"] = entry.get()


# centers the element on the screen
my_label.pack()
entry = Entry(width=15)
entry.pack()
button = Button(text="Click me", command=button_clicked)
button.pack()


window.mainloop()
