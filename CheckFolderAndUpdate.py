#argv rootPath DBPath NameTAble
def createDBAndTable():
    with sq.connect("data.db") as con: #argv[1]
        cur=con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS data (
        datetime TEXT,
        inT INTAGER,
        inH INTAGER,
        outT INTAGER,
        outH INTAGER,
        SH INTAGER,
        WL INTAGER,
        light INTAGER
        )
        """)
def writeToDB(data):
    command=f"""INSERT INTO data VALUES(
    '{data["datetime"]}', 
    {data["inT"]}, 
    {data["inH"]}, 
    {data["outT"]}, 
    {data["outH"]}, 
    {data["SH"]}, 
    {data["WL"]}, 
    {data["light"]}
    )"""
    with sq.connect("data.db") as con: #sys.argv[1]
        cur=con.cursor()
        cur.execute(command)
import sqlite3 as sq
import sys
print(sys.argv)
createDBAndTable()
writeToDB({"datetime":"23","inT":23,"inH":20,"outT":22,"outH":21,"SH":100,"WL":200,"light":300})