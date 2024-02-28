#argv rootPath
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
def checkFolder(path):
    x=os.listdir("\\".join(path))
    return x
def checkListFiles(files):
    return files
def readAndCheckFile(path):
    with open("\\".join(path)) as file:
        x=file.read()
    names=["datetime","inT","inH","outT","outH","SH","WL","light"]
    values=x.split('#')
    if len(names)!=len(values):
        paths.fileErr(path)
        return {"datetime": "0", "inT": 0, "inH": 0, "outT": 0, "outH": 0, "SH": 0, "WL": 0, "light": 0}
    data={}
    for i in range(len(names)):
        data[names[i]]=values[i]
    return data
def runwriteToDB():
    listFiles=checkFolder(pathRoot) #sys.argv[1]
    listFiles=checkListFiles(listFiles)
    for file in listFiles:
        path=pathRoot[:]
        path.append(file)
        print(path)
        data=readAndCheckFile(path)
        writeToDB(data)

import sqlite3 as sq
import sys
import os
import paths
pathRoot=["C:","f"]
import shutil
print(sys.argv)
print(paths.errPath)
print(paths.logPath)
print(paths.archivePath)
#paths.fileErr(["archive","xcvc.ty"])
#createDBAndTable()
#writeToDB({"datetime":"23","inT":23,"inH":20,"outT":22,"outH":21,"SH":100,"WL":200,"light":300})
print(runwriteToDB())