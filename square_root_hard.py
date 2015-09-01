def squareroot():
    y = 1
    x = int(input("Please enter an even number higher than 0: "))
    if type(x) != int:
         print("That is not an even number higher than 0")
         exit()
    elif x <= 0:
        print("That is not an even number higher than 0")
        exit()
    else:
        while round(((y*y)-x), 4) != 0:
            y = ((y+(x/y))/2)

            print(y)

    print("The squareroot of {} is {}".format(x,y))
squareroot()
