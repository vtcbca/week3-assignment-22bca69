Write a python script to perform CRUD operation on following table of "ESM.db" database.

Employee ( eid, ename, dept, basic, branch). eid must be primary key.

Department : Account, Inventory, IT, HR.

Peform Following Operation.

1.from sqlite3 import *

conn = connect('C:\\sqlite3\\ESM.db')

cur = conn.cursor()

tbl = """create table Employee56
            (
                eid integer primary key,
                ename text,
                dept text,
                basic integer,
                branch text
            );"""

cur.execute(tbl)

conn.commit()

conn.close()

2. Insert 5 Records directly, 5 records using tuple and 5 records using taking input from user
->
from sqlite3 import *

conn = connect('C:\\sqlite3\\ESM.db')

cur = conn.cursor()

#record which insert directly are
"""
1|dev|it|65000|dungra
2|dhaval|account|45000|bardoli
3|dhruv|Inventory|50000|kathor
4|rudra|HR|65000|saki
5|arjun|it|2000|matel
"""

#record insert using tuple
"""
ins = [(6,'abhay','HR',50000,'Surat'),
            (7,'krunal','IT',70000,'Vyara'),
            (8,'himal','Inventory',5000,'Vyara'),
            (9,'umesh','HR',50000,'Rajasthan'),
            (10,'ravi','Account',20000,'Baroda'),
           ]

cur.executemany("insert into employee56 values(?,?,?,?,?)",ins)
"""

#record insert  from taking user input
mlis=[]
for i in range(5):
    tlis=[]
    eid = int(input('enter eid :'))
    tlis.append(eid)

    ename = input('enter ename :')
    tlis.append(ename)

    dept = input('enter dept :')
    tlis.append(dept)

    basic = int(input('enter salary :'))
    tlis.append(basic)

    branch = input('enter branch :')
    tlis.append(branch)

    mlis.append(tlis)

cur.executemany("insert into employee56 values(?,?,?,?,?)",mlis)
conn.commit()

conn.close()

3. Update records who are from "Surat" branch with increment in salary 10%.
->
from sqlite3 import *

conn = connect('C:\\sqlite3\\ESM.db')

curobj =  conn.cursor()

query = """update employee56
                    set basic = basic + (basic*10)/100\
                    where branch like 'Surat'"""

curobj.execute(query)

conn.commit()

conn.close()

4. Print All records.
->
from sqlite3 import *

conn = connect('C:\\sqlite3\\ESM.db')

curobj = conn.cursor()

query = "select * from employee56"

curobj.execute(query)

result = curobj.fetchall()

for i in result:
    print(i)

conn.commit()

conn.close()

5. Print records where dept is "HR" and "IT".
->
from sqlite3 import *

conn = connect('C:\\sqlite3\\ESM.db')

curobj = conn.cursor()

query = """select * from employee56
                where dept like 'HR' or dept like 'IT' """

curobj.execute(query)

result = curobj.fetchall()

for i in result:
    print(i)

conn.commit()

conn.close()
   
6. Print records in sorting order of department.
->
from sqlite3 import *

conn = connect('C:\\sqlite3\\ESM.db')

curobj = conn.cursor()

#ascending order
query = "select * from employee56 order by dept "

#descending order
"""
query = "select * from employee56 order by dept desc "
"""
curobj.execute(query)

result = curobj.fetchall()

for i in result:
    print(i)

conn.commit()

conn.close()

7. Print records where basic is >6000.
->
from sqlite3 import *

conn = connect('C:\\sqlite3\\ESM.db')

curobj = conn.cursor()

query = """select * from employee56\
                where basic>6000 """

curobj.execute(query)

result = curobj.fetchall()

for i in result:
    print(i)

conn.commit()

conn.close()

8. Print records whrere employee56 name second character is "r".
->
from sqlite3 import *

conn = connect('C:\\sqlite3\\ESM.db')

curobj = conn.cursor()

query = """select * from employee56\
                where basic>6000 """

curobj.execute(query)

result = curobj.fetchall()

for i in result:
    print(i)

conn.commit()

conn.close()

9. Grouping record of employee56 who are from "Account" and "Inventory".
->
from sqlite3 import *

conn = connect('C:\\sqlite3\\ESM.db')

curobj = conn.cursor()

query = """select * from employee56\
                  group by dept\
                  having dept like 'Account' or dept like 'Inventory'"""

curobj.execute(query)

result = curobj.fetchall()

for i in result:
    print(i)

conn.commit()

conn.close()

10. Print all records based on branch name in descending order.
->
from sqlite3 import *

conn = connect('C:\\sqlite3\\ESM.db')

curobj = conn.cursor()

query = """select * from employee56 order by branch desc"""

curobj.execute(query)

result = curobj.fetchall()

for i in result:
    print(i)

conn.commit()

conn.close()
