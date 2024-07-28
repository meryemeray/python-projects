# A fun game of "Rock, Paper, Scissors"
import random

win_count = 0
games_played = 0
draw_count = 0

print("Are you ready to play? Let's go!")
list = ["Rock", "Paper", "Scissors"]

while True:
    rps = input("Rock, Paper, Scissors? (Press Q to quit and S for stats) ").lower()
    comp = random.randint(0,2)
    #list = ["Rock", "Paper", "Scissors"]
    computer = list[comp].lower()
    #win_count = 0
    #print(computer)
    
    if rps == "q": #quit game
        break
    
    if rps == "s":
        if games_played == 0:
            print("We haven't played yet. Up for a challange?")
            continue 
        
        average = round(100/(games_played - draw_count)*win_count, 2)
        print("Games played: " + str(games_played) 
              + "\nGames won: " + str(win_count)
              + "\nGames lost: " + str(games_played - win_count - draw_count)
              + "\nDraw: " + str(draw_count)
              + "\nWin percentage: " + str(average) + "%")
        continue
        
    if rps != "rock" and rps != "paper" and rps != "scissors": #invalid input
        print("Invalid input. Please try one of the options: Rock/Paper/Scissors/Q")
        continue

    if rps == "paper" and computer == "rock": #paper wins against rock
        win_count += 1
        games_played += 1
        print("Computer chose " + computer + ". You won! Your win count is " + str(win_count) + ".")
    elif rps == "rock" and computer == "scissors": #rock wins against scissors
        win_count += 1
        games_played += 1        
        print("Computer chose " + computer + ". You won! Your win count is " + str(win_count) + ".")
    elif rps == "scissors" and computer == "paper": #scissors win against paper
        win_count += 1
        games_played += 1
        print("Computer chose " + computer + ". You won! Your win count is " + str(win_count) + ".")
    elif rps == computer: #draw
        games_played += 1
        draw_count += 1
        print("Draw. You both chose the same!")
    else:
        games_played += 1
        print("Computer chose: " + computer + ". You lost.")