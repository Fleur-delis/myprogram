#猜数字游戏练习,无限次数
correct_age = 55
count =0
while count <3:
    guess_age =int(input("guess age:"))
    if guess_age==correct_age:
        print("恭喜你，猜对了！")
        break
    elif guess_age>correct_age:
        print("请猜小一点...")
    else:
        print("请猜大一点...")
    count=count+1
    if count==3:
        continue_comfrim =input("do you want to continue?")
        if continue_comfrim!='n':
            count=0