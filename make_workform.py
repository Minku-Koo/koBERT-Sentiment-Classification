import json
import math
import csv

def readComment(paths, filename):
    with open(paths+filename+".json", "rt" , encoding="utf-8") as json_file:
        data = json.load(json_file)
    commentlist = []
    for date in data:
        for article in data[date]:
            for comment in data[date][article][0]:
                if comment == "": continue
                commentlist.append(comment)
    print(f'{filename} 댓글은 {len(commentlist)}개')
    return commentlist

def writeTsv(path, filename, data):
    
    ten_percent_index = int( len(data) * 0.1 )

    f = open(path+filename+'.tsv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(f, delimiter='\t')

    #data.remove("")
    print(f"{filename} 댓글 개수는 {len(data)}")

    num = 0
    for  comment in data:
        if len(comment)<5: continue
        if num > ten_percent_index: break
        wr.writerow([comment.replace("\n", ""), False])
        num+=1

    f.close()
    print(f"저장 댓글 수:{num}")
    return num


tlist = []
for i in range(1,6): tlist.append(["before"+str(i),"after"+str(i)])

all_comment_count = 0
save_numbers = 0

commentpath = "./json-okt-comment/"
save_path = "./train-data/work_tsv_files/"
for tname in tlist:
    potal = "daum"
    for t in tname:
        filename = potal+t+"-dict"
        comments = readComment(commentpath, filename)
        all_comment_count += len(comments)
        savednum = writeTsv(save_path, filename, comments)
        save_numbers += savednum

    potal = "naver"
    for t in tname:
        filename = potal+t+"-dict"
        comments = readComment(commentpath, filename)
        all_comment_count += len(comments)
        savednum = writeTsv(save_path, filename, comments)
        save_numbers += savednum
        
print("총",all_comment_count , "개")
print("저장 총 댓글:", save_numbers)

