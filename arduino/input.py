import sqlite3
database = "../db.sqlite3"
conn = None
try:
    conn = sqlite3.connect(database)
except:
    exit(-1)

cur = conn.cursor()
class_name = input("Enter the classname : ")
query = "SELECT id FROM 'viewattendance_classroom' where class_id='{}'".format(class_name)
cur.execute(query)
rows = cur.fetchall()[0][0]

query = "SELECT student_name,roll_no FROM 'viewattendance_student' where class_id_id={}".format(rows)
cur.execute(query)
rows = cur.fetchall()

f = open("./template.ino", "r")
text = f.read()
f.close()
f = open("./outputs/"+class_name+".ino", "w")
result = ""
result += "\nswitch (finger.fingerID) { "
for row in rows:
    result += "\n case "+str(row[1])+":\n   lcd.print(\""+row[0]+"\");\n   break;"
result += "\n default:\n   lcd.print(\"error\");\n}\n"
text = text.replace("$replacetext", result)
f.write(text)
f.close()
