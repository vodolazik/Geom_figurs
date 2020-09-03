import tkinter as tk
import turtle


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.button1 = tk.Button(self, text="Квадрат", command=self.square)
        self.button1.pack()
        self.button2 = tk.Button(self, text="Прямокутник", command=self.rect)
        self.button2.pack()
        self.button3 = tk.Button(self, text="Трикутник", command=self.triangle)
        self.button3.pack()
        self.button4 = tk.Button(self, text="Очистити", command=self.ochist)
        self.button4.pack()
        self.button5 = tk.Button(self, text="Перейти праворуч", command=self.pravo)
        self.button5.pack()
        self.button6 = tk.Button(self, text="Перейти ліворуч", command=self.levo)
        self.button6.pack()


    def square(self):
        for i in range(4):
            che.forward(100)
            che.left(90)

    def rect(self):
        for i in range(2):
            che.forward(100)
            che.left(90)
            che.forward(60)
            che.left(90)

    def triangle(self):
        for i in range(3):
            che.forward(100)
            che.left(120)

    def ochist(self):
        che.clear()

    def pravo (self):
        che.up()
        che.forward(120)
        che.down()

    def levo (self):
        che.up()
        che.left(180)
        che.forward(120)
        che.left(180)
        che.down()


che = turtle.Turtle()


app = SampleApp()
app.mainloop()
