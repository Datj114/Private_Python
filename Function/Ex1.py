def MyMultiple(*args):
    ''' this function return a multiplication of args '''
    result=1
    for i in args:
        result *=i
    return result
print(MyMultiple(1.2,5))