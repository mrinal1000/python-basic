def add_num(*ram):
    sum=0
    print("*ram:",ram)
    print("we can notice that ram is tuple")
    for num in ram:
        sum=sum+num
        return sum
    
sum= add_num(10,20,30,40)
print("sum:",sum)
    
    