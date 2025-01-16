from tkinter import *
from tkinter import messagebox
from datetime import datetime

# import database
from db_maintenance import *

import uuid


GUI = Tk()

GUI.title('โปรแกรมซ๋อมบำรง By Dimon')
GUI.geometry('500x500+50+50')

# Font
FONT1 = ('Angsana New', 16)


L = Label(GUI,text='ใบแจ้งซ่อม',font=FONT1)
L.pack()

L = Label(GUI,text='ชื่อผู้แจ้ง',font=FONT1)
L.place(x=30, y=50)

v_name = StringVar()
E1 = Entry(GUI, textvariable=v_name, font=FONT1)
E1.place(x=150, y=50)

L = Label(GUI,text='แผนก',font=FONT1)
L.place(x=30, y=100)

v_department = StringVar()
E2 = Entry(GUI, textvariable=v_department, font=FONT1)
E2.place(x=150, y=100)

L = Label(GUI,text='อุปกรณ์/เครื่อง',font=FONT1)
L.place(x=30, y=150)

v_machine = StringVar()
E3 = Entry(GUI, textvariable=v_machine, font=FONT1)
E3.place(x=150, y=150)

L = Label(GUI,text='อาการเสีย',font=FONT1)
L.place(x=30, y=200)

v_problem = StringVar()
E4 = Entry(GUI, textvariable=v_problem, font=FONT1)
E4.place(x=150, y=200)


L = Label(GUI,text='หมายเลข',font=FONT1)
L.place(x=30, y=250)

v_serial = StringVar()
E5 = Entry(GUI, textvariable=v_serial, font=FONT1)
E5.place(x=150, y=250)



L = Label(GUI,text='หมายเลขโทรศัพท์',font=FONT1)
L.place(x=30, y=300)

v_phone = StringVar()
E6 = Entry(GUI, textvariable=v_phone, font=FONT1)
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
                tsid = str(uuid.uuid4())
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
        


B = Button(GUI,text='บันทึกใบแจ้งหนี้', command=save, font=FONT1)
B.place(x=150, y=380)

GUI.mainloop() # ทำให้โปรแกรมรันตลอดเวลา