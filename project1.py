#hangman game
#tic tac toe
#odd/even game
#leetcode 2 game

# odd or even game

import random
computer = random.randint(1,6)
sumvalue = None
def game():
        user = int(input("enter the number between 1 and 6:"))
        if user < 1 or user > 7:
                print("invalide number \n please try again ")
        else:
                print(f"you choose {user} and computer choose {computer} ")
                total = user + computer
        if total%2 == 0 :
                print(f"you win {total}")
        
        else:
                print("you loss")
                play=int(input("Do you want to play again Yes - 1,No - 0: "))
                if play == 1:
                        game()
                else:
                        print("thank you playing")
try:
        game()   

except ZeroDivisionError:
    print(' cannot zero')

