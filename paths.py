import os,shutil
localPath=os.getcwd().split("\\")
archivePath=localPath[:]
archivePath.append("archive")
errPath=localPath[:]
errPath.append("err")
logPath=localPath[:]
logPath.append("logs")
def mkDirs():
    if not os.path.isdir("\\".join(archivePath)): os.mkdir("\\".join(archivePath))
    if not os.path.isdir("\\".join(errPath)): os.mkdir("\\".join(errPath))
    if not os.path.isdir("\\".join(logPath)): os.mkdir("\\".join(logPath))
def fileErr(path):
    shutil.move("\\".join(path),f"{"\\".join(errPath)}\\{path[-1]}")