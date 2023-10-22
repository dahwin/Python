import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")

        # Create the display for the calculator
        self.display = tk.Entry(root, width=40, bg="lightgrey")
        self.display.grid(row=0, column=0, columnspan=5)

        # Create the buttons for the calculator
        button_list = [
            "7", "8", "9", "AC", "C",
            "4", "5", "6", "/", "*",
            "1", "2", "3", "-", "+",
            "0", ".", "=", "^", "sqrt",
        ]

        # Create a 2D list of rows and columns for the buttons
        buttons = []
        for i in range(5):
            button_row = []
            for j in range(4):
                button_row.append(tk.Button(root, text=button_list[i * 4 + j]))
            buttons.append(button_row)

        # Add the buttons to the grid
        for i in range(5):
            for j in range(4):
                buttons[i][j].grid(row=i + 1, column=j)

        # Bind the buttons to the calculator functions
        for i in range(5):
            for j in range(4):
                buttons[i][j].bind("<Button-1>", self.button_press)

    def button_press(self, event):
        # Get the text of the button that was pressed
        button_text = event.widget.cget("text")

        # Perform the appropriate action based on the button text
        if button_text == "AC":
            # Clear the display
            self.display.delete(0, "end")
        elif button_text == "C":
            # Clear the last character in the display
            self.display.delete("end-1c")
        elif button_text == "=":
            # Evaluate the expression in the display
            result = eval(self.display.get())
            self.display.delete(0, "end")
            self.display.insert(0, str(result))
        elif button_text == "sqrt":
            # Compute the square root of the number in the display
            result = math.sqrt(float(self.display.get()))
            self.display.delete(0, "end")
            self.display.insert(0, str(result))
        else:
            # Append the button text to the end of the display
            self.display.insert("end", button_text)


# Create the root window and the calculator
root = tk.Tk()
calc = Calculator(root)

# Run the Tkinter event loop
root.mainloop()
