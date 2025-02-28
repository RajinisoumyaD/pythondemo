import random

target = random.randint(1,100)

while True:
    
    userChoice = input("guess the target or Quit: ")
    if(userChoice == "Quit"):
        break

    userChoice = int(userChoice)


    if (userChoice == target):
        print("Success : Correct Guess!!")
        break

    elif(userChoice < target):
        print("your number was too small. take a bigger guess..")

    else:
        print("your number was too big. take a smaller guess..")



print("----GAME OVER----")