import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

display = tk.Entry(window, width=20, font=('Arial', 16))
display.pack(pady=10)

current = ""

def button_click(number):
    global current
    current += str(number)
    display.delete(0, tk.END)
    display.insert(0, current)

def clear():
    global current
    current = ""
    display.delete(0, tk.END)

def calculate():
    global current
    try:
        result = eval(current)
        display.delete(0, tk.END)
        display.insert(0, str(result))
        current = str(result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")
        current = ""

button_frame = tk.Frame(window)
button_frame.pack()

tk.Button(button_frame, text="1", width=5, height=2, command=lambda: button_click(1)).grid(row=0, column=0)
tk.Button(button_frame, text="2", width=5, height=2, command=lambda: button_click(2)).grid(row=0, column=1)
tk.Button(button_frame, text="3", width=5, height=2, command=lambda: button_click(3)).grid(row=0, column=2)

tk.Button(button_frame, text="4", width=5, height=2, command=lambda: button_click(4)).grid(row=1, column=0)
tk.Button(button_frame, text="5", width=5, height=2, command=lambda: button_click(5)).grid(row=1, column=1)
tk.Button(button_frame, text="6", width=5, height=2, command=lambda: button_click(6)).grid(row=1, column=2)

tk.Button(button_frame, text="7", width=5, height=2, command=lambda: button_click(7)).grid(row=2, column=0)
tk.Button(button_frame, text="8", width=5, height=2, command=lambda: button_click(8)).grid(row=2, column=1)
tk.Button(button_frame, text="9", width=5, height=2, command=lambda: button_click(9)).grid(row=2, column=2)

tk.Button(button_frame, text="0", width=5, height=2, command=lambda: button_click(0)).grid(row=3, column=1)


tk.Button(button_frame, text="+", width=5, height=2, command=lambda: button_click("+")).grid(row=0, column=3)
tk.Button(button_frame, text="-", width=5, height=2, command=lambda: button_click("-")).grid(row=1, column=3)
tk.Button(button_frame, text="*", width=5, height=2, command=lambda: button_click("*")).grid(row=2, column=3)
tk.Button(button_frame, text="/", width=5, height=2, command=lambda: button_click("/")).grid(row=3, column=3)

tk.Button(button_frame, text="=", width=5, height=2, command=calculate).grid(row=3, column=2)
tk.Button(button_frame, text="C", width=5, height=2, command=clear).grid(row=3, column=0)

window.mainloop()
