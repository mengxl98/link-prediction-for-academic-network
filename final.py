import csv
import os
id={}
fh = open("idid.txt", 'r')
for eachline in fh:
    b=eachline.strip('\n').split('\t')
    id[(b[1])]=b[0]
fh.close()
catelist = os.listdir("result1/")

wri={}
for mydir in catelist:
        path = "result1/" + mydir
        csv_reader = csv.reader(open(path))
        for row in csv_reader:
            re=""
            if len(row) == 0:
                continue
            tmp=str(row[1])
            tmp=tmp.strip('[').strip(']').split(',')
            for key in tmp:
                key=key.strip()
                print(row[0])
                re=re+id[key]+" "
            wri[row[0]]=re

with open("resultpa.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["QueryId", "ExpectedTail"])
    for i in range(11529):
        tmp=i+1
        if str(tmp) in wri:
            writer.writerow([tmp, wri[str(tmp)]])
        else:
            writer.writerow([tmp,""])


