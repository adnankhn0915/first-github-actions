#Test commit
def addition(a,b):
    return a+b

def addition_test():
    assert addition(2,3) == 5
    assert addition(-1,1) == 0
    assert addition(0,0) == 0
    assert addition(10,5) == 15
