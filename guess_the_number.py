import random
while True:
    secret_number =random.randint(1,1000)
    guess_counts =0
    guess_limit = 8
    guessed_correctly = False
    while guess_counts< guess_limit:
        try:
            guess= int(input("Guess the number (1-1000): "))
            guess_counts += 1
            if guess == secret_number:
                print("CONGRATULATIONS YOU HAVE GUESSED THE SECRET NUMBER")
                guessed_correctly= True
                break
            if guess_counts== guess_limit:
                pass
            else:
                if guess < secret_number:
                    print("Your guess is too low. Try again")
                elif guess > secret_number:
                    print("Your guess is too high. Try again")
                else:
                    print("YOU ARE WRONG TRY AGAIN")
                print(f"Chance left:{guess_limit - guess_counts}")
        except ValueError :
            print("PLEASE ENTER A VALID NUMBER")
            guess_counts +=1
    if not guessed_correctly:
            print("SORRY YOU ARE OUT OF GUESSES. THE SECRET NUMBER WAS", secret_number)
    play_again =input("PLAY AGAIN? (YES/NO): ").strip().upper()
    if play_again== "NO":
        print("THANKS FOR PLAYING! GOODBYE.")
