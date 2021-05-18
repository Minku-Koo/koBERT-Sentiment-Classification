import json, csv


tlist = []
for i in range(1,6): tlist.append(["before"+str(i),"after"+str(i)])

dictName = { # index and religion name
        "1":"신천지",
        "2":"기독교",
        "3":"천주교",
        "4":"불교",
        "5":"종교" }

def getSentimentsList(data):
    emotions = []

    for date in data:
        #print(data[date])
        for article in data[date]:
            #print(article)
            #print(data[date][article])
            emotions.extend( data[date][article][1] )
    return emotions

for tablelist in tlist:
    for tablename in tablelist:
        path = "./predict-comment/"
        with open(path+"finish-daum"+tablename+'-dict.json', encoding="utf-8") as json_file:
            data1 = json.load(json_file)
            
        with open(path+"finish-naver"+tablename+'-dict.json', encoding="utf-8") as json_file:
            data2 = json.load(json_file)

        emo1 = getSentimentsList(data1)
        emo2 = getSentimentsList(data2)

        f = open("./ttest/"+tablename+'.csv','w', newline='')
        wr = csv.writer(f)
        for e in (emo1+emo2):
            wr.writerow([e])
    




