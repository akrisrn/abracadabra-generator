import pymysql
import re

db_host = ''
db_port = 3306
db_user = ''
db_password = ''
db_name = ''


def analyse(s):
    s = re.sub('[^a-zA-Z]', '', s)
    aeiouy = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    for i, c in enumerate(s):
        if c in aeiouy:
            j = 1
            while i - j >= 0 and s[i - j] not in aeiouy:
                yield s[i - j:i + 1]
                j += 1
            j = 1
            while i + j < len(s) and s[i + j] not in aeiouy:
                yield s[i:i + j + 1]
                j += 1
            k = 1
            while i - k >= 0 and s[i - k] not in aeiouy:
                j = 1
                while i + j < len(s) and s[i + j] not in aeiouy:
                    yield s[i - k:i + j + 1]
                    j += 1
                k += 1


conn = pymysql.connect(host=db_host,
                       port=db_port,
                       user=db_user,
                       passwd=db_password,
                       db=db_name,
                       charset='utf8')
cur = conn.cursor()
cur.execute("CREATE TABLE syllable ("
            "id int(11) NOT NULL AUTO_INCREMENT,"
            "s varchar(255) NOT NULL,"
            "p int(11) NOT NULL,"
            "pp float NOT NULL,"
            "PRIMARY KEY (id),"
            "UNIQUE KEY syllable_s_uindex (s))")

with open("z4.txt") as f:
    for line in f:
        for a in analyse(line):
            cur.execute("select count(s) from syllable where s='" + a + "'")
            num = cur.fetchone()[0]
            if num == 0:
                print("INSERT INTO syllable (s, p) VALUES ('%s', 1);" % a)
                cur.execute("INSERT INTO syllable (s, p) VALUES ('%s', 1);" % a)
            else:
                print("UPDATE syllable SET p=p+1 WHERE s='" + a + "'")
                cur.execute("UPDATE syllable SET p=p+1 WHERE s='" + a + "'")

cur.execute("SELECT sum(p) FROM syllable;")
sum_p = cur.fetchone()[0]
cur.execute("UPDATE syllable SET pp = p / " + str(sum_p) + " * 100")

conn.commit()
cur.close()
conn.close()
