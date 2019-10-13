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
Pp="paper_publish_on"

G = nx.Graph()
edge_list=[]
id={}
fh = open("idid.txt", 'r')
for eachline in fh:
    b=eachline.strip('\n').split('\t')
    id[b[0]]=b[1]
fh.close()

tar=[]
csv_reader = csv.reader(open('test.csv', encoding='utf-8'))
for row in csv_reader:
    if row[2]==Pp:
        tar.append(int(row[0]))

aire={}
pcsv="Ppub.csv"
catelist = os.listdir("data/relation/")
for mydir in catelist:
    path="data/relation/"+mydir
    csv_reader = csv.reader(open(path))
    print(mydir)
    for row in csv_reader:
        if len(row)==0:
            continue
        if mydir == pcsv:
            aire[int(id[row[0]])] = int(id[row[1]])

print(len(aire))

f = csv.writer(open('Ppre_aa.csv', "a"))

ppub={}
with open("Ppreaa.csv", "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        if len(row)==0:
            continue
        inst=[]
        tmp = str(row[1])
        tmp = tmp.strip('[').strip(']').split(',')
        for key in tmp:
            key = key.strip()
            inst.append(int(key))
        if len(inst)==0:
            continue
        ppub[int(row[0])]=inst

print(len(ppub))
ppaper={}
with open("Pp2aa.csv", "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        if len(row)==0:
            continue
        inst=[]
        tmp = str(row[1])
        tmp = tmp.strip('[').strip(']').split(',')
        for key in tmp:
            key = key.strip()
            inst.append(int(key))
        if len(inst)==0:
            continue
        ppaper[int(row[0])]=inst

print(len(ppaper))
for key in tar:
    inst=[]
    if key in ppub:
        inst=ppub[key]
    if len(inst)==3:
        f.writerow([key, inst])
        continue
    if key not in ppaper:
        continue
    prep=ppaper[key]
    for paper in prep:
        if int(paper) in aire:
            pub=aire[int(paper)]
            inst.append(pub)
        if len(inst)==3:
            break
    if len(inst) == 0:
        continue
    f.writerow([key, inst])


