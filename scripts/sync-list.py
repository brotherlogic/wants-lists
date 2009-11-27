import pgdb,sys

filename = sys.argv[1]

#Get the connection details
(username,pwd) = open('details.txt','r').readlines()[0].split(" ")

#Connect to the database
db = pgdb.connect(dsn='192.168.1.103:music',user=username,password=pwd)
cursor = db.cursor()

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
