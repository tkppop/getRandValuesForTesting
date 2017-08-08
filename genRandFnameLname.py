# Author        : Prasanna Krishnan
# Date          : 2017-06-09
# Title         : Create random name for testing
# Description   : Create random name for testing
import csv
from random import randint
class genNames:
    def genRandomFnameLname(self):
        fname = "Firstname"
        lname = "Lastname"
        nameFile = "Test users.csv"
        f = open(nameFile, 'rt')
        fileReader = csv.reader(f)
        #passing it to a list since the file is small
        mycsvdata = list(fileReader)
        num = len(mycsvdata)
        x = randint(1,num-1)
        fname = mycsvdata[x][0]
        y=randint(1,num-1)
        lname = mycsvdata[y][1]
        f.close()
        return fname, lname