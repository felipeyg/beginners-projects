#NAO ACABEI, VOLTO AQUI DEPOIS


#in this code i'm gonna try to create a tic tac toe game for 2 users
# visual part, def to check if its over, loop to run until its over, something to check if someone already played in this space

player1 = {}
player2 = {}
already_played = {}


    while (not its_over()):
        player1_play = input("Make your play:\n")
        if player1_play :
            

game = """ Please choose one space that haven't been played yet 
            a1 | b1 | c1 
            a2 | b2 | c2 
            a3 | b3 | c3 """


print(game)

def its_over():

    if 'a1' in player1 and 'b1' in player1 and 'c1' in player1:
        return True
    elif 'a2' in player1 and 'b2' in player1 and 'c2' in player1:
        return True
    elif 'a3' in player1 and 'b3' in player1 and 'c3' in player1:
        return True
    elif 'a1' in player1 and 'a2' in player1 and 'a3' in player1:
        return True
    elif 'b1' in player1 and 'b2' in player1 and 'b3' in player1:
        return True
    elif 'c1' in player1 and 'c2' in player1 and 'c3' in player1:
        return True
    elif 'a1' in player1 and 'b2' in player1 and 'c3' in player1:
        return True
    elif 'a3' in player1 and 'b2' in player1 and 'c1' in player1:
        return True
    elif 'a1' in player2 and 'b1' in player2 and 'c1' in player2:
        return True
    elif 'a2' in player2 and 'b2' in player2 and 'c2' in player2:
        return True
    elif 'a3' in player2 and 'b3' in player2 and 'c3' in player2:
        return True
    elif 'a1' in player2 and 'a2' in player2 and 'a3' in player2:
        return True
    elif 'b1' in player2 and 'b2' in player2 and 'b3' in player2:
        return True
    elif 'c1' in player2 and 'c2' in player2 and 'c3' in player2:
        return True
    elif 'a1' in player2 and 'b2' in player2 and 'c3' in player2:
        return True
    elif 'a3' in player2 and 'b2' in player2 and 'c1' in player2:
        return True
    else:
        return False

def check_play1():
    if player1_play in already_played:
        return False
    else:
        already_played.append(player1_play)
        return True

def check_play2():
    if player2_play in already_played:
        return False
    else:
        already_played.append(player2_play)
        return True

its_over()