import fileinput
import sys

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)


def createCSV():
    import csv

    f = open('KaggleResult.csv', 'wt')
    try:
        writer = csv.writer(f)
        writer.writerow(('Id','Prediction'))
        count = 1
        newFile = open('/Users/manpreet.singh/Sandbox/codehub/github/machinelearning/BeingDataScientist/vowpal_wabbit/vw_apps/spam/src/p_out_kaggle.txt', 'r')
        for line in newFile.xreadlines():
            print line
            writer.writerow((count, line.strip()))
            count+=1
    finally:
        f.close()
        newFile.close()

if __name__ == '__main__':
    #replaceAll("p_out_kaggle.txt", "-1", "0")
    createCSV()


