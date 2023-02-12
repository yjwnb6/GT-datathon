import csv
def exportCSV() :
    bitcoinDict = {}
    with open ("C:/Users/黑暗在翻騰/Downloads/archive/dataset.csv", "r") as infile :
        header = infile.readline()
        header = header.strip().split(",")
        newList = infile. readlines()
        for i in range(0,len(newList)) :
            newList[i] = newList[i].strip()
            newList[i] = newList[i].split(",")
        newList.sort(key = abc)
        for i in newList :
            bitcoinDict[i[8]] = 0
        #print (newList)
    with open ("C:/Users/黑暗在翻騰/Downloads/archive/exportData.csv", "w", newline = "") as outfile :
        write = csv.writer(outfile, delimiter = ",")
        write.writerow(header)
        write.writerows(newList)
    for bitcoinName in bitcoinDict.keys() :    
        path = "C:/Users/黑暗在翻騰/Downloads/archive/dataset/{}Data.csv".format(bitcoinName)
        with open (path, "w", newline = "") as outfile :
            write = csv.writer(outfile, delimiter = ",")
            write.writerow(header)
            for i in newList :
                if i[8] == bitcoinName :
                    write.writerow(i)
def abc(de) :
    return de[8]
        
exportCSV()
