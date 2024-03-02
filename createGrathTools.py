import datetime
import matplotlib.pyplot as plt
def getData(stlb,startDate,stopDate):
    d2=[]
    import sqlite3 as sq
    with sq.connect("data.db") as con:
        cur=con.cursor()
        print(f"SELECT {', '.join(stlb)}, datetime FROM data WHERE datetime > '{startDate}' AND datetime < '{stopDate}'")
        x=cur.execute(f"SELECT {', '.join(stlb)}, datetime FROM data WHERE datetime > '{startDate}' AND datetime < '{stopDate}'")
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
def createGrath(data,stlb,tp):
    print(data[-1])
    if tp == 1:
        date = []
        counter = 1
        for i in data[-1]:
            dateOne = datetime.datetime.strptime(i, "%d-%m-%Y %H:%M:%S")
            print(dateOne)
            if (0 <= dateOne.minute < 4 or 56 < dateOne.minute <= 59) and dateOne.hour%2==0:
                date.append(dateOne.strftime("%H:%M"))
            else:
                date.append(' ')
    date.reverse()
    print(date)
    for i in range(len(stlb)):
        plt.plot(data[i],label=stlb[i])
    plt.xticks(,labels=["one", "two", "three", "one"])
    plt.legend(loc=4)
    plt.show()
x=getData(["inT","inH"],"22-11-2022 10:8:0","22-11-2022 13:55:0")
createGrath(x,["inT","inH"],1)