
import random

from english_words import english_words_set


word_list = ["aardvark", "baboon", "camel"]

rand_word_list = []
used_letters = []
blanks = []
# next_game = input("press y to play next turn")
lifes = 6
score = 0
win_score = 0

def randomize_letters():
    global win_score
    rand_word = random.choice(tuple(english_words_set))
    for letters in rand_word:
        rand_word_list.append(letters)
        win_score = win_score + 1
    
    print(f"Amount of letters here is {win_score}")
    blanks.extend('_' * win_score)
    
    
    print(blanks)



def new_game():
    global lifes, score, next_game, used_letters, rand_word_list, win_score
    # next_game = input("press y to play new game")
    while lifes == 0 or score < win_score:
        
        if lifes == 6:
            print ("_________")
            print ("|	 |")
            print ("|")
            print ("|")
            print ("|")
            print ("|")
            print ("|________")
            
        elif (lifes == 5):
            print ("_________")
            print ("|	 |")
            print ("|	 O")
            print ("|")
            print ("|")
            print ("|")
            print ("|________")

        elif (lifes == 4):
            print("_________")
            print ("|	 |")
            print ("|	 O")
            print ("|	 |")
            print ("|	 |")
            print ("|")
            print ("|________")
        elif (lifes == 3):
                print ("_________")
                print ("|	 |")
                print ("|	 O")
                print ("|	\|")
                print ("|	 |")
                print ("|")
                print ("|________")
        elif (lifes == 2):
                print ("_________")
                print ("|	 |")
                print ("|	 O")
                print ("|	\|/")
                print ("|	 |")
                print ("|")
                print ("|________")
        elif (lifes == 1):
                print ("_________")
                print ("|	 |")
                print ("|	 O")
                print ("|	\|/")
                print ("|	 |")
                print ("|	/ ")
                print ("|________")
        elif (lifes == 0):
                print ("_________")
                print ("|	 |")
                print ("|	 O")
                print ("|	\|/")
                print ("|	 |")
                print ("|	/ \ ")
                print ("|________")
                print ("\n")
                print (f"The word was {''.join(rand_word_list)}")
                print ("\n")
                print ("\nYOU LOSE! TRY AGAIN!" ) 
                next_game = input("press y to play new game!")
                lifes = 6
                score = 0
                used_letters = []
                rand_word_list = []
                win_score = 0
                x = ""
                blanks.clear()
                break
        print(f"Points: {score}")
        print(f"lifes: {lifes}")
        user_input = input("wpisz coś")
        


        if user_input in used_letters:
                print("that letter was used here")
                continue    
        for x in range(len(rand_word_list)):
            
            if user_input in  rand_word_list[x]:
                score = score + 1
                print('correct')
                used_letters.append(user_input)
                blanks[x] = user_input
                x = "".join(blanks)
                print(x)
                
            if user_input not in rand_word_list:
                print("incorrect")
                lifes = lifes - 1
                
                used_letters.append(user_input)
                break
    
    
    if score == win_score:
        print("You win!")

        
def petla():
    print("""           
                 ██████╗ ███████╗████████╗███████╗██████╗ ███████╗████████╗ █████╗ ██████╗ ███████╗ █████╗ ██╗  ██╗
                ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══███╔╝██╔══██╗██║ ██╔╝
                ██████╔╝█████╗     ██║   █████╗  ██████╔╝███████╗   ██║   ███████║██████╔╝  ███╔╝ ███████║█████╔╝ 
                ██╔═══╝ ██╔══╝     ██║   ██╔══╝  ██╔══██╗╚════██║   ██║   ██╔══██║██╔══██╗ ███╔╝  ██╔══██║██╔═██╗ 
                ██║     ███████╗   ██║   ███████╗██║  ██║███████║   ██║   ██║  ██║██║  ██║███████╗██║  ██║██║  ██╗
                ╚═╝     ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
                             software                                                                                   
""")

    next_game = input("press y to play new game!")
    randomize_letters()
    new_game()
   
    while next_game == 'y':
        global score, lifes
        randomize_letters()
        new_game()
        

petla()