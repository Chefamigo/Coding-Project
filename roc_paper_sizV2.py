import random

def play():
    user = input("'r' for rock, 'p' for paper. 's' for scissors:")
    
    
    if user == 'r':
        print("you picked rock")
    if user =='p':
        print("you picked paper")
    if user == 's':
        print("you picked scissors")
    
    computer = random.choice(['r', 'p', 's'])
    if computer == 'r':
        print("They picked rock")
    if computer =='p':
        print("They picked paper")
    if computer == 's':
        print("They picked scissors")
   
    if user == computer:
        return 'it\'s a tie'

    if is_win(user, computer):
        return 'you won!'
    
    return 'you lost!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's'and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())

