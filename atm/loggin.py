import pymysql
from user_information import user_information

def new_user():
    username = input('请输入您的用户名：')
    flag=True
    while flag:
        password = input('请输入您的密码：')
        password_check = input('请确认您的密码：')
        if(password!=password_check):
            print('两次密码不相同，请重新确认!')
        else:
            flag=False
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='zst15122172253', db='atm')
    cur = conn.cursor()
    cur.execute("insert into loggin(username,password)  values(\'%s\',\'%s\')" % (username,password))
    cur.close()
    conn.commit()
    conn.close()
    print('恭喜您！注册成功')

def user_loggin():
    username_ = input('请输入您的用户名：')
    flag_1=True
    while flag_1:
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='zst15122172253', db='atm')
        cur = conn.cursor()
        name_count = cur.execute('select username from loggin')
        all_username = cur.fetchmany(name_count)
        flag_2=0
        for i in range(name_count):
            if username_==all_username[i][0]:
                flag_2=1
                password_ = str(input('请输入您的密码：'))
                password_check = cur.execute("select password from loggin where username=\'%s\'" % (username_) )
                if password_ != cur.fetchmany(password_check)[0][0]:
                    print('您输入的密码有误！请重新输入！')
                else:
                    print('登陆成功！')
                    user_information(username_)
                    cur.close()
                    conn.close()
                    flag_1=False
                    return True
        if flag_2==0:
            print('该用户不存在，请先注册！')
            return  False
def loggin():
    while True:
        choose = input('1.新用户注册\n'
                    '2.已有用户登录\n')
        if(choose=='1'):
            new_user()
        elif(choose=='2'):
            if user_loggin():
                break
        else:
            print('您的输入有误。请重新输入')


