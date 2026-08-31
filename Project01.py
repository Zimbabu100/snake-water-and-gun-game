import random

computer = random.choice([1, 0, -1])
# if(computer == 1):
#     computer = "snake"
# elif(computer == -1):
#     computer = "water"
# elif(computer == 0):
#     computer = "gun"

# print(computer)

you = int(input("Enter your number : "))

youdic = {1 : "snake", -1 : "water", 0 : "gun"}

if you not in youdic:
    print("Invalid choice! please Enter 1, 0 or -1")

else:
    # print(f"your choice {you}\ncomputer choice {computer}")
    print(f"Your choice: {youdic[you]}\nComputer choice: {youdic[computer]}")

    if (computer == you):
        print ("Game is Tie")

    else:
        if(computer == -1 and you == 1):
            print("You Win!")
        elif(computer == -1 and you == 0):
            print("You loss!")
        elif(computer == 1 and you == -1):
            print("You loss!")
        elif(computer == 1 and you == 0):
            print("You Win!")
        elif(computer == 0 and you == 1):
            print("You loss!")
        elif(computer == 0 and you == -1):
            print("You Win!")

