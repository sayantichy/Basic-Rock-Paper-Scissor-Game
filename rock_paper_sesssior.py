import random
user_score=0
com_score=0
option=["rock", "paper", "scissor"]
while True:
    user_input= input("type rock/paper/scissor or quit to end the game : ").lower()
    if user_input == "quit":
            break
    if user_input not in option:
        print("Your Input is invalid. Put a valid one.")
        continue
    else:
       rand_num= random.randint(0,2)
    computer_pick= option[rand_num]
    if user_input=='rock' and computer_pick == 'paper':
        user_score+=1
        print("you get the point")
        continue
    elif user_input=='rock' and computer_pick == 'scissor':
        user_score+=1
        print("you get the point")
        continue
    elif user_input=='scissor' and computer_pick == 'paper':
        user_score+=1
        print("you get the point")
        continue
    elif (user_input=='paper' and computer_pick == 'paper') or (user_input=='rock' and computer_pick == 'rock')  or (user_input=='scissor' and computer_pick == 'scissscissoror'):
        print('no points')
        continue
    else: 
        com_score+=1
        print("computer get the point")
        continue
    
print("user score : " + str(user_score)  )
print("computer score : " + str(com_score)  )
if user_score> com_score:
    print("You win.")
elif user_score< com_score:
    print("Computer win.")
elif user_score == com_score:
    print("it's a Tie.")
if user_score==0:
    print("Good Luck !! Buddy\nSee You Soon.")