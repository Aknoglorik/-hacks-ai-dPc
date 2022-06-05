import numpy as np
import tkinter as tk
from tkcalendar import DateEntry
import sys

QUALITY = "180x80"


class App:
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry(QUALITY)
        self.root.title("Demo")
        self.root.resizable = False

        self.menubar = tk.Menu(self.root)

        self.setup()

    def setup(self):
        # Make menubar
        self.root.config(menu=self.menubar)

        # Make start scene
        self.btn = tk.Button(text='Предсказать', command=self.on_btn_pressed)
        self.date = DateEntry()
        self.label = tk.Label(text='')

        self.date.pack(expand=True)
        self.btn.pack(expand=True)
        self.label.pack(expand=True)

    def on_btn_pressed(self):
        pred_date = self.date.get_date()
        day = pred_date.day()
        month = pred_date.month()

        temp = 0
        bar = 0

        weather = 0
        weekend = 0

        self.predict([day, month, temp, bar, weather, weekend])

    def predict(self, X):   # FIXME!
        weight = np.array([0.08495557, 0.00297253, -0.06059933, 0.00481572, 0.0133653, 0.01874809])
        X.vstack()
        self.label['text'] = str(weight * X)

    def start(self):
        self.root.mainloop()


app = App()
app.start()