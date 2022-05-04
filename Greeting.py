a=1
b=5
scores={4,1,9,23,a,b}
for x in scores:
    if x==0:
        print("失格です")
    elif x<5:
        print("追試です")
    else:
        print("合格です")
        