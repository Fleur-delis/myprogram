import random
checkcode=''
for i in range(4):
    number=random.randrange(4)
    if i==number:
        plus=chr(random.randint(65,90))
    else:
        plus=random.randint(0,9)
    checkcode+=str(plus)
print(checkcode)