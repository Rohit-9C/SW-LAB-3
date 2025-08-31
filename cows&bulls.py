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

