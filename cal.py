import tkinter as tk
from tkinter import messagebox

def press(key):
    if key == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif key == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, key)

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Entry widget for user input
entry = tk.Entry(root, width=20, font=("Arial", 16), bd=5, relief=tk.SUNKEN, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Add buttons to the window
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(
        root,
        text=button,
        width=5,
        height=2,
        font=("Arial", 14),
        command=lambda b=button: press(b)
    ).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the Tkinter event loop
root.mainloop()
