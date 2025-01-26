from tkinter import *
from tkinter import ttk


GUI = Tk()
GUI.geometry('500x500')



class WorkorderList(ttk.Treeview):
    def __init__(self, GUI):
        header = ['TSID', "ชื่อ", "แผนก", "อุปกรณ์/เครื่อง", "อาการเสีย", "หมายเลข", "หมายเลขโทรศัพท์", "สถานะ"]
        headerw = [100, 150, 120, 200, 200, 150, 150, 120]
        ttk.Treeview.__init__(self, GUI, columns=header,show='headings', height=10)
        for h, w in zip(header, headerw):
            self.heading(h, text=h)
            self.column(h, width=w, anchor='center')

    def insertdata(self, values):
        self.insert('', 'end', values=values)


        

t = WorkorderList(GUI)
t.pack()
t.insertdata(["a", "b", "c"])



GUI.mainloop()