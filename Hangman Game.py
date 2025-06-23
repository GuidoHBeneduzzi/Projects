def main():
    print("Welcome to the Hangman Game!")
    print("I am Clodsire, your friendly chatbot.")
    print("Guess the word one letter at a time. You have 6 strikes.")

    word = input("Enter the secret word: ")
    white_space = []
    word_array = []
    
    for i in range(len(word)):
        white_space.append("_")
    print(" ".join(white_space))

    for i in word:
        word_array.append(i)
      
    cont = len(word)
    strike = 0
    
    while cont > 0 and strike < 6:
        answer = input("Your guess: ")
        error = True
        
        for i in range(len(word)):
            if answer == word_array[i] and white_space[i] == "_":
                white_space[i] = answer
                cont -= 1
                error = False
    
        if error:
            strike += 1
            
        print(" ".join(white_space))
        print("Strikes:", strike)
    
    if cont == 0:
        print("Congratulations! You won!")
    else:
        print("Oh no! You lost. The word was:", word)

main()
