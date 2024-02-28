import matplotlib.pyplot as plt
d2=[]
import sqlite3 as sq
with sq.connect("data.db") as con:
    cur=con.cursor()
    print(f"SELECT  FROM tepldata")
    x=cur.execute(f"SELECT inT FROM data")
    y=x.fetchall()
    for row in y:
#        print(list(row))
        d2.append(list(row))
"""d21=[[] for i in range(len(row))]
#print(*d21,sep="\n")
for i in range(len(d2)):
    for j in range(len(d2[0])):
        d21[j].append(d2[i][j])"""
print(*d2,sep="\n")
print()
rotated = tuple(zip(*d2[::-1])) # Python 3
print(*rotated,sep="\n")