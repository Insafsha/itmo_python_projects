import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

API_URL = "https://randomfox.ca/floof/"

def get_fox_url():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json().get("image")
    return None

def update_image():
    image_url = get_fox_url()
    if not image_url:
        return

    response = requests.get(image_url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content)).resize((400, 400), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo

root = tk.Tk()
root.title("Случайная лиса")
root.geometry("450x500")

image_label = tk.Label(root)
image_label.pack()

tk.Button(root, text="Новая лиса!", command=update_image, font=("Arial", 14)).pack(pady=10)

update_image()
root.mainloop()
