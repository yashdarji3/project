import random

def get_random_word():
    words = ["python", "hangman", "program", "challenge", "code"]
    return random.choice(words)

def play_game():
    word = get_random_word()
    guessed_letters = []
    attempts = 6
    print("🎉 Welcome to Hangman!\n")

    while attempts > 0:
        display = [letter if letter in guessed_letters else "_" for letter in word]
        print("Word:", " ".join(display))

        if "_" not in display:
            print("\n🏆 Congratulations! You guessed the word:", word)
            break

        guess = input("\nGuess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            print("Good guess!")
            guessed_letters.append(guess)
        else:
            print("Wrong guess!")
            attempts -= 1
            guessed_letters.append(guess)

        print("Attempts left:", attempts)

    else:
        print("\n💀 Game Over! The word was:", word)

if __name__ == "__main__":
    play_game()
