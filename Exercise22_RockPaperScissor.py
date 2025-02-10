# Exercise 22: Rock Paper Scissors

def rpsWinner(player1, player2):
    r = 'rock'
    p = 'paper'
    s = 'scissors'

    if player1 not in [r, p, s]:
        return "Choose rock, paper, or scissors"
    if player2 not in [r, p, s]:
        return "Choose rock, paper, or scissors" 
    
    if player1 == r and player2 == s:
        return 'player one'
    if player1 == r and player2 == p:
        return 'player two'
    
    if player1 == p and player2 == r:
        return 'player one'
    if player1 == p and player2 == s:
        return 'player two'
    
    if player1 == s and player2 == p:
        return 'player one'
    if player1 == s and player2 == r:
        return 'player two'
    
    return 'tie'

assert rpsWinner('rock', 'paper') == 'player two'
assert rpsWinner('rock', 'scissors') == 'player one'
assert rpsWinner('paper', 'scissors') == 'player two'
assert rpsWinner('paper', 'rock') == 'player one'
assert rpsWinner('scissors', 'rock') == 'player two'
assert rpsWinner('scissors', 'paper') == 'player one'
assert rpsWinner('rock', 'rock') == 'tie'
assert rpsWinner('paper', 'paper') == 'tie'
assert rpsWinner('scissors', 'scissors') == 'tie'