def max_of_two(x, y):
    if x <= y :
        return y
    else :
        return x
max_of_two(5,4)    
max_of_two(-2,-3)
max_of_two(0,0)
def max_of_three(x, y, z):
    if x <= y and z <= y :
        return y
    elif y <= z and x <= z :
        return z
    else :
        return x
max_of_three(-2,-3,-1)
max_of_three(0,0,0)
