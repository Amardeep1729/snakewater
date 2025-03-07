'''
1 for snake
-1 for water
0 for gun

'''
import random


computer = random.choice([1,-1,0])
youstr = input("Entre your choice   Snake(s) Water(w) Gun(g):")
youDict = {"s":1 , "w":-1 , "g":0} 
reverseDict = {1:"Snake", -1:"Water", 0:"Gun"}

you = youDict[youstr]
 
# By now we have two numbers(variables), you and computer 

print(f"You choose {reverseDict[you]} \nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("Match draw")

else:

    if (computer == -1 and you == 1):
        print ("You win!")

    elif (computer == -1 and you == 0):
        print ("You lose")

    elif (computer == 1 and you == -1):
        print ("You lose")

    elif (computer == 1 and you == 0):
        print ("You win!")

    elif (computer == 0 and you == -1):
        print ("You win!")

    elif (computer == 0 and you == 1):
        print ("You lose")

    else:
        print("Something went wrong")