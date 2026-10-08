import tkinter as tk

# Create the main window
window = tk.Tk()

# Window title and size
window.title("My Calculator")
window.geometry("300x400")
window.configure(background="green")

# Calculator display
display = tk.Entry(window, font=("Arial", 20), background="lightgreen", borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=3, pady=20)


button1 = tk.Button(
    window,
    text="1",
    font=("Arial", 18),
    command=lambda: display.insert(tk.END, "1")
)
button1.grid(row=1, column=0)


button2 = tk.Button(
    window,
    text="2",
    font=("Arial", 18),
    command=lambda: display.insert(tk.END, "2")
)
button2.grid(row=1, column=1)


button3 = tk.Button(
    window,
    text="3",
    font=("Arial", 18),
    command=lambda: display.insert(tk.END, "3")
)
button3.grid(row=1, column=2)


button4 = tk.Button(
    window,
    text="4",
    font=("Arial", 18),
    command=lambda: display.insert(tk.END, "4")
)
button4.grid(row=2, column=0)


button5 = tk.Button(
    window,
    text="5",
    font=("Arial", 18),
    command=lambda: display.insert(tk.END, "5")
)
button5.grid(row=2, column=1)


button6 = tk.Button(
    window,
    text="6",
    font=("Arial", 18),
    command=lambda: display.insert(tk.END, "6")
)
button6.grid(row=2, column=2)


button7 = tk.Button(
    window,
    text="7",
    font=("Arial", 18),
    command=lambda: display.insert(tk.END, "7")
)
button7.grid(row=3, column=0)


button8 = tk.Button(
    window,
    text="8",
    font=("Arial", 18),
    command=lambda: display.insert(tk.END, "8")
)
button8.grid(row=3, column=1)


button9 = tk.Button(
    window,
    text="9",
    font=("Arial", 18),
    command=lambda: display.insert(tk.END, "9")
)
button9.grid(row=3, column=2)


button0 = tk.Button(
    window,
    text="0",
    font=("Arial", 18),
    command=lambda: display.insert(tk.END, "0")
)
button0.grid(row=4, column=1)

button_clear = tk.Button(
    window,
    text="C",
    font=("Arial", 18),
    command=lambda: display.delete(0, tk.END)
)

button_clear.grid(row=4, column=2)

def choose_operator(op):
    global first_number, operator

    first_number = float(display.get())
    operator = op

    display.insert(tk.END, " " + op + " ")


def calculate():
    expression = display.get()

    parts = expression.split()

    first_number = float(parts[0])
    operator = parts[1]
    second_number = float(parts[2])

    if operator == "+":
        answer = first_number + second_number
    elif operator == "-":
        answer = first_number - second_number

    display.delete(0, tk.END)
    display.insert(tk.END, answer)
button_add = tk.Button(
    window,
    text="+",
    font=("Arial", 18),
    command=lambda: choose_operator("+")
)

button_add.grid(row=4, column=0)

button_subtract = tk.Button(
    window,
    text="-",
    font=("Arial", 18),
    command=lambda: choose_operator("-")
)

button_subtract.grid(row=5, column=0)

button_equals = tk.Button(
    window,
    text="=",
    font=("Arial", 18),
    command=calculate
)

button_equals.grid(row=5, column=2)


window.mainloop()