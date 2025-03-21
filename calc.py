import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        tk.Button(root, text=button, padx=40, pady=20, command=calculate).grid(row=row_val, column=col_val)
    elif button == "C":
        tk.Button(root, text=button, padx=40, pady=20, command=clear).grid(row=row_val, column=col_val)
    elif button == "<-":
        tk.Button(root, text=button, padx=40, pady=20, command=backspace).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=40, pady=20, command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text="C", padx=40, pady=20, command=clear).grid(row=5, column=0)
tk.Button(root, text="<-", padx=40, pady=20, command=backspace).grid(row=5, column=1)

root.mainloop()
