import time,pgdb

POUNDS_PER_WEEK = 15

day_of_year = time.localtime()[7]
budget = (10*52/365.0)*day_of_year

db = pgdb.connect(dsn='192.168.1.100:music',user='music')
cursor = db.cursor()

cursor.execute("select sum(purchase_price) from records where owner = 1 AND boughtdate > '2010-01-01'")
row = cursor.fetchone()
spends = float(row[0])

print budget - spends

