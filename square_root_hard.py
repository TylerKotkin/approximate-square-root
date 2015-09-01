def squareroot():

    try:
        x = int(input("Please enter a number higher than 0: "))
        y = 1

    except ValueError:
         print("ERROR: That is not a number higher than 0")
         exit()
    if int(x) <= 0:
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
