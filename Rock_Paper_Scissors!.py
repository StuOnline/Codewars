def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"



    def rps(p1, p2):
        d1 = [('paper','rock'), ('rock', 'scissors'), ('scissors', 'paper')]
        return 'Draw!' if p1 == p2 else "Player {} won!".format(1 if (p1, p2) in d1 else 2)




    def rps(p1, p2):
        return f"Player {1+(p1[0]+p2[0] in 'psrp')} won!" if p1 != p2 else 'Draw!'    