import sys,os
from uk.co.brotherlogic.mdb.record import Record
from uk.co.brotherlogic.mdb.record import GetRecords
from uk.co.brotherlogic.mdb import User
from uk.co.brotherlogic.mdb import Connect

#Add all the jars to the class path
sys.path.append('./postgresql-8.3-603.jdbc4.jar')
sys.path.append('./mdbcore-0.6-SNAPSHOT.jar')

# Set for COnnection
#for i in range(1,len(sys.argv),2):
#    record_id = int(sys.argv[i])
#    score = int(sys.argv[i+1])#

    # Retrieve the record
#    rec = GetRecords.create().getRecord(record_id);
#    user = User.getUser("Simon")
#    print "Scoring " + rec.getAuthor() + " - " + rec.getTitle() + ": " + `score`
#    rec.addScore(user,score)
    
    # Commit the trans
#    Connect.getConnection().commitTrans()

def scorelist(listname,show):
    scores = []
    read = False
    for line in open(listname,'r').readlines()[1:]:
        read = True
        elems = line.strip().split("~")
        if len(elems) == 3:
            (artist,title,id) = elems
            rec = GetRecords.create().getRecord(int(id))

            score = rec.getScore(User.getUser("Simon"))
            if show:
                print rec.getAuthor() + " - " + rec.getTitle() + " [" + `score` + "]"
            scores.append(score)

    scores.sort()
    if len(scores) > 0:
        print sum(scores)/len(scores),listname
    elif read:
        print 0.0,listname

if len(sys.argv) > 1:
    scorelist(sys.argv[1],True)
else:
    for file in os.listdir('.'):
        if file.endswith(".list"):
            scorelist(file,False)
