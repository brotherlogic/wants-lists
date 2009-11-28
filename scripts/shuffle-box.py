import pg,sys
from random import shuffle

records = []

for form in sys.argv[1:]:

    sql = "SELECT recordnumber,author,title,formatname from records,formats where boxed = -1 AND format = formatnumber AND baseformat like '" + form + "%'"

    con = pg.connect(dbname='music',host='192.168.1.103',user='music')
    res = con.query(sql)
    for dic in res.dictresult():
        records.append(dic['author'] + " - " + dic['title'] + " [" + `dic['recordnumber']` + "] => " + dic['formatname'])

shuffle(records)

for rep in records:
    print rep
