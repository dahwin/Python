def get_difference(str1, str2):
    # Initialize a counter to keep track of the number of differences
    difference_count = 0

    # Compare each character in the strings and increment the counter if they are different
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            difference_count += 1

    # Return the difference count plus the difference in length between the two strings
    return difference_count + abs(len(str1) - len(str2))



# Test the function


def get_difference_indices(str1, str2):
    # Initialize a list to store the indices of the different characters
    difference_indices = []

    # Compare each character in the strings and add the index to the list if they are different
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            difference_indices.append(i)

    # Add the indices of any extra characters in the longer string
    for i in range(min(len(str1), len(str2)), max(len(str1), len(str2))):
        difference_indices.append(i)

    return difference_indices
# print(get_difference("hello", "hello"))
# print(get_difference_indices("hello", "hello"))
# print(get_difference("hello", "hellofuck"))
# print(get_difference_indices("hello", "hellofuck"))
#
import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the line edit widgets for the input strings
        self.str1Edit = tk.Entry(self)
        self.str2Edit = tk.Entry(self)

        # Create the buttons for the two functions
        self.differenceButton = tk.Button(self, text='Get Difference', command=self.getDifference)
        self.differenceIndicesButton = tk.Button(self, text='Get Difference Indices', command=self.getDifferenceIndices)

        # Create the label for the output
        self.outputLabel = tk.Label(self)

        # Create the layout and add the widgets
        self.str1Edit.pack()
        self.str2Edit.pack()
        self.differenceButton.pack()
        self.differenceIndicesButton.pack()
        self.outputLabel.pack()

    def getDifference(self):
        # Get the input strings from the line edit widgets
        str1 = self.str1Edit.get()
        str2 = self.str2Edit.get()

        # Call the get_difference function and set the output label to the result
        result = get_difference(str1, str2)
        self.outputLabel.config(text=str(result))

    def getDifferenceIndices(self):
        # Get the input strings from the line edit widgets
        str1 = self.str1Edit.get()
        str2 = self.str2Edit.get()

        # Call the get_difference_indices function and set the output label to the result
        result = get_difference_indices(str1, str2)
        self.outputLabel.config(text=str(result))


app = MainWindow()
app.mainloop()
