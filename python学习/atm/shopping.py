#购物
import pymysql
import user_information
import datetime
def shops():
    pass
def shopping(username):
    username = username
    menu = '''
    1.apple    $5
    2.banana   $7
    3.pear     $11
    4.orange   $20
    '''
    dic_buy = {
        '1':'apple',
        '2':'banana',
        '3':'pear',
        '4':'orange'
    }
    print(menu)
    choose = str(input('请输入您想要购买的商品编号：'))
    time = datetime.datetime.now()
    buy = str(dic_buy[choose])
    conn = pymysql.connect(host='localhost', port=3306,user='root', password='zst15122172253', db='atm')
    cur = conn.cursor()
    price_ = cur.execute("select price from shopping where goods= \'%s\'"  %buy)
    price = int(cur.fetchmany(price_)[0][0])
    money_ = cur.execute("select balance from loggin where username = \'%s\' "   %username)
    money = int(cur.fetchmany(money_)[0][0])
    print(money)
    if money>=price:
        balance = money-price
        print('您的余额为：%d'  %balance)
        cur.execute("update loggin set balance = %d where username = \'%s\'"   %(balance,username))
        cur.execute("insert into account(username,goods,balance,time) values(\'%s\',\'%s\',%d,\'%s\')"  %(username,buy,balance,time))
        print('购买成功！')
        cur.close()
        conn.commit()
        conn.close()

