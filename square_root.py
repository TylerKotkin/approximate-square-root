

def squareroot():
    y = 1
    x = int(input("Please enter a even number higher than 0: "))
    while round(((y*y)-x), 4) != 0:
        y = ((y+(x/y))/2)

        #print(y)
    #return print(y)
    print("The squareroot of {} is {}".format(x,y))
squareroot()
