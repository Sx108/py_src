import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

root = tk.Tk()
root.title("Calculator")

screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold")
screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    'C', '0', '=', '+'
]

row, col = 0, 0
for button in buttons:
    btn = tk.Button(button_frame, text=button, font="lucida 15 bold", padx=20, pady=20)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col += 1
    if col == 4:
        col = 0
        row += 1

root.mainloop()