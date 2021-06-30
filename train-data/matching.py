import csv

def compair(filename, origin_data, worked_data):
    result = []
    for d in origin_data:
        text = d.split("\t")[0]
        if text not in worked_data:
            result.append( [text, "FALSE"] )

    if result == []: return

    path = "./addwork/"
    with open(path + filename + ".tsv", 'w', newline='', encoding='utf-8') as tsvout:
        tsvout = csv.writer(tsvout, delimiter='\t')

        for row in result:
            tsvout.writerow(row)
            
    return result

worked = "./humanInspection/"
origin = "./work_tsv_files_[10%]/"

tlist = []
for i in range(1,6): tlist.append(["before"+str(i),"after"+str(i)])

result  = 0
for period in tlist:
    for t in period:
        
        file = "daum"+t
        try:
            with open(worked+file+"-dict.tsv", "rt", encoding="utf-8") as f:
                worked_data = f.read()
                l1 = len(worked_data.strip("\n").split("\n") )
        except:
            worked_data = ""
            l1 = 0

        with open(origin+file+"-dict.tsv", "rt", encoding="utf-8") as f:
            origin_data = f.readlines()
            l2 = len(origin_data )

        if l1 != l2: compair(file, origin_data, worked_data)



        file = "naver"+t
        try:
            with open(worked+file+"-dict.tsv", "rt", encoding="utf-8") as f:
                worked_data = f.read()
                l1 = len(worked_data.strip("\n").split("\n") )
        except:
            worked_data = ""
            l1 = 0
        with open(origin+file+"-dict.tsv", "rt", encoding="utf-8") as f:
            origin_data = f.readlines()
            l2 = len(origin_data )

        if l1 != l2: compair(file, origin_data, worked_data)


