def Leap_year(x):
year=int(input("请输入年份：\n"))
if(year%4==0|(year%4==0&year%100!=0)):
    print("闰年")
else:
    print("平年")
return(That's all.)
