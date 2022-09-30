from random import random
import random as random


money = 1000
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

class Game():
    def __init__(self, random_card):
        random_card = random.choice(cards)
        self.random_card = random_card

    def player():
        

    def game(self): 
        croupier = 0
        shouldEnd = True
        while shouldEnd:
            if croupier >= 21:
                break

            croupier = croupier + self.random_card
            print(croupier)
            
            
            
            while croupier < 21:
                draw = input("Do you want draw next card? Y or N?")
                if draw == "y":
                    a = self.random_card
                    croupier = croupier + a    
                elif draw == "n":
                
                    print("yoo") 
                    shouldEnd = False
                print(croupier)
                
                
g = Game(random_card=cards)             
g.game()