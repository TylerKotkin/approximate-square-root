

def squareroot():
    x = int(input("Please enter a even number higher than 0: "))
    y = int(input("Please guess the square root of the number entered: "))
    while round(((y*y)-x), 4) != 0:
        y = ((y+(x/y))/2)

        
    print("The squareroot of {} is {}".format(x,y))
squareroot()
