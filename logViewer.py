import futabaReader as fr
#import csv

def create3dView():

    csvFile = fr.readCsv(filename='CSV_OUTPUT\\formatedLog.csv')

    for row in csvFile:
        print row

    print csvFile.__class__
    print "Done"

if __name__ == "__main__":
    create3dView()
