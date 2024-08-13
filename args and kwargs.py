def cal_percen(**kwargs):
    sum=0
    print("kwargs:",kwargs)
    print("mrinal is a hero")
    print(len(kwargs))
    for key,value in kwargs.items():
        sum=sum+value
    
    return sum/len(kwargs)
    
percentage=cal_percen(math=45,bio=73,eco=76)
print("percentage:",percentage)  
percentage=cal_percen(math=80,bio=45)
print("percentage:",percentage)