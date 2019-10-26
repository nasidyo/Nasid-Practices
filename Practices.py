def switch():
    print ("Press 1 for case 1\nPress 1 for case 2\nPress 3 for case 3.1\nPress 4 for case 3.2\nPress 5 for case 3.3\nPress 6 for case 3.4\nPress 7 for case 3.5\nPress 8 for case 3.6\nPress 9 for case 4\nPress 10 for case 5")
    option = int(input("Your Case ? : "))
    def Case1():
        #examlpe 1
        numberlist = []
        str = ''
        for i in range(1,100):
            if i%3 == 0 and i%5 == 0 :
                str ="FizzBuzz"
            elif i%3 == 0 :
                str ="Fizz"
            elif i%5 == 0 :
                str = "Buzz"
            else:
                str = i
            numberlist.append(str)
        print(numberlist)

    def Case2():
        #examlpe 2
        yearnumber = int(input("Enter year number : "))
        yearsCheck = "false"
        if yearnumber % 400 == 0:
            yearsCheck = "true"
        elif yearnumber % 100 != 0 and yearnumber % 4 == 0 :
            yearsCheck = "true"
        print (yearnumber ,"-->", yearsCheck)

    def Case3():
        #exlampe 3.1
        row = int(input("Enter number of n: "))
        for i in range(0,row):
            for j in range (0,i+1):
                print("*",end="")
            print()

    def Case4():
        #examlpe 3.2
        row = int(input("Enter number of n: "))
        for i in range(0,row):
            for j in range (1, row):
                print(" ",end="")
            row = row-1
            for k in range(0, i+1):
                print("*",end="")
            print()

    def Case5():
        #examlpe 3.3
        row = int(input("Enter number of n: "))
        for i in range(1,row+1):
            for j in range (1,row):
                print(" ",end="")
            row = row-1
            for k in range(0, (i*2)):
                if k == 1 or k == (i*2-1):
                    print("*",end="")
                else :
                    print(" ",end="")
            print()
    def Case6():
        #examlpe 3.4
        row = int(input("Enter number of n: "))
        for i in range(1,row+1):
            for j in range (1,row+1):
                if j == i or j == (row-i+1):
                    print("*",end="")
                else:
                    print("-",end="")
            print()

    def Case7():
        #examlpe 3.5
        k = 0
        row = int(input("Enter number of n: "))
        for i in (1, row+1):
            for j in range (1, (row -i)+1):
                print(end="")
                while k != (2*i-1):
                    print("*",end="")
                    k = k+1
                k=0
            print()
            



    def Case8():
        #examlpe 3.6
        print("Function in progess")
    
    def Case9():
        #examlpe 4
        print("In Python , What is the defference between else and finally :: \n Else is under loop will run when top condition is not success , But Finally will run when code end of function.")
    
    def Case10():
        #examlpe 5
        inputnumber = int(input("Enter your number : "))
        listnumber = [];
        if inputnumber > 1 :
            for val in range(2,inputnumber):
                isPrime = True
                for n in range(2, val):
                    if (val % n) == 0: 
                            isPrime = False
                if isPrime:
                    listnumber.append(val)
            print( inputnumber," -> ",listnumber)
        else : 
            print ("prime number is is more than 1")



    def default():
        return "Incorrect day"

    switcher = {
        1: Case1,
        2: Case2,
        3: Case3,
        4: Case4,
        5: Case5,
        6: Case6,
        7: Case7,
        8: Case8,
        9: Case9,
        10: Case10
    }

    switcher.get(option, default)()
    

switch()
