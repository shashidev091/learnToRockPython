import requests
from tkinter import Tk, Canvas, PhotoImage, Button

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.json()['message'])
print(response.status_code)
print(response.raise_for_status())

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data.get("iss_position").get("latitude")
iss_position = (longitude, latitude)
print(iss_position)


def get_quotes():
    response_data = requests.get('https://api.kanye.rest')
    response_data.raise_for_status()
    quote = response_data.json().get('quote')
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(pady=40, padx=40)

canvas = Canvas(width=300, height=500)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 287, image=background_img)
quote_text = canvas.create_text(150, 287, text="Kanye Quotes", width=200, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_pic = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_pic, command=get_quotes, highlightthickness=0)
kanye_button.grid(row=1, column=0)

window.mainloop()
