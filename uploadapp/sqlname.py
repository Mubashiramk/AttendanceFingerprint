import sqlite3
database = "../db.sqlite3"
conn = None
try:
    conn = sqlite3.connect(database)
except:
    exit(-1)
cur = conn.cursor()
rollno = input("enter roll no: ")
query = "SELECT student_name FROM 'viewattendance_student' where roll_no={}".format(rollno)
cur.execute(query)
rows = cur.fetchall()
for row in rows:
    print(row[0])
"""student_id	student_name	class_id_id	roll_no"""
