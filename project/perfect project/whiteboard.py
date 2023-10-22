import tkinter as tk

class Whiteboard:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=400, height=400, bg='white')
        self.canvas.pack()
        self.canvas.bind('<B1-Motion>', self.paint)

        self.clear_button = tk.Button(root, text='Clear', command=self.clear_canvas)
        self.clear_button.pack()

    def paint(self, event):
        x1, y1 = (event.x - 5), (event.y - 5)
        x2, y2 = (event.x + 5), (event.y + 5)
        self.canvas.create_oval(x1, y1, x2, y2, fill='black')

root = tk.Tk()
app = Whiteboard(root)
root.mainloop()
