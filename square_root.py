

def squareroot():
    y = 1
    x = int(input("Please enter a even number: "))
    while round(((y*y)-x), 2) != 0:
        y = ((y+(x/y))/2)


    #return print(y)
    print("The squareroot of {} is {}".format(x,y))
squareroot()
