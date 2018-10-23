# game of sticks using loops

# example from online
def sticks_game1():
    sticks = 21 
    print("There are 21 sticks, you can take 1 to 4 sticks at a time.")
    print("Whoever takes the last stick loses!")

    while sticks > 0:
        print(f"Sticks left: {sticks}")
        
        try:
            sticks_taken = input("How many sticks are you taking? ")
            sticks_taken = int(sticks_taken)
        except ValueError as e:
            print(f"Hey! {sticks_taken} is not a number!")
            continue
    
        if sticks_taken > 4 or sticks_taken < 1:
            print("You must take 1, 2, 3, or 4 sticks!")
            continue        
        
        if sticks_taken > sticks:
            print(f"You can only take at most {min(sticks, 4)} sticks!")
            continue
        
        if sticks == 1:
            print("You took the last stick, you lose sucka!")
            break
        
        print(f"Computer took {5 - sticks_taken}.", "\n")
        
        sticks -= 5
# whoever goes first loses

sticks_game1()