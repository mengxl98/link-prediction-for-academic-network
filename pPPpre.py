#!/usr/bin/python
# -*- coding: utf-8 -*-
import networkx as nx
import community
import csv
import os
import pickle

FF="field_is_part_of"
PF="paper_is_in_field"
AF="author_is_in_field"
PA="paper_is_written_by"
Pp="paper_publish_on"

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
    if row[2]==Pp:
        tmp=int(id[row[1]])
        tar[tmp]=row[0]

catelist = os.listdir("data/relation/")
for mydir in catelist:
    path="data/relation/"+mydir
    csv_reader = csv.reader(open(path))
    for row in csv_reader:
        if len(row)==0:
            continue
        G.add_edge(int(id[row[0]]), int(id[row[1]]))
        edge_list.append((int(id[row[0]]), int(id[row[0]])))

G = max(nx.connected_component_subgraphs(G), key=len)

non_edge_gen = nx.non_edges(G)
target_edge = []
for edge in non_edge_gen:
    if min(edge)>50000 and max(edge)>50000:
        target_edge.append(edge)

partition = community.best_partition(G)
for node in G.nodes():
    G.node[node]['community']= partition[node]


cn = nx.adamic_adar_index(G, target_edge)
ralist=[]
ral=[]
result={}
for each in cn:
    if each[2]>0:
        if each[0] in tar.keys() or each[1] in tar.keys():
            ral.append(each)

print(len(ral))
for key in tar:
    list=[]
    t=3
    tmp=[]
    for eachedge in ral:
        if eachedge[0]==key or eachedge[1]==key:
            list.append(eachedge)
    if len(list)>0:
        sortlist = sorted(list, key=lambda student: student[2], reverse=True)
        if len(sortlist)<3:
            t=len(sortlist)
        for i in range(t):
            edge=sortlist[i]
            ralist.append(sortlist[i])
            if edge[0] == key:
                tmp.append(edge[1])
            else:
                tmp.append(edge[0])
    else:
        continue
    if len(tmp)==0:
        print(key)
    result[tar[key]] =tmp
print(len(result))
with open("Pp2aa.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    for key in result:
        writer.writerow([key,result[key]])




