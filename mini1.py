#!/usr/bin/env python3
import random

print("Welcome to rock, paper, scissors!")

rps = ["rock","paper","scissors"]
outcomes = ["Rock beats scissors!", "Paper beats rock!", "Scissors beats paper!", " You win!", "TIE", " You lose!"]
ans = ["yes","no"]

player_score = 0
bot_score = 0

end_game = False


while end_game != True:
    
    player_choice = input("Rock, paper, or scissors? ").lower().strip()
    while player_choice not in rps:
        print("invalid input, please choose rock, paper, or scissors")
        player_choice = input("Rock, paper, or scissors? ").lower().strip()

    print(f"You have chosen {player_choice}")
    
    bot_choice = random.choice(rps)
    print(f"The bot has chosen {bot_choice}")

    if player_choice == bot_choice:
        print(outcomes[4])
    elif player_choice == rps[0]:
        if bot_choice == rps[1]:
            print(outcomes[1]+outcomes[5])
            bot_score += 1
        else:
            print(outcomes[0]+outcomes[3])
            player_score += 1
    elif player_choice == rps[1]:
        if bot_choice == rps[0]:
            print(outcomes[1]+outcomes[3])
            player_score += 1
        else:
            print(outcomes[2]+outcomes[5])
            bot_score += 1
    else:
        if bot_choice == rps[0]:
            print(outcomes[0]+outcomes[5])
            bot_score += 1
        else:
            print(outcomes[2]+outcomes[3])
            player_score += 1
    
    print(f"Your score: {player_score} Bot score: {bot_score}")
    end = input(f"Play Again? ").lower().strip()
    while end not in ans:
        print("Invalid answer, please type yes or no")
        end = input("Play Again? ").lower().strip()
    
    if end == ans[1]:
        end_game = True
    else:
        print("Starting next round")

print("GAME OVER")

