import tkinter as tk
from tkinter import messagebox
from math import log

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.entry = tk.Entry(self.window, width=20)
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.window, text=button, width=5, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(self.window, text="log", width=5, command=lambda: self.click_button("log")).grid(row=row_val, column=0)
        tk.Button(self.window, text="%", width=5, command=lambda: self.click_button("%")).grid(row=row_val, column=1)
        tk.Button(self.window, text="C", width=5, command=lambda: self.click_button("C")).grid(row=row_val, column=2)
        tk.Button(self.window, text="=", width=10, command=lambda: self.click_button("=")).grid(row=row_val, column=3, columnspan=2)

    def click_button(self, button):
        if button == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif button == "C":
            self.entry.delete(0, tk.END)
        elif button == "log":
            try:
                result = log(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif button == "%":
            try:
                result = float(self.entry.get()) / 100
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            self.entry.insert(tk.END, button)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()