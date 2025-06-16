import random

def pvp(a, b):
    if a == b:
        return "It's a tie!"
    elif (a == 'r' and b == 's') or (a == 'p' and b == 'r') or (a == 's' and b == 'p'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def vsBot(player):
    bot = random.choice(['r', 'p', 's'])
    if player == bot:
        return "It's a tie!"
    elif (player == 'r' and bot == 's') or (player == 'p' and bot == 'r') or (player == 's' and bot == 'p'):
        return "You win!"
    else:
        return "The bot wins!"

def main():
    print("Hey there! I'm Clodsire, your game bot!")
    print("Let's play Rock, Paper, Scissors!\n")

    choice = int(input(
        "Choose an option:\n"
        "1 - Play against a friend\n"
        "2 - Play against the bot\n"
        "3 - View the rules\n"
        "4 - Exit the game\n"
    ))

    if choice == 1:
        print('Choose your move:')
        print('"r" = Rock')
        print('"p" = Paper')
        print('"s" = Scissors')

        player1 = input("Player 1: ")
        player2 = input("Player 2: ")

        winner = pvp(player1, player2)
        print(winner)

    elif choice == 2:
        print('Choose your move:')
        print('"r" = Rock')
        print('"p" = Paper')
        print('"s" = Scissors')

        player = input("Your move: ")

        winner = vsBot(player)
        print(winner)

    elif choice == 3:
        print("Rules:")
        print("- Rock beats Scissors")
        print("- Scissors beats Paper")
        print("- Paper beats Rock")

    else:
        print("Thanks for playing! See you next time.")
        return

if __name__ == "__main__":
    main()
