import random
import string

def randomize(len_password):
    password = ""
    for i in range(len_password):
        rand = random.randint(1, 3)
        if rand == 1:
            password += str(random.randint(0, 9))
        
        elif rand == 2:
            char_random = random.randint(0, 1)
            if char_random == 0:
                password += random.choice(string.ascii_lowercase)
            else:
                password += random.choice(string.ascii_uppercase)
        
        elif rand == 3:
            special_characters = "!@#$%&?/"
            password += random.choice(special_characters)
            
    return password
    
def main():
    
    print("Hello, I'm Clodsire, the chatbot that can generate random passwords (really random).")
    
    len_password = int(input("Enter the length of your password: "))
    
    final_password = randomize(len_password)
    
    print(final_password)    

main()
