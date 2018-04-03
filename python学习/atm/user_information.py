#暂存用户信息
id_info = {'id':''}
def user_information(user):
    id_info['id']=user
def get_user():
    username=id_info['id']
    return username
