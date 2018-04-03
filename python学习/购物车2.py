#file5-f1 已购商品，file6-f2    余额
choose_user=["1.购买商品","2.查询余额及购买记录"]
choose_player=["1.添加商品信息","2.更改商品价格"]
character=input("用户或管理员登陆：")
if character=='用户':
    count = 0
    while True:
        name = input("name:")
        password = input("password:")
        if name == 'tom.json':
            if password == '123456':
                print("恭喜您，登陆成功！")
                while True:
                    for i in choose_user:
                        print(i)
                    choose1=input("请输入您所需要的服务：")
                    if choose1=='1':
                        brought = []
                        f2=open("file6",'r',encoding='utf-8')
                        x=f2.readlines()
                        if x==[]:
                            salary = int(input("请输入您的工资："))
                        else:
                            salary=int(x[0])
                            print("您的余额为：%s" %salary)
                        while salary:
                            f = open("file4", 'r', encoding='utf-8')
                            good = f.readlines()
                            for i in good:
                                print(i)
                            buy = input("请输入您购买的商品编号")
                            if buy == 'q':
                                print("您的购物清单：", brought)
                                print("您的余额：", salary)
                                f1 = open("file5",'a',encoding='utf-8')
                                f2 = open("file6",'w', encoding='utf-8')
                                for i in brought:
                                    f1.write(i)
                                f2.write(str(salary))
                                exit()
                            elif buy.isdigit():
                                buy = int(buy)
                                if int(buy) <= len(good):
                                    money = int(good[2*buy-1])
                                    while salary - money >= 0:
                                        salary = salary - money
                                        brought.append(good[2*buy-2])
                                        print("购买成功！您的余额为[%s]" % salary)
                                        break
                                    else:
                                        print("对不起，您的余额不足")
                                else:
                                    print("您选择的商品不存在，请重新输入！")
                            else:
                                print("您的输入有错误，请重新输入！")
                    else:
                        f1 = open("file5", 'r', encoding='utf-8')
                        f2 = open("file6", 'r', encoding='utf-8')
                        buy=f1.read()
                        salary1=f2.read()
                        print("您的余额为：%s"%salary1)
                        print("您的已购商品为：%s"%buy)
            else:
                count = count + 1
                if count > 3:
                    f = open("file3", 'w', encoding="utf-8")
                    f.write('#')
                    f.close()
                f = open("file3", 'r', encoding="utf-8")
                y = f.read()
                if y != '#':
                    print("密码错误,请重新输入")
                    f.close()
                else:
                    print("出入次数过多，账户已被锁定！")
                    f.close()
                    break
        else:
            print("该用户不存在，请重新输入！")
if character=='管理员':
    print(choose_player)
    choose2=input("请选择：")
    while True:
     if choose2 == '1':
            goods = input("所添加商品名称：")
            price = input("所添加商品价格：")
            f3 = open("file4", 'a', encoding='utf-8')
            f3.write(goods)
            f3.write(price)
            print("添加成功！")
     elif choose2=='2':
            for i in choose_user:
                print(i)
            goods_number = int(input("请输入想要修改的商品编号："))
            price_change = input("修改后的价格为：")
            f4 = open("file4", 'r+', encoding='utf-8')
            new_file=f4.readlines()
            new_file[2*goods_number-1]=price_change
            print(new_file)
            f5 = open("file7",'w',encoding='utf-8')
            f5.writelines(new_file)
            print("修改成功！")



