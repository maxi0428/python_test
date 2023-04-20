import csv
def printList(pList) :
    for data in pList :
        print(data, end='\t')
    print()

with open("CSV/singer2.csv", "r") as inFp :
    csvReader = csv.reader(inFp)
    header_list = next(csvReader)
    printList(header_list)
    for inStr in inFp:
        inStr = inStr.strip()
        row_list = inStr.split(',')
        printList(row_list)
 