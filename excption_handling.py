# class ashok(Exception):
#     pass
# try:
#     a=[1,2,3,4]
#     user=int(input("enter a index:"))
#     if user > len(a):
#         raise ashok()
#     else:
#         print("the index value is:",a[user])        
# except ashok:
#     print("this is index error")

def result(x,y):
    if x/y:
        raise ValueError("cannot be divided")
    return x/y 

try:
    result(10,2)
except ValueError as e:
    print(e)
    