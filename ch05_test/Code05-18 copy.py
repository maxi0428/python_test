inFp = None	# 입력 파일
inStr = ""		# 읽어온 문자열

inFp = open("test.txt", "r", encoding="utf-8" )
#inFp = open("C:/Temp/data1.txt", "r")
i=0
while True :
    inStr = inFp.readline()
    if inStr == "" :
        break;
    i = i+1
    print("%d : %s" %(i,inStr), end = "")

inFp.close()
