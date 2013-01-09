import operator

myCollatz = range(1,1000000)

def myMapper(x):
    num = 0
    while x != 1:
        if ((x%2)==0):
            x = x/2
            num += 1
        elif ((x%2)==1):
            x = 3*x + 1
            num += 1
    return num

myMapped = map(myMapper,myCollatz)

answer =  max(enumerate(myMapped), key=operator.itemgetter(1))

print answer

