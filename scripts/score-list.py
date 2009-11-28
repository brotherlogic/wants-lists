import pgdb,sys,os

(username,pwd) = open('details.txt','r').readlines()[0].split(" ")
db = pgdb.connect(dsn='192.168.1.103:music',user=username,password=pwd)
cursor = db.cursor()

def scorelist(listname):
    scores = []
    for line in open(listname,'r').readlines():
        elems = line.strip().split("~")
        if len(elems) == 3:
            (artist,title,id) = elems
            
            cursor.execute("select simon_rank from score_table where record_id = " + id)
            row = cursor.fetchone()
            if row != None:
                score = float(row[0])
                scores.append(score)

    print sum(scores)/len(scores),listname

if len(sys.argv) > 1:
    scorelist(sys.argv[1])
else:
    for file in os.listdir('.'):
        if file.endswith(".list"):
            scorelist(file)
