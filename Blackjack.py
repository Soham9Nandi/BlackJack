from replit import clear
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""





while input("Do you want to play Blackjack, kid? Type 'y' if yes or 'n' if no.") == 'y':
    clear()

    # declaring all the required lists
    card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player = []
    dealer = []


    # function that deals the opening hand of the player and the dealer
    def deal_opening_hand():
        player.append(card[random.randint(0, 12)])
        player.append(card[random.randint(0, 12)])
        dealer.append(card[random.randint(0, 12)])
        dealer.append(card[random.randint(0, 12)])


    # functions for dealing another card to the player or dealer
    def deal_another_card_player():
        draw = True
        while (draw == True) and (sum(player) < 21):

            player_draw = input("Type 'y' to draw another card or type 'n' to pass")
            if (player_draw == 'n'):
                draw = False
            else:
                player.append(card[random.randint(0, 12)])
                print(f"Your cards: {player}, Your Score: {sum(player)}")
                print(f"The dealer's first card is {dealer[0]}")
            if sum(player) == 21:
                break
        while (sum(dealer) < 17):
            dealer.append(card[random.randint(0, 12)])


    # declaring function to show final score and declare winner
    def final_score():
        print(f"Your final hand: {player}, Final Score: {sum(player)}")
        print(f"The dealer's final hand: {dealer}, Final Score: {sum(dealer)}")
        if sum(player) > 21:
            print("You bust! You Lose!")
        else:
            if (sum(dealer) <= 21):
                if sum(player) > sum(dealer):
                    if sum(player) and (len(card)==2) == 21:
                        print("YOU WIN WITH BLACKJACK!")
                    else:
                        print("YOU WIN!!!")

                elif sum(player) < sum(dealer):
                    if sum(dealer) and (len(card)==2) == 21:
                        print("DEALER WINS WITH BLACKJACK!\nYOU LOSE!!!")
                    else:
                        print("YOU LOSE!!!")
                else:
                    print("DRAW!")
            else:
                print("The dealer busted! You win!!!")



    print(logo)
    deal_opening_hand()
    print(f"Your opening hand is {player}. Your total score is {player[0]+player[1]}")
    print(f"The dealer's first card is {dealer[0]}")
    deal_another_card_player()
    final_score()









