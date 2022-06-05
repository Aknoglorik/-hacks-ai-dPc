import numpy as np
import tkinter as tk
from tkcalendar import DateEntry
import joblib
from sklearn.ensemble import RandomForestClassifier
import datetime as dt

QUALITY = "180x80"


class App:
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry(QUALITY)
        self.root.title("Demo")
        self.root.resizable = False

        self.menubar = tk.Menu(self.root)

        self.setup()
        self.rf = joblib.load("my_random_forest.joblib")

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
        
        year = str(pred_date).split('-')[0]
        month = str(pred_date).split('-')[1]
        day = str(pred_date).split('-')[2]
        
        date = dt.datetime.strptime(str(pred_date), '%Y-%m-%d')
        

        temp = 0
        bar = 0

        weather = 0
        weekend = 0
        with open('weather/info.txt') as file:
            for line in file:
                spl = line.split(' ')
                y, m, d = spl[0].split('-')
                if y == year and month == m and d == day:
                    print(y,m,d)
                    temp = spl[2]
                    bar = spl[3]
                    wear = spl[4]
                    week = [5]
                    break
            else:
                self.label['text'] = 'нет данных о погоде'
                return
        
        X = np.array(list(map(float, [day, month, temp, bar, weather, weekend])))
        
        res = self.rf.predict((X,))
        self.label['text'] = str(res[0]* 506 + 2) # восстановление данных

    def start(self):
        self.root.mainloop()


app = App()
app.start()
