import tkinter as tk
from tkinter import messagebox
from keygen import generate_key


def start_ui():
    window = tk.Tk()
    window.title("Генератор ключей")
    window.geometry("600x400")

    # Фон
    try:
        bg_img = tk.PhotoImage(file="lab3/data/game_art.png")
        lbl_bg = tk.Label(window, image=bg_img)
        lbl_bg.image = bg_img
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print("Ошибка загрузки картинки:", e)

    frame = tk.Frame(window, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    pref_label = tk.Label(frame, text="1 блок ключа (5 символов):", bg="white")
    pref_label.grid(row=0, column=0, padx=10, pady=10)

    pref_entry = tk.Entry(frame, width=20)
    pref_entry.grid(row=0, column=1, padx=10, pady=10)

    key_label = tk.Label(frame, text="Сгенерированный ключ:", bg="white")
    key_label.grid(row=1, column=0, padx=10, pady=10)

    key_field = tk.Entry(frame, width=20)
    key_field.grid(row=1, column=1, padx=10, pady=10)

    def on_click():
        try:
            key = generate_key(pref_entry.get())
            key_field.delete(0, tk.END)
            key_field.insert(0, key)
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    button = tk.Button(frame, text="Генерировать", bg="#4CAF50", fg="white", command=on_click)
    button.grid(row=2, column=0, columnspan=2, pady=20)

    window.mainloop()
