import pymysql

db = pymysql.connect(
    user='root',
    passwd='1234',
    host='localhost:3306',
    db='playnewsdb',
    charset='utf8'
)


cursor = db.cursor(pymysql.cursors.DictCursor)



insert_sql = "INSERT INTO `newsinfo` (cnt,title,link,date_first,date_mod,newspaper,writer,context,img_link,img_alt) VALUES (%(cnt)s, %(title)s, %(link)s, %(date_first)s, %(date_mod)s, %(newspaper)s, %(writer)s, %(context)s, %(img_link)s, %(img_alt)s);"
cursor.executemany(insert_sql, DataResult)
db.commit()
