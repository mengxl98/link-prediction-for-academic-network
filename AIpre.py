import networkx as nx
import community
import csv
import os
import pickle

FF="field_is_part_of"
PF="paper_is_in_field"
AF="author_is_in_field"
PA="paper_is_written_by"
AI="work_in"

G = nx.Graph()
edge_list=[]
id={}
fh = open("idid.txt", 'r')
for eachline in fh:
    b=eachline.strip('\n').split('\t')
    id[b[0]]=b[1]
fh.close()
tar={}
csv_reader = csv.reader(open('test.csv', encoding='utf-8'))
for row in csv_reader:
    if row[2]==AI:
        tmp=int(id[row[1]])
        tar[tmp]=row[0]

aire={}
acsv="AI.csv"
catelist = os.listdir("data/relation/")
for mydir in catelist:
    path="data/relation/"+mydir
    csv_reader = csv.reader(open(path))
    print(mydir)
    for row in csv_reader:
        if len(row)==0:
            continue
        if mydir == acsv:
            aire[int(id[row[0]])] = int(id[row[1]])

f = csv.writer(open('AIpre.csv', "w"))

with open("AApre.csv", "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        t=0
        inst=[]
        tmp = str(row[1])
        tmp = tmp.strip('[').strip(']').split(',')
        for key in tmp:
            t=t+1

            if len(inst)>=3:
                break
            key = key.strip()
            if int(key) in aire:
                inst.append(aire[int(key)])
        if len(inst)==0:
            continue
        f.writerow([row[0],inst])

