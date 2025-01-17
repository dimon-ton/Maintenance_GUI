from tkinter import *
from tkinter import messagebox
from datetime import datetime
from tkinter import ttk

# import database
from db_maintenance import *


# Generate a unique tsid
import uuid


GUI = Tk()

GUI.title('โปรแกรมซ๋อมบำรง By Dimon')
GUI.geometry('800x600+50+50')

# Font
FONT1 = ('Angsana New', 16)


############## TAB ##################
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)
Tab.add(T1, text='ใบแจ้งซ่อม')
Tab.add(T2, text='ดูใบแจ้งซ่อม')
Tab.add(T3, text='สรุป')
Tab.pack(fill=BOTH, expand=1)




L = Label(T1,text='ใบแจ้งซ่อม',font=FONT1)
L.place(x=80, y=13)

L = Label(T1,text='ชื่อผู้แจ้ง',font=FONT1)
L.place(x=30, y=50)

v_name = StringVar()
E1 = ttk.Entry(T1, textvariable=v_name, font=FONT1)
E1.place(x=150, y=50)

L = Label(T1,text='แผนก',font=FONT1)
L.place(x=30, y=100)

v_department = StringVar()
E2 = ttk.Entry(T1, textvariable=v_department, font=FONT1)
E2.place(x=150, y=100)

L = Label(T1,text='อุปกรณ์/เครื่อง',font=FONT1)
L.place(x=30, y=150)

v_machine = StringVar()
E3 = ttk.Entry(T1, textvariable=v_machine, font=FONT1)
E3.place(x=150, y=150)

L = Label(T1,text='อาการเสีย',font=FONT1)
L.place(x=30, y=200)

v_problem = StringVar()
E4 = ttk.Entry(T1, textvariable=v_problem, font=FONT1)
E4.place(x=150, y=200)


L = Label(T1,text='หมายเลข',font=FONT1)
L.place(x=30, y=250)

v_serial = StringVar()
E5 = ttk.Entry(T1, textvariable=v_serial, font=FONT1)
E5.place(x=150, y=250)



L = Label(T1,text='หมายเลขโทรศัพท์',font=FONT1)
L.place(x=30, y=300)

v_phone = StringVar()
E6 = ttk.Entry(T1, textvariable=v_phone, font=FONT1)
E6.place(x=150, y=300)

def save():
    name = v_name.get()
    department = v_department.get()
    machine = v_machine.get()
    problem = v_problem.get()
    serial = v_serial.get()
    phone = v_phone.get()
    

    try:
        if name == '' or department == '' or machine == '' or problem == '' or serial == '' or phone == '':
            messagebox.showwarning('Error','กรุณากรอกข้อมูลให้ครบ')
        else:

            if messagebox.askyesno('ยืนยันการบันทึก', 'คุณต้องการบันทึกข้อมูลใช่หรือไม่?'):
                dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


            #     with open('data.csv', 'a', newline='', encoding='utf-8') as f:
            #         fw = csv.writer(f)
            #         data = [dt, name, department, machine, problem, serial, phone]
            #         fw.writerow(data)

                # Generate a unique tsid
                tsid = 'MT' + str(uuid.uuid4().int)[:8]
                insert_mtworkorder(tsid, name, department, machine, problem, serial, phone)
            
            else:
                return
                
            text = f'วันที่: {dt}\n'
            text += f'ชื่อ: {name}\n'
            text += f'แผนก: {department}\n'
            text += f'อุปกรณ์/เครื่อง: {machine}\n'
            text += f'อาการเสีย: {problem}\n'
            text += f'หมายเลข: {serial}\n'
            text += f'หมายเลขโทรศัพท์: {phone}\n'
            messagebox.showinfo('บันทึกข้อมูลสำเร็จ', text)

            v_name.set('')
            v_department.set('')
            v_machine.set('')
            v_problem.set('')
            v_serial.set('')
            v_phone.set('')
    except Exception as e:
        messagebox.showerror('Error', str(e))
        


B = Button(T1,text='บันทึกใบแจ้งหนี้', command=save, font=FONT1)
B.place(x=150, y=380)





################################### TAB2 ##########################################
header = ['TSID', "ชื่อ", "แผนก", "อุปกรณ์/เครื่อง", "อาการเสีย", "หมายเลข", "หมายเลขโทรศัพท์"]
headerw = [50, 100, 100, 150, 200, 100, 100]

mtworkorderlist = ttk.Treeview(T2, columns=header,show='headings', height=10)
mtworkorderlist.pack()


for h, w in zip(header, headerw):
    mtworkorderlist.heading(h, text=h)
    mtworkorderlist.column(h, width=w)


[mtworkorderlist.insert('', 'end', values=r[1:]) for r in view_mtworkorder()]


GUI.mainloop() # ทำให้โปรแกรมรันตลอดเวลา