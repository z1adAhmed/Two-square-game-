grid = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10", "11", "12", "13", "14", "15", "16"]  # this array has all the numbers, becuz we will replace them with x later
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
        16]  #these are the numbers we can pick from, we want to save a copy that wont be edited
leftSide = [4, 8, 12, 16]
            # these are the numbers on the left side, we made this becuz for example, 4 and 5 arent next to each other

rightSide = [1, 5, 9, 13]
            # these are the numbers on the right side, we made this becuz for example, 9 and 8 arent next to each other

cornerTopNumbers = [1,4]
cornerBottomNumbers = [13,16]
            #numbers at the corners, we need this for checking if the game ended

coreNumbers = [6,7,10,11]
player = True
gameOnGoing = True
def game():  # this is main grid for our game, we integrated variables inside a string then printed it
    # we did this becuz we want to change numbers to "x" later
    print("+====+=======+=======+======+")
    print(f"|  {grid[0]}  |  {grid[1]}  |  {grid[2]}  |  {grid[3]}  |")
    print("+----+-------+-------+------+")
    print(f"|  {grid[4]}  |  {grid[5]}  |  {grid[6]}  |  {grid[7]}  |")
    print("+----+-------+-------+------+")
    print(f"|  {grid[8]}  |  {grid[9]}  |  {grid[10]}  |  {grid[11]}  |")
    print("+----+-------+-------+------+")
    print(f"|  {grid[12]}  |  {grid[13]}  |  {grid[14]}  |  {grid[15]}  |")
    print("+====+=======+=======+======+")


game()  # this starts the game for the first time

def NumberApproved(real, no1, no2): #real means its inputed by the player, otherwise if real is false means its from the computer

    global gameOnGoing

    if real:
        grid[no1 - 1] = "x "
        grid[no2 - 1] = "x "
    else:

        gameOnGoing = True

def CheckNumbers (real, no1, no2):

        def checkifclose():
            # then we check if these numbers are next to each other,
            # e.g five minus four is 1, but they arent next to each other
            if no1 in leftSide:
                if no1 > no2:
                    NumberApproved(real, no1, no2)

            elif no1 in rightSide:
                if no1 < no2:
                    NumberApproved(real, no1, no2)

            else:
                    NumberApproved(real, no1, no2)


        # this is the main function that looks if numbers are next to each other
        if (grid[no1 - 1] != "x " and grid[no2 - 1] != "x "):
            if abs(no1 - no2) == 1:  # checks if the absolute value of the number equals 1
                checkifclose()
            elif abs(no1 - no2) == 4:
                NumberApproved(real, no1, no2)
            if real:
                print("\n" * 100)
                game()
        elif real:
            print("\n" * 100)
            print("Number is already chosen !")
            game()

while (gameOnGoing):
    if player:       #check if player is true, means he is player 1, we print it
        print("【Ｐｌａｙｅｒ　１】")
        player = False       #then we switch it to false so that it switches to player 2

    else:                    #else if its false, means he is player 2, we print it
        print("【Ｐｌａｙｅｒ　２】")
        player = True        #then we switch it to true so that it switches to player 1

    num1 = int(input("Please enter the first number:"))  # ask for the first number
    num2 = int(input("Please enter the second number:"))  # ask for the second number

    if num1 in numbers and num2 in numbers:
        CheckNumbers(True, num1, num2)
    else:
        print("\n" * 100)
        print("Please input a valid number")
        game()

    gameOnGoing = False
    for x in range(1, 17):
        for y in range(1, 17):
            CheckNumbers(False, x, y)

    if not gameOnGoing:
        print("\n" * 100)
        print("    .-=========-.")
        print("    \ -=======-'/")
        print("    _|   .=.   |_")
        if player:
            print("   ((| {𝗣𝗹𝗮𝘆𝗲𝗿𝟮} |))")
        else:
            print("   ((| {𝗣𝗹𝗮𝘆𝗲𝗿𝟭} |))")
        print("    \|   /|\   |/")
        print("     \__ '`' __/")
        print("       _`) (`_")
        print("     _/_______\_")
        print("    /___________\ ")

        restart = input("Type anything to restart:")
        grid = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10", "11", "12", "13", "14", "15", "16"]
        gameOnGoing = True
        player = True
        game()
# ============================================================#
