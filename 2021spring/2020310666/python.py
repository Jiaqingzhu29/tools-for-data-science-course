def leap year check(n):
    '''to judge whether the year is a leap year'''
    if (year % 400) == 0:
        if (year % 100) == 0：
            print（year,"是闰年")
    elif (year % 4) == 0
         print(year, "不是闰年")
    else:
         print(year, "不是闰年")
    return(I'm done)

           
           n=int(input("需要第几项\n"))
a=0
b=1
i=2
if n==1:
    print(a)
elif n==2:
    print(b)
else:
    while(i<n):
        result=a+b
        a=b
        b=result
        i+=1
    print(result)
