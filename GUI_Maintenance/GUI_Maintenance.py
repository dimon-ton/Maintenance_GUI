from tkinter import *
from tkinter import messagebox
from datetime import datetime
from tkinter import ttk

# import database
from db_maintenance import *


# Generate a unique tsid
import uuid


from tkcalendar import Calendar, DateEntry

GUI = Tk()

GUI.title('โปรแกรมซ๋อมบำรง By Dimon')

w = 1400
h = 600

ws = GUI.winfo_screenwidth()
hs = GUI.winfo_screenheight()

x = (ws/2)-(w/2)
y = (hs/2)-(h/2)

GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')


# GUI.geometry('1300x800+50+50')

# Font
FONT1 = ('Angsana New', 16)


############## TAB ##################
# s = ttk.Style()
# s.theme_create('MyStyle', parent='alt', settings={
#     'TNotebook':{'configure':{'tabmargins':[2,5,2,0]}},
#     'TNotebook.Tab':{'configure':{'padding':[10,5], 'font':('Angsana New', '12', 'bold')}}
# })
# s.theme_use('MyStyle')




# Create a Style object
style = ttk.Style()

# Configure the font for the 'TNotebook.Tab' element
style.configure("TNotebook.Tab", font=("Angsana New", 13), padding=[10,5])




Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)
T4 = Frame(Tab)
Tab.add(T1, text='ใบแจ้งซ่อม')
Tab.add(T2, text='ดูใบแจ้งซ่อม')
Tab.add(T3, text='อนุมัติให้ซ่อมแล้ว')
Tab.add(T4, text='รายการซ่อมเสร็จแล้ว')
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
                update_table()
            
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
header = ['TSID', "ชื่อ", "แผนก", "อุปกรณ์/เครื่อง", "อาการเสีย", "หมายเลข", "หมายเลขโทรศัพท์", "สถานะ"]
headerw = [100, 150, 120, 200, 200, 150, 150, 120]

mtworkorderlist = ttk.Treeview(T2, columns=header,show='headings', height=10)
mtworkorderlist.pack(pady=20)

# adjust font size and table larger
style = ttk.Style()
style.configure('Treeview.Heading', font=('Angsana New', 10, 'bold'))
style.configure('Treeview', rowheight=25, font=('Angsana New', 15))

for h, w in zip(header, headerw):
    mtworkorderlist.heading(h, text=h)
    mtworkorderlist.column(h, width=w, anchor='center')


mtworkorderlist.column('TSID', anchor='w')


def update_table():
    mtworkorderlist.delete(*mtworkorderlist.get_children()) # clear records in Treeview
    [mtworkorderlist.insert('', 'end', values=r[1:]) for r in view_mtworkorder_status('new')]



# page for editing record
def editPage_mtworkorder(event=None):

    select  = mtworkorderlist.selection()
    output = mtworkorderlist.item(select)


    op = output['values']

    tsid = op[0]
    name = op[1]
    department = op[2]
    machine = op[3]
    problem = op[4]
    serial = op[5]
    phone = f'0{op[6]}'
    

    GUI2 = Toplevel()
    GUI2.title('หน้าแก้ไขข้อมูลใบแจ้งซ่อม')
    GUI2.geometry('500x500')


    L = Label(GUI2,text='ใบแจ้งซ่อม',font=FONT1)
    L.place(x=80, y=13)

    L = Label(GUI2,text='ชื่อผู้แจ้ง',font=FONT1)
    L.place(x=30, y=50)

    v_name2 = StringVar()
    v_name2.set(name)
    E1 = ttk.Entry(GUI2, textvariable=v_name2, font=FONT1)
    E1.place(x=150, y=50)

    L = Label(GUI2,text='แผนก',font=FONT1)
    L.place(x=30, y=100)

    v_department2 = StringVar()
    v_department2.set(department)
    E2 = ttk.Entry(GUI2, textvariable=v_department2, font=FONT1)
    E2.place(x=150, y=100)

    L = Label(GUI2,text='อุปกรณ์/เครื่อง',font=FONT1)
    L.place(x=30, y=150)

    v_machine2 = StringVar()
    v_machine2.set(machine)
    E3 = ttk.Entry(GUI2, textvariable=v_machine2, font=FONT1)
    E3.place(x=150, y=150)

    L = Label(GUI2,text='อาการเสีย',font=FONT1)
    L.place(x=30, y=200)

    v_problem2 = StringVar()
    v_problem2.set(problem)
    E4 = ttk.Entry(GUI2, textvariable=v_problem2, font=FONT1)
    E4.place(x=150, y=200)


    L = Label(GUI2,text='หมายเลข',font=FONT1)
    L.place(x=30, y=250)

    v_serial2 = StringVar()
    v_serial2.set(serial)
    E5 = ttk.Entry(GUI2, textvariable=v_serial2, font=FONT1)
    E5.place(x=150, y=250)



    L = Label(GUI2,text='หมายเลขโทรศัพท์',font=FONT1)
    L.place(x=30, y=300)

    v_phone2 = StringVar()
    v_phone2.set(phone)
    E6 = ttk.Entry(GUI2, textvariable=v_phone2, font=FONT1)
    E6.place(x=150, y=300)

    def update():
        name = v_name2.get()
        department = v_department2.get()
        machine = v_machine2.get()
        problem = v_problem2.get()
        serial = v_serial2.get()
        phone = v_phone2.get()
        
        

        try:
            if name == '' or department == '' or machine == '' or problem == '' or serial == '' or phone == '':
                messagebox.showwarning('Error','กรุณากรอกข้อมูลให้ครบ')
            else:

                if messagebox.askyesno('หน้าต่างยืนยันการเปลี่ยนแปลง', 'คุณต้องการบันทึกข้อมูลการเปลี่ยนแปลงใช่หรือไม่?'):
                    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                    update_mtworkorder(tsid, 'name', name)
                    update_mtworkorder(tsid, 'department', department)
                    update_mtworkorder(tsid, 'machine', machine)
                    update_mtworkorder(tsid, 'problem', problem)
                    update_mtworkorder(tsid, 'serial', serial)
                    update_mtworkorder(tsid, 'phone', phone)

                    update_table()
                    GUI2.destroy()
                
                else:
                    return
                    
                text = f'วันที่: {dt}\n'
                text += f'ชื่อ: {name}\n'
                text += f'แผนก: {department}\n'
                text += f'อุปกรณ์/เครื่อง: {machine}\n'
                text += f'อาการเสีย: {problem}\n'
                text += f'หมายเลข: {serial}\n'
                text += f'หมายเลขโทรศัพท์: {phone}\n'
                messagebox.showinfo('ปรับปรุงข้อมูลสำเร็จ', text)

        except Exception as e:
            messagebox.showerror('Error', str(e))
            


    B = Button(GUI2,text='ปรับปรุงใบแจ้งหนี้', command=update, font=FONT1)
    B.place(x=150, y=380)



    GUI2.mainloop()




