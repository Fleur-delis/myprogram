cart={
    '天谕':{'近战':["光刃","圣堂","业刹"],
            '远程':["炎天","玉虚","灵珑","流光"]},
    '阴阳师':{'SSR':["一目连","荒","茨木童子"],
              'SR':["姑获鸟","妖狐","夜叉"],
              'R':["椒图","山兔","雨女"]},
    '王者荣耀':{'法师':["诸葛亮","貂蝉","妲己"],
                '刺客':["兰陵王","荆轲","李白"],
                '射手':["李元芳","马可波罗","百里守约"]}
}
count=False
while not count:
    for i in cart:
        print(i)
    choose1=input('请输入：')
    if choose1 in cart:
            while not count:
                for i in cart[choose1]:
                    print(i)
                choose2=input('请输入：')
                if choose2 in cart[choose1]:
                    while not count:
                        for i in cart[choose1][choose2]:
                            print(i)
                        choose3 = input('请输入：')
                        if choose3=='q':
                            break
                        elif choose3=='n':
                            count=True
                elif choose2 == 'q':
                    break
                elif choose2 == 'n':
                    count = True
    elif choose1 == 'q':
        break
    elif choose1 == 'n':
        count = True

