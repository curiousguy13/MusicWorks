inFile = open("NotDone.txt",'r')

outFile = open("NotDoneList.txt",'w')


List = (inFile.read()).split("\', \'")


for path in List:
    outFile.write(path+"\n")
    
