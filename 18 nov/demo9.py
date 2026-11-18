# 8 arbitary keyword argument list function 
def product(**p):
    print(type(p))
    print(p)

product(code=1,name="cpu",price=25000) 