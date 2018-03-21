#查询用户信息
import pymysql
def my_information(username):
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='zst15122172253', db='atm')
    cur = conn.cursor()
    all_information_ = cur.execute("select * from loggin where username= \'%s\'" % username)
    all_information = cur.fetchmany(all_information_)
    password = all_information[0][1]
    balance = all_information[0][2]
    info = '''
    -------my information------
    username:%s
    password:%s
    balance:%s
    ''' %(username,password,balance)
    print(info)