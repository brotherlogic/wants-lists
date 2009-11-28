import pgdb,sys,os

(username,pwd) = open('details.txt','r').readlines()[0].split(" ")
db = pgdb.connect(dsn='192.168.1.103:music',user=username,password=pwd)
cursor = db.cursor()

def scorelist(listname):
    unranked = []
    for line in open(listname,'r').readlines():
        elems = line.strip().split("~")
        if len(elems) == 3:
            (artist,title,id) = elems
            
            cursor.execute("select simon_rank,baseformat from score_table,records,formats where record_id = " + id + " AND record_id = recordnumber AND format = formatnumber")
            row = cursor.fetchone()
            if row != None:
                score = float(row[0])
                if score == 0:
                    unranked.append((id,row[1]))

    return unranked

if len(sys.argv) > 1:
    for id in scorelist(sys.argv[1]):
        print id
else:
    unranked = []
    for file in os.listdir('.'):
        if file.endswith(".list"):
            unranked.extend(scorelist(file))
    for pair in unranked:
        print pair[0],pair[1]
