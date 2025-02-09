import sqlite3


# get path of parent directory
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
databse_path = os.path.join(BASE_DIR, 'maintenance.sqlite3')



# Create a connection to the database
conn = sqlite3.connect(databse_path)

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
                phone TEXT,
                status TEXT)""")




c.execute(""" CREATE TABLE IF NOT EXISTS mt_note (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            tsid TEXT,
            date_start TEXT,
            detail TEXT,
            other TEXT
          
          ) """)


# Department Table
c.execute(""" CREATE TABLE IF NOT EXISTS department (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            dep_code TEXT,
            dep_title TEXT
          
          ) """)


# Machine Equipment Table
c.execute(""" CREATE TABLE IF NOT EXISTS machine_equipment (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            mc_code TEXT,
            mc_title TEXT,
            mc_detail TEXT,
            dep_code TEXT
          
          ) """)


# Spare Part Table
c.execute(""" CREATE TABLE IF NOT EXISTS sparepart (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            sp_code TEXT,
            sp_title TEXT,
            sp_detail TEXT,
            sp_quantity INTEGER,
            sp_reorderpoint INTEGER
          
          ) """)



def view_department():

    with conn:
        command = 'SELECT * FROM department'
        c.execute(command)
        result = c.fetchall()

    return result

def insert_department(dep_code, dep_title):
    with conn:
        command = 'INSERT INTO department VALUES (?,?,?)'
        c.execute(command, (None, dep_code, dep_title))
    conn.commit()

def update_department(dep_code, field, newvalue):
    with conn:
        command = 'UPDATE department SET {} = (?) WHERE dep_code = (?)'.format(field)
        c.execute(command, (newvalue, dep_code))
    conn.commit()

def delete_department(dep_code):

    with conn:
        command = 'DELETE FROM department WHERE dep_code = (?)'
        c.execute(command, (dep_code,))
    conn.commit()



def view_machine_equipment():

    with conn:
        command = 'SELECT * FROM machine_equipment'
        c.execute(command)
        result = c.fetchall()

    return result

def insert_machine_equipment(mc_code, mc_title, mc_detail, dep_code):
    with conn:
        command = 'INSERT INTO machine_equipment VALUES (?,?,?,?,?)'
        c.execute(command, (None, mc_code, mc_title, mc_detail, dep_code))
    conn.commit()


def update_machine_equipment(mc_code, field, newvalue):
    with conn:
        command = 'UPDATE machine_equipment SET {} = (?) WHERE mc_code = (?)'.format(field)
        c.execute(command, (newvalue, mc_code))
    conn.commit()

def delete_machine_equipment(mc_code):

    with conn:
        command = 'DELETE FROM machine_equipment WHERE dep_code = (?)'
        c.execute(command, (mc_code,))
    conn.commit()



def view_sparepart():

    with conn:
        command = 'SELECT * FROM sparepart'
        c.execute(command)
        result = c.fetchall()

    return result

def insert_sparepart(sp_code, sp_title, sp_detail, sp_quantity, sp_reorderpoint):
    with conn:
        command = 'INSERT INTO sparepart VALUES (?,?,?,?,?,?)'
        c.execute(command, (None, sp_code, sp_title, sp_detail, sp_quantity, sp_reorderpoint))
    conn.commit()

def update_sparepart(sp_code, field, newvalue):
    with conn:
        command = 'UPDATE sparepart SET {} = (?) WHERE sp_code = (?)'.format(field)
        c.execute(command, (newvalue, sp_code))
    conn.commit()

def delete_sparepart(sp_code):

    with conn:
        command = 'DELETE FROM sparepart WHERE sp_code = (?)'
        c.execute(command, (sp_code,))
    conn.commit()




def insert_mtworkorder(tsid, name, department, machine, problem, serial, phone):
    # CREATE
    with conn:
        command = 'INSERT INTO mt_workorder VALUES (?,?,?,?,?,?,?,?,?)'
        c.execute(command, (None, tsid, name, department, machine, problem, serial, phone, 'new'))

    conn.commit()



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



def delete_mtworkorder(tsid):

    with conn:
        command = 'DELETE FROM mt_workorder WHERE tsid = (?)'
        c.execute(command, (tsid,))
    conn.commit()




def view_mtworkorder_status(status):
    with conn:
        command = 'SELECT * FROM mt_workorder WHERE status = ?'
        c.execute(command, (status, ))
        result = c.fetchall()

    return result


#####################################################


def insert_mtnote(tsid, date_start, detail, other):
    with conn:
        command = 'INSERT INTO mt_note VALUES (?,?,?,?,?)'
        c.execute(command, (None, tsid, date_start, detail, other))
    conn.commit()


def view_mtnote():

    with conn:
        command = 'SELECT * FROM mt_note'
        c.execute(command)
        result = c.fetchall()

    return result



def view_mtnote_tsid(tsid):

    with conn:
        command = 'SELECT * FROM mt_note WHERE tsid=(?)'
        c.execute(command, ([tsid]))
        result = c.fetchone()

    return result




def update_mtnote(tsid, field, newvalue):
    with conn:
        command = 'UPDATE mt_note SET {} = (?) WHERE tsid = (?)'.format(field)
        c.execute(command, (newvalue, tsid))
    conn.commit()


def delete_mtnote(tsid):

    with conn:
        command = 'DELETE FROM mt_note WHERE tsid = (?)'
        c.execute(command, (tsid,))
    conn.commit()




if __name__ == '__main__':
    alldata = view_mtnote()
    print(alldata)
    print(view_mtnote_tsid('MT12127779'))