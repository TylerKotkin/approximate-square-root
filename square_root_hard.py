def squareroot():

    try:
        x = int(input("Please enter a number higher than 0: "))
        y = int(input("Please guess the square root of the number entered: "))

    except ValueError:
         print("ERROR: That is not a number")
         exit()
    if int(x) <= 0:
        print("ERROR: That is not a number higher than 0")
        exit()
    if int(y) <= 0:
        print("ERROR: That is not a number higher than 0")
        exit()
    else:
        counter = 0
        while round(((y*y)-x), 4) != 0:
            y = ((y+(x/y))/2)
            counter+=1
            print (counter, y)



    print("The squareroot of {} is {}".format(x,y))
squareroot()
