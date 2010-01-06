import pgdb,sys,os

#Connect to the database
db = pgdb.connect(dsn='192.168.1.100:music',user='music')
cursor = db.cursor()

def sync(filename):
    for line in open(filename,'r').readlines()[1:]:
        elems = line.strip().split('~')
        artist = ""
        title = ""
        if len(elems) == 2:
            (artist,title) = elems

        cursor.execute("select recordnumber from records where author = '" + pgdb.escape_string(artist) + "' AND title = '" + pgdb.escape_string(title) + "'")
        row = cursor.fetchone()
        seen = False
        while row != None:
            if not seen:
                print artist,title
                seen = True

            print "\t",row[0]
            row = cursor.fetchone()

if len(sys.argv) > 1:
    sync(sys.argv[1])
else:
    for file in os.listdir('.'):
        if file.endswith('.list'):
            sync(file)
