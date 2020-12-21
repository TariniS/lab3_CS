#Name: Tarini Srikanth
#Instructor: Turner
#Project: Lab3 - Conditional
def max_101(x,y):
    if(x>y):
        return(x)
    elif(y>x):
        return(y)
    else:
        return("Equal")
def max_of_three(x,y,z):
    if(x>y and x>z):
        return x
    elif(y>x and y>z):
        return y
    elif(z>x and z>y):
        return z
    else:
        return("Equal")
    #should put a conditional if they are equal
def rental_late_fee(d):
    if(d<=0):
        return(0)
    elif(d<=9):
        return(5)
    elif(d<=15):
        return(7)
    elif(d<=24):
        return(19)
    else:
        return(100)
