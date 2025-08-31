import random
#generate number 

def generate_number():
    # Generate a random 4-digit number as a string
    return str(random.randint(1000, 9999))

def cows_and_bulls(secret, guess):
    cows = 0
    bulls = 0
    
    # Count cows (correct digit in correct place)
    for i in range(4):
        if guess[i] == secret[i]:
            cows += 1
    
    # Count bulls (correct digit in wrong place)
    for i in range(4):
        if guess[i] != secret[i] and guess[i] in secret:
            bulls += 1
    
    return cows, bulls

def play_game():
    print("Welcome to the Cows and Bulls Game!")
    secret_number = generate_number()
    attempts = 0
    
    while True:
        guess = input("Enter a 4-digit number: ")
        
        # Check valid input
        if not guess.isdigit() or len(guess) != 4:
            print("Please enter a valid 4-digit number.")
            continue
        
        attempts += 1
        cows, bulls = cows_and_bulls(secret_number, guess)
        
        print(f"{cows} cows, {bulls} bulls")
        
        if cows == 4:
            print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

# Run the game
if _name_ == "_main_":
    play_game()
