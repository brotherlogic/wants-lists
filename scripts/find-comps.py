import pg,sys,os

sql = "SELECT * from records,score_table WHERE recordnumber = record_id AND author = 'Various' AND simon_score >= 7 AND simon_rank_count >= 2"
con = pg.connect(dbname='music',host='192.168.1.100',user='music')

res = con.query(sql)

for dic in res.dictresult():
    if not os.path.exists('comps/' + `dic['recordnumber']` + '.list'):
        print dic['recordnumber'],dic['author'],dic['title']
