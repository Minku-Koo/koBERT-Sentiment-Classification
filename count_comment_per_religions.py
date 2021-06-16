import json
import math
import csv

def count_comment(paths, filename):
    with open(paths+filename+".json", "rt" , encoding="utf-8") as json_file:
        data = json.load(json_file)
    commentlist = []
    for date in data:
        for article in data[date]:
            for comment in data[date][article][0]:
                commentlist.append(comment)

    return len(commentlist)

tlist = []
for i in range(1,6): tlist.append(["before"+str(i),"after"+str(i)])

commentpath = "./json-okt-comment/"
for tname in tlist:
    potal = "daum"
    for t in tname:
        filename = potal+t+"-dict"
        count = count_comment(commentpath, filename)
        print(f'{filename} 댓글 개수 : {count}개')

    potal = "naver"
    for t in tname:
        filename = potal+t+"-dict"
        count = count_comment(commentpath, filename)
        print(f'{filename} 댓글 개수 : {count}개')
