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

insert_mtworkorder('TS10002', 'สมชาย', 'ไอที', 'หน้าจอ', 'เปิดไม่ติด', 'SE2375214', '0863754154')



def view_mtworkorder():
    with conn:
        command = 'SELECT * FROM mt_workorder'
        c.execute(command)
        result = c.fetchall()

    return result

def update_mtworkorder(tsid, field, newvalue):
    with conn:
        command = 'UPDATE mt_workorder SET {} = (?) WHERE tsid = (?)'.format(field)
        c.execute(command, (newvalue, tsid))
    conn.commit()

    print('database updated')



def delete_mtworkorder(tsid):

    with conn:
        command = 'DELETE FROM mt_workorder WHERE tsid = (?)'
        c.execute(command, (tsid,))
    conn.commit()
    print(f'database id {tsid} was deleted.')

