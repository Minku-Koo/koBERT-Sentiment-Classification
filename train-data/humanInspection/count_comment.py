
# 총 댓글 몇개인지 확인

def checkLine(filename):
    try:
        with open("./"+filename+"-dict.tsv", "rt", encoding="utf-8") as f:
            l = f.readlines()
    except:
        l = []
    return len(l)


tlist = []
for i in range(1,6): tlist.append(["before"+str(i),"after"+str(i)])

result  = 0
for period in tlist:
    for t in period:
        file = "daum"+t
        count = checkLine(file)
        result += count
        print(file, ":", count)
        
        file = "naver"+t
        count = checkLine(file)
        result += count
        print(file, ":", count)
        
print("-----\nAll >>", result)