import datetime,random
x=datetime.datetime.now()
print(x.strftime("%d.%m.%Y %H:%M:%S"))
def t():
    return random.randint(10,30)
def h():
    return random.randint(50,80)
def sh():
    return random.randint(200,600)
def generateFile(path,startDT,inter,count):
#    for i in range()
    st=datetime.datetime.strptime(startDT,"%d#%m#%Y#%H#%M#%S")
    for _ in range(count):
        st+=datetime.timedelta(minutes=inter)
        p2="\\".join(path)+"\\"+st.strftime("%d#%m#%Y#%H#%M#%S")+".txt"
        with open(p2,"w") as file:
            file.write(f"{st.strftime("%d.%m.%Y %H:%M:%S")}#{t()}#{h()}#{t()}#{h()}#{sh()}#{sh()}#{sh()}")
generateFile(["C:","f"],"22#11#2022#23#11#42",12,100)