import tkinter as tk
import sqlite3

##fields = 'ID','NAME','AGE','ADDRESS','SALARY'
def fetch(entries):
    ls=[]
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        ls.append(entry[1].get())
        print('%s: "%s"' % (field, text))

    insertRecord_(int(ls[0]),ls[1],int(ls[2]),ls[3],float(ls[4]))

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='e')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
##    print (entries)
    return entries
def createTable():
    conn.execute('''CREATE TABLE COMPANY
             (ID INT PRIMARY KEY     NOT NULL,
             NAME           TEXT    NOT NULL,
             AGE            INT     NOT NULL,
             ADDRESS        CHAR(50),
             SALARY         REAL);''')
    print ("Table created successfully");

def insertRecord_(*args):
    conn.execute(f"INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)  VALUES ({args[0]}, '{args[1]}', {args[2]}, '{args[3]}', {args[4]} )");
    conn.commit()

def insertRecord():
    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

    conn.commit()
    print ("Records created successfully");

def select():
##    cursor = conn.execute("SELECT id, name, address, salary from COMPANY where salary>20000 and salary<50000 ")
##    cursor = conn.execute("SELECT id, name, address, salary from COMPANY where address='Tehran' ")
    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
       print ("ID = ", row[0])
       print ("NAME = ", row[1])
       print ("ADDRESS = ", row[2])
       print ("SALARY = ", row[3], "\n")

    print ("Operation done successfully")

def appEnd():
    root.quit()
    conn.close()
def delete(entries):
    id_=int(entries[0][1].get())
    print(id_)

    conn.execute(f"DELETE from COMPANY where ID = {id_};")
    conn.commit()
    print ("Total number of rows deleted :", conn.total_changes )

if __name__ == '__main__':
    root = tk.Tk()
    fields = 'ID','NAME','AGE','ADDRESS','SALARY'
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   

    b1 = tk.Button(root, text='Insert',
                  command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)

    b2 = tk.Button(root, text='Show', command=select)
    b2.pack(side=tk.LEFT, padx=5, pady=5)

    b4 = tk.Button(root, text='Delete',
                   command=(lambda e=ents: delete(e)))
    b4.pack(side=tk.LEFT, padx=5, pady=5)

    b3 = tk.Button(root, text='Quit', command=appEnd)
    b3.pack(side=tk.LEFT, padx=5, pady=5)

    conn = sqlite3.connect('test1.db')
    print ("Opened database successfully");
##    createTable()

    
    root.mainloop()
