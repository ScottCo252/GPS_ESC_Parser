import xml.etree.ElementTree as et
import csv



def convertFutabaCsv():
    print "Open File!"

    gpsLatitude = []
    gpsLongitude = []
    gpsTime = []
    gpsLatLong = []

    with open('CSV\\LOG_RAW_YELLOW.csv', 'rb') as csvfile:
        fileReader = csv.reader(csvfile, delimiter=',')

        fileReader.next()
        fileReader.next()
        fileReader.next()
        fileReader.next()

        for row in fileReader:
            gpsLatitude.append(row[30])
            gpsLongitude.append(row[31])
            gpsTime.append(row[32])

    print "length : ", len(gpsTime)

    for i in range(len(gpsTime)):
        tempLat = gpsLatitude[i][2:gpsLatitude[i].find(":")]
        tempLat += "d "
        tempLat += gpsLatitude[i][(gpsLatitude[i].find(":") + 1):]
        tempLat += gpsLatitude[i][0:1]

        tempLong = gpsLongitude[i][1:gpsLongitude[i].find(":")]
        tempLong += "d "
        tempLong += gpsLongitude[i][(gpsLongitude[i].find(":") + 1):]
        tempLong += gpsLongitude[i][0:1]

        gpsLatLong.append(tempLat + ", " + tempLong)

    print gpsLatLong

    with open('CSV_OUTPUT\\formatedLog.csv', 'wb') as csvfile:
        outFile = csv.writer(csvfile, delimiter=',')

        outFile.writerow(['Latitude', 'Longitude', 'Lat-Long', 'Time'])

        for i in range(len(gpsTime)):
            outFile.writerow([gpsLatitude[i], gpsLongitude[i], gpsLatLong[i], gpsTime[i]])

def readCsv(filename):
    csvFile = []
    with open(filename, 'rb') as csvfile:
        fileReader = csv.reader(csvfile, delimiter=',')
        for row in fileReader:
            csvFile.append(row)

    return csvFile

if __name__ == "__main__":
    convertFutabaCsv()
