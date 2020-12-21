#Name: Tarini Srikanth
#Instructor: Turner
#Project- Lab3 Logic
def is_even(x):
    mod= x%2
    return(mod==0)
def in_an_interval(y):
    twoAndNine = y>=2 and y<9
    fortySevenAndNinetyTwo = y>47 and y<92
    twelveAndNineteen = y>12 and y<=19
    hunderedAndOneAndThree = y>=101 and y<=103
    return(twoAndNine==True or fortySevenAndNinetyTwo==True or twelveAndNineteen==True or hunderedAndOneAndThree ==True)


