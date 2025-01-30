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



def view_mtnote(tsid):

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
    pass