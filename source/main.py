import tkinter as tk
import time, webbrowser, sys

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.labelUrl = tk.Label(text="URL")
        self.entryUrl = tk.Entry(bd=3)
        self.labelTime = tk.Label(text="Time (24H)")
        self.entryTime = tk.Entry(bd=3)
        self.root.geometry("370x420")
        self.root.title('ZOOMBot')
        self.labelUrl.pack()
        self.entryUrl.pack()
        self.labelTime.pack()
        self.entryTime.pack()
        self.submit = tk.Button(text="run", command=self.openZoom)
        self.submit.pack()
        self.updateTime()
        self.root.mainloop()

    def updateTime(self):
        self.now = time.strftime("%H:%M")
        self.root.after(1000, self.updateTime)

    def openUrl(self):
        url = self.entryUrl.get()
        webbrowser.open_new_tab(url)

    def openZoom(self):
        self.startTime = self.entryTime.get()
        startHour = self.startTime[1]
        if startHour == ":":
            self.startTime = str("0" + startTime)
        if(self.now == self.startTime):
            self.openUrl()
            sys.exit()
        self.root.after(1000, self.openZoom)

app=App()
