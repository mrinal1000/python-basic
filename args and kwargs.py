def add_num(*args):
    sum=0
    print("args:", args)
    print("it is a good program")
    for num in args:
        sum=sum+num
    return sum
sum=add_num(12,1,31,43)
print("sum:",sum)
sum=add_num()
print("sum:",sum)
