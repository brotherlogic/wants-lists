import pg,sys,os
from random import shuffle

just_print = False
con = pg.connect(dbname='music',host='192.168.1.103',user='music')

def pick_records(format,count,first_choose):

    #Randomize the first_choose list
    shuffle(first_choose)

    for id in first_choose:
        if count > 0:
            sql = "update records set boxed = -1 where recordnumber = " + id
            if just_print:
                print sql
            else:
                con.query(sql)
            count -= 1

    if count > 0:
        sql = "update records set boxed = -1 where recordnumber in (select recordnumber from records,score_table,formats where boxed != -1 AND recordnumber = record_id AND (owner = 1 OR simon_score >= 8) AND format = formatnumber AND baseformat = '"+format+"'  AND salepricepence < 0 ORDER BY RANDOM() LIMIT "+`count`+")";
        if just_print: 
            print sql 
        else: 
            con.query(sql)

#Move all boxed records into the to-shelve box
sql = "UPDATE records set boxed = 0 where boxed = -1"
if just_print: 
    print sql 
else: 
    con.query(sql)

# Pull in the unranked data
format_map = {}
for line in os.popen('python scripts/find-unranked.py').readlines():
    (id,format) = line.strip().split()
    if format not in format_map:
        format_map[format] = []
    format_map[format].append(id)

formats_count = {}
formats_count["12"] = 11
formats_count["CD"] = 20
formats_count["10"] = 3
formats_count["7"] = 11

for format in formats_count:
    if format in format_map:
        pick_records(format,formats_count[format],format_map[format])
    else:
        pick_records(format,formats_count[format],[])   
