
#                                                 Welcome to number scrabble :)
print("welcome to number scrabble :)")
print("played with the list of numbers between 1 and 9 . Each player takes turns picking a number from the list. Once a number has been picked, it cannot be picked again. If a player has picked three numbers that add up to 15, that player wins the game") #game rules
the_exist_numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
player2_numbers = []
player1_numbers = []
z = 0
M = 0
print (the_exist_numbers)
while len(the_exist_numbers) != 0 and M ==0 and z == 0:
    player1 = int(input("player1 pick your number:"))
    while True:                                                          # check if the user 1 input in the list
        if player1 in the_exist_numbers:
            break
        else:
           player1 = int(input("please pick an existing number:"))
    player1_numbers.append(player1)                                      # add the choosen number to player 1 list
    the_exist_numbers.remove(player1)                                    # remove that number from the main list
    print("player1 numbers are", player1_numbers)
    print("THE REMAINING NUMBERS IS")
    print(the_exist_numbers)
    if len(the_exist_numbers) != 0:
        player2 = int(input("player2 pick your number:"))
        while True:                                                      # check if the user 2 input in the list
            if player2 in the_exist_numbers:
                break
            else:
               player2 = int(input("please pick an existing number:"))
        player2_numbers.append(player2)                                  # add the choosen number to player 2 list
        the_exist_numbers.remove(player2)                                # remove that number from the main list
        print("player2 numbers are", player2_numbers)
        print("THE REMAINING NUMBERS IS")
        print(the_exist_numbers)
    if len(player1_numbers)==3:                                          # check if player 1 win
         if player1_numbers [0] + player1_numbers [1] + player1_numbers [2] == 15:
             print(player1_numbers[0], "+", player1_numbers[1], "+", player1_numbers[2], " = 15 ")
             z += 1
    if len(player1_numbers) == 4:
        if player1_numbers [0] + player1_numbers [1] + player1_numbers [3] == 15:
            print(player1_numbers[0], "+", player1_numbers[1], "+", player1_numbers[3], " = 15 ")
            z += 1
        elif player1_numbers [1] + player1_numbers [2] + player1_numbers [3] == 15:
            print(player1_numbers[1], "+", player1_numbers[2], "+", player1_numbers[3], " = 15 ")
            z += 1
        elif player1_numbers [0] + player1_numbers [2] + player1_numbers [3] == 15:
            print(player1_numbers[0], "+", player1_numbers[2], "+", player1_numbers[3], " = 15 ")
            z += 1
    if len(player1_numbers) == 5:
        if player1_numbers[0] + player1_numbers[1] + player1_numbers[4] == 15:
            print(player1_numbers[0], "+", player1_numbers[1], "+", player1_numbers[4], " = 15 ")
            z += 1
        elif player1_numbers[0] + player1_numbers[2] + player1_numbers[4] == 15:
            print(player1_numbers[0], "+", player1_numbers[2], "+", player1_numbers[4], " = 15 ")
            z += 1
        elif player1_numbers[1] + player1_numbers[2] + player1_numbers[4] == 15:
            print(player1_numbers[1], "+", player1_numbers[2], "+", player1_numbers[4], " = 15 ")
            z += 1
        elif player1_numbers[1] + player1_numbers[3] + player1_numbers[4] == 15:
            print(player1_numbers[1], "+", player1_numbers[3], "+", player1_numbers[4], " = 15 ")
            z += 1
        elif player1_numbers[2] + player1_numbers[3] + player1_numbers[4] == 15:
            print(player1_numbers[2], "+", player1_numbers[3], "+", player1_numbers[4], " = 15 ")
            z += 1
        elif player1_numbers[0] + player1_numbers[3] + player1_numbers[4] == 15:
            print(player1_numbers[0], "+", player1_numbers[3], "+", player1_numbers[1], " = 15 ")
            z += 1
    if len(player2_numbers) == 3:                                                # check if player 2 win
         if player2_numbers [0] + player2_numbers [1] + player2_numbers [2] == 15:
             print(player2_numbers [0] ,"+", player2_numbers [1] ,"+", player2_numbers [2], " = 15 ")
             M += 1
             break
    if len(player2_numbers)==4:
        if player2_numbers [0] + player2_numbers [1] + player2_numbers [3] == 15:
            print(player2_numbers[0], "+", player2_numbers[1], "+", player2_numbers[3], " = 15 ")
            M += 1
            break
        elif player2_numbers [1] + player2_numbers [2] + player2_numbers [3] == 15:
            print(player2_numbers[1], "+", player2_numbers[2], "+", player2_numbers[3], " = 15 ")
            M += 1
            break
        elif player2_numbers [0] + player2_numbers [2] + player2_numbers [3] == 15:
            print(player2_numbers[0], "+", player2_numbers[2], "+", player2_numbers[3], " = 15 ")
            M += 1
            break
if len(the_exist_numbers) == 0 and z ==0 and M ==0:        # check if anyone doesn't win
    print(">>> Draw <<< ")
elif z == 1 and M == 0:                                    # check if player 1 win
    print("player 1 is the winner <3 :)")
elif z == 1 and M == 1:                                    # check if player 2 win
    print(">>> Draw <<< ")
elif z == 0 and M == 1:                                    # check if they both win (draw)
    print("player 2 is the winner <3 :)")
