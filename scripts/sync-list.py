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

        if artist != 'Various':
            cursor.execute("select records.recordnumber,author,title from records,track,groops,lineupset,lineup where records.recordnumber = track.recordnumber and track.trackrefnumber = lineupset.tracknumber and lineupset.lineupnumber = lineup.lineupnumber AND lineup.groopnumber = groops.groopnumber and lower(records.title) = '" + pgdb.escape_string(title.lower()) + "' AND lower(groops.show_name) = '" + pgdb.escape_string(artist.lower()) + "'")
        else:
            cursor.execute("select recordnumber from records where author = '" + pgdb.escape_string(artist) + "' AND title = '" + pgdb.escape_string(title) + "'")
        row = cursor.fetchone()
        seen = False
        done = []
        while row != None:
            if not seen:
                if (artist,title) not in done:
                    print artist,title,"(" + filename + ")"
                    seen = True
            if row[0] not in done:
                print "\t",row[0]
                done.append(row[0])
            row = cursor.fetchone()

if len(sys.argv) > 1:
    sync(sys.argv[1])
else:
    for file in os.listdir('.'):
        if file.endswith('.list'):
            sync(file)
