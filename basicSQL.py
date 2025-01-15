import sqlite3


'''
 name = v_name.get()
    department = v_department.get()
    machine = v_machine.get()
    problem = v_problem.get()
    serial = v_serial.get()
    phone = v_phone.get()

'''

# Create a connection to the database
conn = sqlite3.connect('maintenance.sqlite3')

# Create a cursor object
c = conn.cursor()

c.execute("""

    CREATE TABLE IF NOT EXISTS mt_workorder (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                tsid INTEGER,
                name TEXT,
                department TEXT,
                machine TEXT,
                problem TEXT,
                serial TEXT,
                phone TEXT)""")

def insert_mtworkorder(tsid, name, department, machine, problem, serial, phone):
    # CREATE
    with conn:
        command = 'INSERT INTO mt_workorder VALUES (?,?,?,?,?,?,?,?)'
        c.execute(command, (None, tsid, name, department, machine, problem, serial, phone))

    conn.commit()
    print('saved')

# insert_mtworkorder('TS10001', 'ลุง', 'ไอที', 'เครื่องปริ้น', 'ปริ้นไม่ออก', 'SE2365214', '0863254154')



def view_mtworkorder():
    with conn:
        command = 'SELECT * FROM mt_workorder'
        c.execute(command)
        result = c.fetchall()

    print(result)
    return result

view_mtworkorder()