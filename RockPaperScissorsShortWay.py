import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lost!")
else:
    print(game_images[user_choice])
    computer_random_choice = random.randint(0, 2)
    print("Computer chose")
    print(game_images[computer_random_choice])


    if user_choice == 0 and computer_random_choice == 2:
        print("You win")
    elif user_choice == 2 and computer_random_choice == 0:
        print("You lose")
    elif computer_random_choice > user_choice:
        print("You Lose")
    elif user_choice > computer_random_choice:
        print("You win")
    elif computer_random_choice == user_choice:
        print("Its a draw")