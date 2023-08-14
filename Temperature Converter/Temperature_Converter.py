import tkinter as tk
from tkinter import IntVar, Label, Entry, Button

def TemperatureConverter():
    def convert():
        try:
            celTemp = celTempVar.get()
            fahTemp = fahTempVar.get()
            kelTemp = kelTempVar.get()

            if celTemp != 0.0:
                celToFah = (celTemp * 9/5 + 32)
                fahTempVar.set(celToFah)
                kelTempVar.set(celTemp + 273.15)

            elif fahTemp != 0.0:
                fahToCel = ((fahTemp - 32) * 5/9)
                celTempVar.set(fahToCel)
                kelTempVar.set((fahTemp + 459.67) * 5/9)

            elif kelTemp != 0.0:
                kelToCel = (kelTemp - 273.15)
                celTempVar.set(kelToCel)
                fahTempVar.set(kelTemp * 9/5 - 459.67)

            message_var.set("")  # Clear any previous messages
        except ValueError:
            message_var.set("Invalid input")

    def reset():
        celTempVar.set(0)
        fahTempVar.set(0)
        kelTempVar.set(0)
        message_var.set("Reset Complete")

    root = tk.Tk()
    root.title("Temperature Converter")
    root.geometry("500x250")

    celTempVar = IntVar()
    fahTempVar = IntVar()
    kelTempVar = IntVar()
    message_var = tk.StringVar()

    titleLabel = Label(root, text="Temperature Converter", font=("Arial", 16, "bold"))
    titleLabel.grid(column=0, row=0, columnspan=3, pady=20)

    celLabel = Label(root, text="Celsius: ", font=("Arial", 14), fg="red")
    celLabel.grid(row=1, column=0, padx=50, sticky=tk.W)

    fahLabel = Label(root, text="Fahrenheit: ", font=("Arial", 14), fg="blue")
    fahLabel.grid(row=1, column=1, padx=18, sticky=tk.W)

    kelLabel = Label(root, text="Kelvin: ", font=("Arial", 14), fg="green")
    kelLabel.grid(row=1, column=2, padx=18, sticky=tk.W)

    celEntry = Entry(root, width=10, bd=5, textvariable=celTempVar)
    celEntry.grid(row=2, column=0, padx=50, pady=10, sticky=tk.W)

    fahEntry = Entry(root, width=10, bd=5, textvariable=fahTempVar)
    fahEntry.grid(row=2, column=1, padx=20, pady=10, sticky=tk.W)

    kelEntry = Entry(root, width=10, bd=5, textvariable=kelTempVar)
    kelEntry.grid(row=2, column=2, padx=20, pady=10, sticky=tk.W)

    convertButton = Button(root, text="Convert", font=("Arial", 12, "bold"), command=convert)
    convertButton.grid(row=3, column=0, columnspan=1, pady=10)

    resetButton = Button(root, text="Reset", font=("Arial", 12, "bold"), command=reset)
    resetButton.grid(row=3, column=2, columnspan=4, pady=10)

    message_label = Label(root, textvariable=message_var, font=("Arial", 12, "bold"), fg="green")
    message_label.grid(row=5, column=0, columnspan=3)

    root.mainloop()

if __name__ == "__main__":
    TemperatureConverter()
