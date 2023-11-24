import random
name=('rock','paper','scissors')
length=len(name)
#print(length)
random_choice=random.randint(0,length-1)
print(random_choice)
user_choice=int(input("enter the user choice:"))
if user_choice>=3 or user_choice<0:
    print("you entered invalid nuber,you lose.")
else:
    if random_choice == user_choice:
        print("the match is tied")
    elif random_choice == 0 and user_choice == 2:
        print("you lost")
    elif random_choice == 2 and user_choice == 0:
        print("you won the game")
    elif random_choice > user_choice:
        print("you last the game")
    elif random_choice < user_choice:
        if random_choice == user_choice:
            print("the match is tied")
        elif random_choice == 0 and user_choice == 2:
            print("you lost")
        elif random_choice == 2 and user_choice == 0:
            print("you won the game")
        elif random_choice > user_choice:
            print("you last the game")
        elif random_choice < user_choice:
            print("you won the game")


if random_choice == user_choice:
    print("the match is tied")
elif random_choice==0 and user_choice==2:
    print("you lost")
elif random_choice==2 and user_choice==0:
    print("you won the game")
elif random_choice > user_choice:
    print("you last the game")
elif random_choice < user_choice:
    print("you won the game")


