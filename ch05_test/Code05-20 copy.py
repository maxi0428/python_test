inFp = None 
inList, inStr = [], ""

inFp = open("test.txt", "r", encoding="utf-8" )
#inFp = open("C:/Temp/data1.txt", "r")
i= 0
inList = inFp.readlines()
for inStr in inList :
    i += 1
    print("%d : %s"%(i,inStr), end="")


inFp.close()
