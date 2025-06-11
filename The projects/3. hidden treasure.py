print("Hello, I'm Clodsire, the game bot!")
print("You need to choose your path. If you're ready, say hi!!\n")

print("Game Start")
print("Hidden Treasure")

print("You need to find the treasure... but can you?")
print("You're in the jungle and you see a boat and think:")
print("- A boat might be a good choice.")
print("But the lake is infested with alligators.\n")

boat = int(input("If you want to risk your life using the boat, type 1. If you want to stay safe in the jungle, type 2:\n"))

if boat == 1:
    print("The boat was a good choice!\n")
    print("The alligators ignored you, and you're closer to the treasure!")
    print("You see a big mountain. The treasure could be at the top or behind the mountain.")

    mountain = int(input("If you want to climb it, type 1. If you want to go around on the left, type 2. If you want to go around on the right, type 3:\n"))
    
    if mountain == 1:
        print("Yes, you're doing well!\n")
        print("But you didn't find anything at the top. :/")

        final = int(input("If you want to keep searching, type 1. If you want to go down the mountain, type 2:\n"))
        if final == 1:
            print("You found it, congratulations!!!!!!!!\n")
        else:
            print("Going down the mountain, you fell into a hole and died!")
            print("You died.\n")
            
    elif mountain == 2:
        print("You chose to go to the left, but a group of wolves attacked you. You lost a lot of blood and died.")
    
    else:
        print("You were walking peacefully until a coconut fell on your head.")
        print("Yeah... you died.\n")

else:
    print("Oh no! You were bitten by a snake and died from the poison!")
    print("You died.\n")

print("Game Over.")
