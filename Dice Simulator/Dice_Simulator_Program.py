import random as rd 
while True:
    x = input("Roll the Dice ? y/n \n")
    if x=='y':
        x = rd.randint(1,6)
        if x==1:
            print("------------")
            print("|          |")
            print("|     0    |")
            print("|          |")
            print("------------")

        elif x==2:
            print("------------")
            print("|          |")
            print("|   0  0   |")
            print("|          |")
            print("------------")

        elif x==3:
            print("------------")
            print("|     0    |")
            print("|     0    |")
            print("|     0    |")
            print("------------")

        elif x==4:
            print("------------")
            print("|  0    0  |")
            print("|          |")
            print("|  0    0  |")
            print("------------")

        elif x==5:
            print("------------")
            print("| 0      0 |")
            print("|     0    |")
            print("| 0      0 |")
            print("------------")

        else :
            print("------------")
            print("|  0    0  |")
            print("|  0    0  |")
            print("|  0    0  |")
            print("------------")
    else:
        print("Thank you !!")
        break