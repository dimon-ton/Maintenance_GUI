from tkinter import *
from tkinter import messagebox
from datetime import datetime
from tkinter import ttk
from allpage import *

# import database
from db_maintenance import *

# Generate a unique tsid
import uuid
from tkcalendar import Calendar, DateEntry

def center_windows(w, h):

    ws = GUI.winfo_screenwidth()
    hs = GUI.winfo_screenheight()

    x = (ws/2)-(w/2)
    y = (hs/2)-(h/2)

    return f'{w}x{h}+{x:.0f}+{y:.0f}'


GUI = Tk()
GUI.title('โปรแกรมซ๋อมบำรง By Dimon')

w = 1400
h = 600

GUI.geometry(center_windows(w, h))



# GUI.geometry('1300x800+50+50')

# Font
FONT1 = ('Angsana New', 14)


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


############################################### Menu Bar ###################################################
# Main Menu
menubar = Menu(GUI)
GUI.config(menu=menubar)
# File
menu_file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=menu_file)

menu_file.add_command(label='Sync')
menu_file.add_command(label='Update Database')

def Report():
    messagebox.showinfo('Report', 'ตอนนี้ Report ยังไม่พร้อมใช้งาน')

sub_menu = Menu(menu_file, tearoff=0)
sub_menu.add_command(label='config database')
sub_menu.add_command(label='config report', command=Report)

menu_file.add_cascade(label='Config', menu=sub_menu)

menu_file.add_separator()

menu_file.add_command(label='Exit', accelerator='Ctrl + Q', command=lambda: GUI.quit())
GUI.bind('<Control-q>', lambda x: GUI.quit())


# Help

menu_help = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=menu_help)

menu_help.add_command(label='About')
menu_help.add_command(label='Update Software')
menu_help.add_command(label='Contact Developer')
menu_help.add_command(label='Donate')


############################################### Notebook ###################################################

Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)
T4 = Frame(Tab)
Tab.add(T1, text='เมนูหลัก')
Tab.add(T2, text='ดูใบแจ้งซ่อม')
Tab.add(T3, text='อนุมัติให้ซ่อมแล้ว')
Tab.add(T4, text='รายการซ่อมเสร็จแล้ว')
Tab.pack(fill=BOTH, expand=1)



######################## FUNCTION ###########################
def update_table():
    mtworkorderlist.delete(*mtworkorderlist.get_children()) # clear records in Treeview
    [mtworkorderlist.insert('', 'end', values=r[1:]) for r in view_mtworkorder_status('new')]

########################### MTWorkorder ################################
def WindowMTWorkorder():
    GUI2 = Toplevel()
    GUI2.geometry(center_windows(600, 500))
    GUI2.title('ใบแจ้งซ่อม')
    GUI2.transient(GUI) # set Toplevel only in front of main GUI
    GUI2.grab_set() # disable main GUI while Toplevel is on

    F1 = MTWorkorder(GUI2, insert_mtworkorder, update_table)
    F1.pack()

    GUI2.mainloop()

FBM1 = Frame(T1)
FBM1.place(x=50, y=45)
icon_bm1 = PhotoImage(file='mtworkorder.png')
BM1 = ttk.Button(FBM1, text='ใบแจ้งซ่อม', image=icon_bm1, compound='top',command=WindowMTWorkorder)
BM1.pack(ipadx=30, ipady=15, pady=(20,0))



########################### Department ################################
def WindowDepartment():
    GUI3 = Toplevel()
    GUI3.geometry(center_windows(600, 500))
    GUI3.title('เพิ่ม/ลด แผนก')
    GUI3.transient(GUI)
    GUI3.grab_set()

    MenuText(GUI3, 'เพิ่ม/ลด แผนก', 20).pack(pady=(20,20))

    v_dep_code = StringVar()

    E1 = ET(GUI3, label='รหัสแผนก', textvariable=v_dep_code)
    E1.place(x=50, y=50)


    v_dep_title = StringVar()

    E2 = ET(GUI3, label='ชื่อแผนก', textvariable=v_dep_title)
    E2.place(x=50, y=100)



    def saveDep():
        dep_code = v_dep_code.get()
        dep_title = v_dep_title.get()
        insert_department(dep_code, dep_title)
        v_dep_code.set('')
        v_dep_title.set('')
        E1.E1.focus()

    B = ttk.Button(GUI3, text='บันทึก', command=saveDep)
    B.place(x=50, y=190, width=100, height=40)

    # Apply font size and style
    B.config(style="Custom.TButton")

    style = ttk.Style()
    style.configure("Custom.TButton", font=("Angsana New", 14))  # Adjust font family and size

    GUI3.mainloop()

