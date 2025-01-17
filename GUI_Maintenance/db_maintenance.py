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
                phone TEXT)""")



def insert_mtworkorder(tsid, name, department, machine, problem, serial, phone):
    # CREATE
    with conn:
        command = 'INSERT INTO mt_workorder VALUES (?,?,?,?,?,?,?,?)'
        c.execute(command, (None, tsid, name, department, machine, problem, serial, phone))

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










if __name__ == '__main__':
    result = view_mtworkorder()
    print(result)