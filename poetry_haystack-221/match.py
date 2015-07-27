import enchant

dic = enchant.Dict("en_US")
with open('input.txt','r') as f:
    for index,line in enumerate(f,start=1):
        weight = 0
        for l in line.split():
            if dic.check(l) == True and len(l) > 2:
                weight += 1
        if weight > 3:
            print index,':',line
