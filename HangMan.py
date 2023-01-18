
import random
import HangManAsciArt
import HangManWordsList


print(HangManAsciArt.logo)

chosen_word = random.choice(HangManWordsList.word_list)

display = []
for x in range(0, len(chosen_word)):
    x = "_"
    display += x

end_of_game = False
lives = 6
remaining_lives = 0

while not end_of_game:
    guess = input("Please guess a letter: ").lower()
    print(f"Random word is: {chosen_word}")

    if guess in display:
        print("You already tried that letter")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    if guess not in chosen_word:
        print(f"Sorry, your choice {guess} is incorrect")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win")
    print(HangManAsciArt.stages[lives])

