#Hand Cricket

import random

computer = random.choice([1,2,3,4,5,6])
youstr = int(input("Entre "))
l = [1,2,3,4,5,6]


you = l[youstr]


print(f"You choose {l[youstr]} \nComputer choose {[computer]}")

if (computer == you) :
    print("out")  
else:
    print("you win")    