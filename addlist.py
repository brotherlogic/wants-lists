import os,sys,pg
from random import shuffle

#Connect to the database
con = pg.connect(dbname='webwants',user='webwants')

files = []
for file in os.listdir('.'):
    if file.endswith('.list'):
        files.append(file)

shuffle(files)

def listAdded(name):
    sql = "SELECT COUNT(*) as count from wants_list where name = '" + pg.escape_string(name) + "'"
    res = con.query(sql)
    for dic in res.dictresult():
        num = dic['count']
    return num > 0

def addList(lines):
    name = lines[0].strip()

    # Add this list
    sql = "INSERT INTO wants_list (name,score) VALUES ('" + pg.escape_string(name) + "',-1.0)"
    con.query(sql)

    #Get th list id
    sql = "SELECT id from wants_list WHERE name = '" + pg.escape_string(name) + "'"
    res = con.query(sql)
    idv = res.dictresult()[0]['id']

    #print name,idv
    for line in lines[1:]:
        elems = line.strip().split('~')
        if len(elems) == 5:
            (num,artist,title,format,genre) = elems
        elif len(elems) == 4:
            (artist,title,format,genre) = elems
        elif len(elems) == 2:
            (artist,title) = elems
            format = "12"
            genre = "jazz"
        else:
            print line
            sys.exit(1)

        sql = "INSERT INTO wants_want (artist,title,format,genre,label,mainid,cdexists,score,doneebay,donegemm,donepops) VALUES ('" + pg.escape_string(artist) + "','" + pg.escape_string(title) + "','" + pg.escape_string(format) + "','" + pg.escape_string(genre) + "','',-1,false,-1.0,false,false,false)"
        print sql
        res = con.query(sql)

        sql = "SELECT id from wants_want where artist = '" + pg.escape_string(artist) + "' AND title = '" + pg.escape_string(title) + "' AND format = '" + pg.escape_string(format) + "' AND genre = '" + pg.escape_string(genre) + "'"
        res = con.query(sql)
        idw = res.dictresult()[0]['id']

        sql = "INSERT INTO wants_list_want (list_id,want_id) VALUES (" + `idv` + "," + `idw` + ")"
        res = con.query(sql)

if len(sys.argv) == 2:
    files = [sys.argv[1]]
    
for file in files:
    lines = open(file,'r').readlines()
    name = lines[0].strip()
    
    #Check if this list has been added
    if not listAdded(name):
        addList(lines)
        sys.exit(1)

print "All lists added"
