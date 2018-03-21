from loggin import loggin
import user_information
from my_information import my_information
from shopping import shopping
loggin()
username=user_information.get_user()
menu = {
    '1': my_information,
    '2': shopping,
    '3':'存款',
    '4':'取款'
}
#存款，取款未实现
while True:
    info = '''------HELLO  %s------
    1.查询用户信息
    2.购物
    3.存款
    4.还款
    ''' %username
    print(info)
    service_id = str(input('请输入您所需要的服务编号：'))
    if service_id in menu:
        menu[service_id](username)
