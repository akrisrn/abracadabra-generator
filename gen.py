from random import randint, uniform, seed

import pymysql


def ran_int(m):
    return randint(1, m)


def ran_double():
    return uniform(1, 100)


def get_word(ss=None):
    if ss:
        seed(ss)
    s_c = ran_int(3)
    sp_c = ran_int(10)

    db_host = ''
    db_port = 3306
    db_user = ''
    db_password = ''
    db_name = ''

    conn = pymysql.connect(host=db_host,
                           port=db_port,
                           user=db_user,
                           passwd=db_password,
                           db=db_name,
                           charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT s, pp FROM syllable ORDER BY pp")
    data = cur.fetchall()
    ste = ""
    for n in range(sp_c):
        st = ""
        for u in range(s_c):
            r = ran_double()
            c = 0
            s = 0
            for i, d in enumerate(data):
                s += d[1]
                if s > r:
                    c = i
                    break
            st += data[c][0]
        if ran_int(100) > 50:
            ste += st + " "
        else:
            ste += st + " "
    ste = ste[:-1] + "."
    cur.close()
    conn.close()
    return ste

if __name__ == '__main__':
    print(get_word())
