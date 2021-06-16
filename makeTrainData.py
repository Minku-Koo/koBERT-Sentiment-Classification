import json
import math
import csv

def labeling(paths, filename):
    savepath = "./train-data/humanInspection/"
    with open(paths+filename+".json", "rt" , encoding="utf-8") as json_file:
        data = json.load(json_file)
    commentlist = []
    for date in data:
        for article in data[date]:
            for comment in data[date][article][0]:
                # print("comment", comment)
                if len(comment)<5 : continue
                commentlist.append(comment)

    count=0
    values = []
    # print(commentlist[:10])
    while count<100:
        print( count,")" ,commentlist[count].replace("\n","") )
        value = input(">>")
        if value not in ['0', '1']: 
            count += 1
            continue
        values.append( int(value))
        count += 1

    f = open(savepath+filename+"-train.tsv", "wt" ,  encoding='utf-8', newline='')
    wr = csv.writer(f, delimiter='\t')
    for i, v in enumerate(values):
        wr.writerow([commentlist[i].replace("\n"," "), v])
    print(filename+"--end")

tlist = []
for i in range(1,6): tlist.append(["before"+str(i),"after"+str(i)])

filename = "./train-data/makeTrainData.tsv"
commentpath = "./json-okt-comment/"

for tname in tlist:
    potal = "daum"
    for t in tname:
        if t in ["daumafter1-dict-train", "daumbefore1-dict-train"]: continue
        labeling(commentpath, potal+t+"-dict")

    potal = "naver"
    for t in tname:
        labeling(commentpath, potal+t+"-dict")


