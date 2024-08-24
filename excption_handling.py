class invalidageexception(Exception):
    pass
age=2
try:
    if age<18:
        raise invalidageexception("can't vote")
    else:
        print("eligible to vote")
        
except invalidageexception as e:
    print(e)
finally:
    print("job done")
    
    
    
