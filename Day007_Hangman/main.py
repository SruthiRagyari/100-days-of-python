import random

word_list = ["apple", "banana", "mango", "grape", "peach"]

logo = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __   
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\  
| | | | (_| | | | | (_| | | | | | | (_| | | | | 
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_| 
                    __/ |                      
                   |___/                       
"""

stages = [
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """
]

lives = 6
print(logo)

chosen_word = random.choice(word_list)

word_length = len(chosen_word)
display = "_" * word_length
print("Word to guess:", display)

game_over = False
correct_letters = []

while not game_over:
    print(f"\n****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    new_display = ""

    for letter in chosen_word:
        if letter == guess:
            new_display += letter
            if guess not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            new_display += letter
        else:
            new_display += "_"

    display = new_display
    print("Word to guess:", display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"\nIT WAS {chosen_word}! YOU LOSE")

    if "_" not in display:
        game_over = True
        print("\nYOU WIN")

    print(stages[lives])