mtworkorderlist.bind('<Double-1>', editPage_mtworkorder)


def Delete_mtworkorder(event=None):

    select  = mtworkorderlist.selection()
    
    if select:
        output = mtworkorderlist.item(select)
        tsid = output['values'][0]

        check = messagebox.askyesno('ยืนยันการลบ', 'คุณต้องการลบข้อมูลใช่หรือไม่')

        if check:
            delete_mtworkorder(tsid)
            update_table()


mtworkorderlist.bind('<Delete>', Delete_mtworkorder)


########### right click menu ##################
def Approved():
    select  = mtworkorderlist.selection()
    
    if select:
        output = mtworkorderlist.item(select)
        tsid = output['values'][0]

        check = messagebox.askyesno('ยืนยันการเปลี่ยนสถานะ', 'คุณต้องการเปลี่ยนสถานะใช่หรือไม่')

        if check:
            update_mtworkorder(tsid, 'status', 'approved')
            update_table()
            update_table_approved_wlist()




approved_menu = Menu(GUI, tearoff=0)
approved_menu.add_command(label='Approved', command=Approved)
approved_menu.add_command(label='delete', command=Delete_mtworkorder)


def popup(event):
    approved_menu.post(event.x_root, event.y_root)


mtworkorderlist.bind('<Button-3>', popup)


######################## TAB3 ################################

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



class MenuText(ttk.Label):
    def __init__(self, GUI, text="example", size=20):
        ttk.Label.__init__(self, GUI, text=text, font=('Angsana New', size, 'bold'), foreground='black')



# Table of Approved List

L = MenuText(T3, 'ตารางแสดงอนุมัติให้ซ่อม', 30)
L.pack(pady=(15,0))

approved_wlist = WorkorderList(T3)
approved_wlist.pack(pady=15)



def update_table_approved_wlist():
    approved_wlist.delete(*approved_wlist.get_children()) # clear records in Treeview
    [approved_wlist.insert('', 'end', values=r[1:]) for r in view_mtworkorder_status('approved')]




def Newnote(event):
    GUI3 = Toplevel()
    GUI3.geometry('500x580')
    GUI3.title('รายละเอียดการซ๋อม')

    select  = approved_wlist.selection()
    
    if select:
        output = approved_wlist.item(select)
        tsid = output['values'][0]




    FONT4 = (None, 15)
    L = ttk.Label(GUI3, text="รายละเอียดการซ่อม (tsid): {}".format(tsid), font=FONT4)
    L.pack(pady=10)



    
    v_date = StringVar()
    v_detail = StringVar()
    v_other = StringVar()



    L = ttk.Label(GUI3, text="วันที่เริ่ม", font=FONT4)
    L.pack(pady=10)


    cal = DateEntry(GUI3, width=18, background='white', foreground='black', borderwidth=1, year=2025)
    cal.configure(showweeknumbers=False)  # Hide week numbers
    cal.configure(date_pattern='y-mm-dd')  # Set the date format
    cal.configure(font=FONT4)  # Set the font to match other Entry widgets
    cal.configure(state='readonly')  # Make it readonly to prevent manual editing
    cal.pack()


    L = ttk.Label(GUI3, text="รายละเอียดงานซ่อม", font=FONT4)
    L.pack(pady=10)
    E2 = Text(GUI3, font=FONT4, width=35, height=5)
    E2.pack()


    L = ttk.Label(GUI3, text="หมายเหตุ", font=FONT4)
    L.pack(pady=10)
    E3 = Text(GUI3, font=FONT4, width=35, height=5)
    E3.pack()


    # get data from newnote
    data = view_mtnote_tsid(tsid)

    print(data)

    if data != None:
        cal.set_date(data[2])
        E2.insert(END, data[3])
        E3.insert(END, data[4])
    
    def SaveDetail():

        date_start = cal.get()
        detail = E2.get('1.0', END).strip()
        other = E3.get('1.0', END).strip()
        
        data = view_mtnote_tsid(tsid)

        if data == None:
            insert_mtnote(tsid, date_start, detail, other)
            messagebox.showinfo('save dialog box','saved successfully')




    B = ttk.Button(GUI3, text='save', command=SaveDetail)
    B.pack(pady=(60,0))



    GUI3.mainloop()



approved_wlist.bind('<Double-1>', Newnote)




update_table()
update_table_approved_wlist()

GUI.mainloop() # ทำให้โปรแกรมรันตลอดเวลา