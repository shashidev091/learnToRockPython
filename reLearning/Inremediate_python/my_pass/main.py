from tkinter import Tk, Label, Button, Canvas, PhotoImage, Entry, END, messagebox
from password_genrator import generate_random_password
import pyperclip
import json

window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")


def generate_handler():
    strong_password = generate_random_password(length=21)
    password_input.delete(0, END)
    password_input.insert(0, strong_password)
    pyperclip.copy(strong_password)


def parse_into_json(website, email, password):
    password_obj = {
        website: {
            "email": email,
            "password": password
        }
    }
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)

    except (json.JSONDecodeError, FileNotFoundError) as error:
        print(error, "Since there was no file to open or read .")
        with open('data.json', 'w') as data_file:
            json.dump(password_obj, data_file, indent=4)

    else:
        data.update(password_obj)

        with open('data.json', 'w') as data_file:
            json.dump(data, data_file, indent=4)

    finally:
        website_input.delete(0, END)
        email_input.delete(0, END)
        password_input.delete(0, END)


def submit_password():
    email = email_input.get()
    website = website_input.get()
    password = password_input.get()

    if len(email) <= 0 or len(website) <= 0 or len(password) <= 0:
        messagebox.showwarning(title='Fields required', message="Please fill all the required fields")
    elif len(password) < 8:
        messagebox.showwarning(title="OOPS!!!", message='Password is too short...')
    else:
        is_ok = messagebox.askokcancel(title="confirmation",
                                       message=f"These are the details entered: \n Email: {email}\n"
                                               f"Password {password} \n Is it ok to save?")
        if is_ok:
            # with open('data.txt', 'a') as data_file:
            #     data_file.writelines(f'\n{website} | {email} | {password}')
            #     website_input.delete(0, END)
            #     email_input.delete(0, END)
            #     password_input.delete(0, END)
            parse_into_json(website, email, password)

        messagebox.showinfo(message="details saved successfully!😊! \n and password copied to clipboard",
                            title="Status")


def search_handler():
    website = website_input.get()

    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, ):
        if website in data:
            fetched_email = data[website]['email']
            fetched_password = data[website]['password']

            messagebox.showinfo(title="found item",
                                message=f"Email : {fetched_email} \n Password : \n {fetched_password}")
        else:
            messagebox.showinfo(title="Status", message=f"No info is available in the database similar to {website}")


# required objects
canvas = Canvas()
image = PhotoImage(file='logo.png')
website_label = Label(text="Website")
website_input = Entry(width=21)
email_input = Entry(width=35)
email_label = Label(text="Email/Username")
password_label = Label(text="Password")
password_input = Entry(width=21)
password_generator = Button(width=10, text='generator', command=generate_handler)
search_button = Button(width=10, text='search', command=search_handler)
submit_btn = Button(width=25, text="submit", command=submit_password)

# organise the ui
canvas.config(width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
website_input.grid(row=1, column=1)
search_button.grid(row=1, column=2)
email_label.grid(row=2, column=0)
email_input.grid(row=2, column=1, columnspan=2)
password_label.grid(row=3, column=0)
password_input.grid(row=3, column=1)
password_generator.grid(row=3, column=2)
submit_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
