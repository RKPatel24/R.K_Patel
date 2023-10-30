import tkinter as tk

def increase_value():
    value = int(label["text"])
    value += 1
    label["text"] = str(value)

def decrease_value():
    value = int(label["text"])
    value -= 1
    label["text"] = str(value)


window = tk.Tk()


label = tk.Label(window, text="0", width=10, font=("Arial", 16))
label.pack(pady=120)


plus_button = tk.Button(window, text="+", width=10, command=increase_value)
plus_button.pack(pady=120)


minus_button = tk.Button(window, text="-", width=10, command=decrease_value)
minus_button.pack(pady=120)


window.mainloop()
