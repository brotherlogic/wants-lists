import pgdb,sys,os

db = pgdb.connect(dsn='192.168.1.100:music',user='music')
cursor = db.cursor()

def scorelist(listname,show):
    scores = []
    for line in open(listname,'r').readlines():
        elems = line.strip().split("~")
        if len(elems) == 3:
            (artist,title,id) = elems
            
            cursor.execute("select author,title,simon_score from score_table,records where record_id = recordnumber AND record_id = " + id)
            row = cursor.fetchone()
            if row != None and row[0] != None:
                score = float(row[2])
                if show:
                    print row[0] + " - " + row[1] + " [" + `score` + "]"
                scores.append(score)

    scores.sort()
    if len(scores) > 0:
        print sum(scores)/len(scores),listname
    else:
        print 0.0,listname

if len(sys.argv) > 1:
    scorelist(sys.argv[1],True)
else:
    for file in os.listdir('.'):
        if file.endswith(".list"):
            scorelist(file,False)
    for file in os.listdir('comps'):
        if file.endswith(".list"):
            scorelist("comps/" + file,False)
