import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words =[]
    tries = 6
    print("lets play hangman")
    print(display_hangman(tries))
    print(f"word: {word_completion}")
    #print("\n")
    print(f"number of letters: {len(word)}")
    print("\n")
    while not guessed and tries >0:
        guess = input("guess a letter or word:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("you already guessed the letter ", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(guess, "is in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True


        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("you already guessed the word ", guess)
            elif guess != word:
                print(guess," is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word


        else:
            print("not a valid guess")

        print(display_hangman(tries))
        print(f"guessed letters : {guessed_letters} \n")
        print(f"guessed_words : {guessed_words}\n")
        print(word_completion)
        print("\n")

    if guessed:
        print("congrats, you guessed")
    else:
        print("you ran out of tries. the word was ",word)


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("play again?(Y/N)").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
