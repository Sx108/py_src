from tkinter import *

def btn_click(num):
    #BUTTON CLICK AND UPDATE HANDLING
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current)+str(num))

def btn_clr():
    #CLEARS THE DISPLAY
    entry.delete(0, END)

def btn_eql():
    #PERFORMS THE CALCULATION
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, str('Error'))

#MAIN WINDOW
root = Tk()
root.geometry("400x600")
root.title("Calculator")
root.resizable(width=False, height=False)
root.configure(background="#ffffff")

#CREATING THE DISPLAY
entry = Entry(root,width = 400,borderwidth=2)
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

#DEFINING BUTTONS
btns = ['1', '2', '3','+'
        '4', '5', '6','-',
        '7', '8', '9','*',
        '0','.','=','/']

#CREATING AND POSITIONING BUTTONS
row = 3
col = 0
for button in btns:
    btn_txt = button
    button = Button(root,text=btn_txt,padx = 40,pady = 20,command = lambda b=btn_txt:btn_click(b))
    button.grid(row=row,column=col,padx=10,pady=10)
    col += 1
    if col > 3:
        col = 0
        row += 1

#CLEAR BUTTON
clr_btn = Button(root,text = "C",padx = 40,pady = 20, command=btn_clr)
clr_btn.grid(row=5,column=0,columnspan=2)

#EQL_BTN
eql_btn = Button(root,text = "=",padx = 40,pady = 20,command = btn_eql)
eql_btn.grid(row=5,column=2,columnspan=2)

root.mainloop()