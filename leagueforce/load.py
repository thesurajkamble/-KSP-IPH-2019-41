import pandas as pd
import csv
name=[]
i=0
a=[2,3]
com1=[]
data=pd.read_csv("people.csv")
m=data['name']
while(i<=len(a)-1):
            n=m[a[i]-1]
            i=i+1
            com1.append(n)
            with open('attendance.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow(com1)

