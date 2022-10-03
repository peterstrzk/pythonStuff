from random import random
import random as random


money = 1000
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

class Game():
    def __init__(self):
        pass

    # def tossing(): 
        # croupier_card = random.choice(cards)
        # self.bet = bet
        # random_card = random.choice(cards)
        # self.random_card = random_card

    # def betting(self):
    #     print(self.bet)
    #     value_of_bet = int(input("How much do you want to bet?"))
    #     value_after_bet = self.bet - value_of_bet
    #     print(value_after_bet)

        

    def croupier(self): 
         
        croupier_card = random.sample(cards, 2)
        print(croupier_card)
        croupier = 0
        shouldEnd = True
        while shouldEnd:
            if croupier >= 21:
                break
            
            croupier = croupier + croupier_card[0] + croupier_card[1]
            print(croupier)
            
            
            
            while croupier < 21:
                draw = input("Do you want draw  next card or deal(n)? Y or N?")
                if draw == "y":
                    croupier_card = random.choice(cards)
                    a = croupier_card
                    croupier = croupier + a
                    
                elif draw == "n":
                
                    print("yoo") 
                    shouldEnd = False
                    break
                print(croupier)

            if croupier < 21:
                print("you lose!")  
                
# g = Game(random_card=cards, bet = money)             
g = Game()
# g.betting()
g.croupier()