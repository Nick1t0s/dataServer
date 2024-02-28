import matplotlib.pyplot as plt
def getData(stlb):
    d2=[]
    import sqlite3 as sq
    with sq.connect("data.db") as con:
        cur=con.cursor()
        print(f"SELECT {', '.join(stlb)} FROM tepldata")
        x=cur.execute(f"SELECT {', '.join(stlb)} FROM data")
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
    return rotated
def createGrath(data,stlb):
    for i in range(len(data)):
        plt.plot(data[i],label=stlb[i])
    plt.legend(loc=4)
    plt.show()
x=getData(["inT","inH"])
createGrath(x,["inT","inH"])