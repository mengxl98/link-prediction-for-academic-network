import csv

PF="paper_is_in_field"
AF="author_is_in_field"
PP="paper_cit_paper"
FF="field_is_part_of"
PA="paper_is_written_by"
AI="work_in"
Pp="paper_publish_on"
paper=[]
author=[]
field=[]
publisher=[]
inst=[]
t=0
csv_reader = csv.reader(open('train.csv', encoding='utf-8'))
for row in csv_reader:
    t=t+1
    if t%1000==0:
        print(t)
    relation=row[1]
    if relation==PF:
        paper.append(row[0])
        field.append(row[2])
    if relation==AF:
        author.append(row[0])
        field.append(row[2])
        with open("data1/AF.csv", "a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([row[0], row[2]])
    if relation==PP:
        paper.append(row[0])
        paper.append(row[2])
        with open("data1/PP.csv", "a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([row[0], row[2]])
    if relation==FF:
        field.append(row[0])
        field.append(row[2])
        with open("data1/FF.csv", "a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([row[0], row[2]])
    if relation==PA:
        paper.append(row[0])
        author.append(row[2])
        with open("data1/PF.csv", "a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([row[0], row[2]])
    if relation==AI:
        author.append(row[0])
        inst.append(row[2])
        with open("data1/AI.csv", "a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([row[0], row[2]])
    if relation==Pp:
        paper.append(row[0])
        publisher.append(row[2])
        with open("data1/Pp.csv", "a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([row[0], row[2]])
    if relation==PA:
        paper.append(row[0])
        author.append(row[2])
        with open("data1/PA.csv", "a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([row[0], row[2]])

paper = list(set(paper))
with open("data1/paper.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    for p in paper:
        writer.writerow([p])
author = list(set(author))
with open("data1/author.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    for a in author:
        writer.writerow([a])
publisher = list(set(publisher))
with open("data1/publisher.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    for b in publisher:
        writer.writerow([b])
inst = list(set(inst))
with open("data1/inst.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    for i in inst:
        writer.writerow([i])
field = list(set(field))
with open("data1/field.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    for f in field:
        writer.writerow([f])