FBM1 = Frame(T1)
FBM1.place(x=200, y=45)
icon_bm2 = PhotoImage(file='department.png')
BM1 = ttk.Button(FBM1, text='สร้างแผนก', image=icon_bm2, compound='top', command=WindowDepartment)
BM1.pack(ipadx=30, ipady=15, pady=(20,0))




# F1 = MTWorkorder(T1, insert_mtworkorder, update_table)
# F1.pack()

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


    L = Label(GUI2,text='ใบแจ้งซ่อม',font=('Angsana New',18))
    L.place(x=200, y=13)

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



class ET(Frame):
    def __init__(self, GUI, label, textvariable, FONT=('Angsana New', 15)):
        Frame.__init__(self, GUI, width=500, height=500)

        self.L1 = ttk.Label(self, text=label, font=FONT)
        self.L1.place(x=0, y=20)
        self.E1 = ttk.Entry(self, textvariable=textvariable, font=FONT)
        self.E1.place(x=90, y=20)




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


    GUI3.bind('<F1>', lambda x: E3.focus())
    
    # get data from newnote
    data = view_mtnote_tsid(tsid)

    print(data)

    if data != None:
        cal.set_date(data[2])
        E2.insert(END, data[3])
        E3.insert(END, data[4])
    
    def SaveDetail(event=None):
        
        date_start = cal.get()
        detail = E2.get('1.0', END).strip()
        other = E3.get('1.0', END).strip()
        
        data = view_mtnote_tsid(tsid)


        if data == None:
            insert_mtnote(tsid, date_start, detail, other)
            messagebox.showinfo('save dialog box','saved successfully')
        else:
            update_mtnote(tsid, 'date_start', date_start)
            update_mtnote(tsid, 'detail', detail)
            update_mtnote(tsid, 'other', other)
            messagebox.showinfo('update dialog box','updated successfully' )

        GUI3.destroy()



    B = ttk.Button(GUI3, text='save', command=SaveDetail)
    B.pack(pady=(60,0))



    GUI3.mainloop()



approved_wlist.bind('<Double-1>', Newnote)

########### right click menu ##################
def Done():
    select  = approved_wlist.selection()
    
    if select:
        output = approved_wlist.item(select)
        tsid = output['values'][0]

        check = messagebox.askyesno('ยืนยันการเปลี่ยนสถานะ', 'คุณต้องการเปลี่ยนสถานะใช่หรือไม่')

        if check:
            update_mtworkorder(tsid, 'status', 'done')
            update_table()
            update_table_approved_wlist()
            update_table_done_wlist()


done_menu = Menu(GUI, tearoff=0)
done_menu.add_command(label='done', command=Done)

def popup(event):
    done_menu.post(event.x_root, event.y_root)


approved_wlist.bind('<Button-3>', popup)

########################## TAB 4 ###########################

# Table of Approved List

L = MenuText(T4, 'ตารางแสดงรายการซ่อมเสร็จแล้ว', 30)
L.pack(pady=(15,0))

done_wlist = WorkorderList(T4)
done_wlist.pack(pady=15)



def update_table_done_wlist():
    done_wlist.delete(*done_wlist.get_children()) # clear records in Treeview
    [done_wlist.insert('', 'end', values=r[1:]) for r in view_mtworkorder_status('done')]

update_table()
update_table_approved_wlist()
update_table_done_wlist()

GUI.mainloop() # ทำให้โปรแกรมรันตลอดเวลา