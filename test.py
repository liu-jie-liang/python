from Tkinter import *

class Application (Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.quitButton = Button(self)
        self.quitButton["text"] = "quit"
        self.quitButton["fg"] = "red"
        self.quitButton["command"] = self.quit

        self.quitButton.pack({"side": "left"})

        self.hi = Button(self)
        self.hi["text"] = "hi"
        self.hi["command"] = self.say_hi

        self.hi.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()