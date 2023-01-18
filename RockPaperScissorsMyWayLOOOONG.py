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
choices = [rock, paper, scissors]
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.")
int_user_choice = int(user_choice)
computer_random_choice = random.randint(0, 2)
print(computer_random_choice)

if int_user_choice == 0 and computer_random_choice == 1:
    print(int_user_choice)
    print(rock)
    print("Computer chose: ")
    print(f"{computer_random_choice}")
    print(paper)
    print("You lose")
elif int_user_choice == 1 and computer_random_choice == 2:
    print(int_user_choice)
    print(paper)
    print("Computer chose: ")
    print(f"{computer_random_choice}")
    print(scissors)
    print("You lose")
elif int_user_choice == 2 and computer_random_choice == 1:
    print(int_user_choice)
    print(scissors)
    print("Computer chose: ")
    print(f"{computer_random_choice}")
    print(rock)
    print("You lose")
elif int_user_choice == 1 and computer_random_choice == 0:
    print(int_user_choice)
    print(paper)
    print("Computer chose: ")
    print(f"{computer_random_choice}")
    print(rock)
    print("You win")
elif int_user_choice == 2 and computer_random_choice == 1:
    print(int_user_choice)
    print(scissors)
    print("Computer chose: ")
    print(f"{computer_random_choice}")
    print(paper)
    print("You win")
elif int_user_choice == 1 and computer_random_choice == 2:
    print(int_user_choice)
    print(paper)
    print("Computer chose: ")
    print(f"{computer_random_choice}")
    print(scissors)
    print("You win")
elif int_user_choice == 0 and computer_random_choice == 0:
    print(int_user_choice)
    print(rock)
    print("Computer chose: ")
    print(f"{computer_random_choice}")
    print(rock)
    print("Draw")
elif int_user_choice == 1 and computer_random_choice == 1:
    print(int_user_choice)
    print(paper)
    print("Computer chose: ")
    print(f"{computer_random_choice}")
    print(paper)
    print("Draw")
elif int_user_choice == 2 and computer_random_choice == 2:
    print(int_user_choice)
    print(scissors)
    print("Computer chose: ")
    print(f"{computer_random_choice}")
    print(scissors)
    print("Draw")
elif int_user_choice == 0 and computer_random_choice == 2:
    print(int_user_choice)
    print(rock)
    print("Computer chose: ")
    print(f"{computer_random_choice}")
    print(scissors)
    print("You win")
elif int_user_choice == 2 and computer_random_choice == 0:
    print(int_user_choice)
    print(scissors)
    print("Computer chose: ")
    print(f"{computer_random_choice}")
    print(rock)
    print("You lose")
else:
    print("This is not working")
'''
Rules:
rock (0)
Paper (1)
Scissors (2)
Rock + Paper = Paper win
Paper + Scissors = Scissors win
Scissors + Rock = Rock win

0 - 0
0 - 1
0 - 2

1 - 0
1 - 1
1 - 2

2 - 0
2 - 1 
2 - 2
'''
