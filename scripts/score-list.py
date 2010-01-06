import pgdb,sys,os

db = pgdb.connect(dsn='192.168.1.100:music',user='music')
cursor = db.cursor()

def scorelist(listname):
    scores = []
    for line in open(listname,'r').readlines():
        elems = line.strip().split("~")
        if len(elems) == 3:
            (artist,title,id) = elems
            
            cursor.execute("select simon_score from score_table where record_id = " + id)
            row = cursor.fetchone()
            if row != None and row[0] != None:
                score = float(row[0])
                scores.append(score)

    scores.sort()
    if len(scores) > 0:
        print sum(scores)/len(scores),scores[len(scores)/2],listname
    else:
        print 0.0,listname

if len(sys.argv) > 1:
    scorelist(sys.argv[1])
else:
    for file in os.listdir('.'):
        if file.endswith(".list"):
            scorelist(file)
