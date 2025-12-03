import tkinter as tk
from math import *

def click(button):
    current = entry.get()

    # Clear
    if button == "C":
        entry.delete(0, tk.END)

    # Delete last character
    elif button == "DEL":
        entry.delete(len(current)-1, tk.END)

    # Evaluate expression safely
    elif button == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    # Insert function with parentheses (sin -> sin())
    elif button in ["sin", "cos", "tan", "log", "sqrt"]:
        entry.insert(tk.END, button + "(")

    # Insert normal characters
    else:
        entry.insert(tk.END, button)

# Window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("380x550")
root.configure(bg="pink")

entry = tk.Entry(root, width=18, font=("Arial", 24), bd=5, relief=tk.FLAT, justify="right")
entry.pack(pady=20)

# Button layout
buttons = [
    ["C", "DEL", "(", ")"],
    ["sin", "cos", "tan", "log"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "sqrt", "+"],
    ["="]
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root, bg="pink")
    frame.pack()
    for btn in row:
        tk.Button(
            frame,
            text=btn,
            width=8,
            height=2,
            font=("Arial", 14),
            bg="#222",
            fg="white",
            command=lambda button=btn: click(button)
        ).pack(side="left", padx=5, pady=5)

root.mainloop()
