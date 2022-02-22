import sqlite3
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

def update():
    conn.execute("UPDATE COMPANY set SALARY = SALARY*1.1 where ID >3")
    conn.commit()
    print ("Total number of rows updated :", conn.total_changes)

def delete():
    conn.execute("DELETE from COMPANY where ID = 2;")
    conn.commit()
    print ("Total number of rows deleted :", conn.total_changes )
if __name__=="__main__":
    conn = sqlite3.connect('test.db')
    print ("Opened database successfully");
    ##createTable()
    ##insertRecord()
    ##insertRecord_(5,'Ali',40,'Tehran',30000.00)
##    update()
    delete()
    select()
    conn.close()
