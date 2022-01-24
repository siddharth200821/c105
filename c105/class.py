import csv
import math
# to open and read the csv using with open
with open("c105.csv",newline="")as file:
    fileReader=csv.reader(file)
    #to convert the contents of file reader into a list
    filelist=list(fileReader)
#print(filelist)
#to remove the column names (first row-0th index)
fileReader.pop(0)
#to find the mean of a data
#to find the number of items inside file reader
n=len(fileReader)
#to find out the sum of all the items inside the fileReader
total=0
for i in fileReader:
    total+=i
mean=total/n
squarednumbers=[]
for i in fileReader:
    a=int(i)-mean
    a=a**2
    squarednumbers.append(a)
sum=0
for i in squarednumbers:
    sum=sum+i
result=sum/(n-1)
sd=math.sqrt(result)
print(sd)