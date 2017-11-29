import random
l=['r','p','s']
nu=int(input("Enter no. of players."))
ch='y'
if nu==1:
    while(ch=='y'):
        ci=random.choice(l)
        ui=input("Enter your choice.")
        if((ci=='r' and ui=='s') or (ci=='s' and ui=='p') or (ci=='p' and ui=='r')):
            print("Computer wins,You lose with the choice ",ui," as Computer had chosen ",ci)
        elif((ui=='r' and ci=='s') or (ui=='s' and ci=='p') or (ui=='p' and ci=='r')):
            print("Congratulations! You win with choice ",ui," as Computer had selected ",ci)
        else:
            print("Game is a draw!")
        ch=input("If you want to play again press <y>")


else:
    while(ch=='y'):
        u1=input("Turn for player 1.")
        u2=input("Turn for player 2.")
        if((u1=='r' and u2=='s') or (u1=='s' and u2=='p') or (u1=='p' and u2=='r')):
            print("Player 1 wins with a ",u1," and Player 2 loses with a ",u2)
            print("Congratulations Player 1!")
        elif((u2=='r' and u1=='s') or (u2=='s' and u1=='p') or (u2=='p' and u1=='r')):
            print("Player 2 wins with a ",u2," and Player 1 loses with a ",u1)
            print("Congratulations Player 2!")
        else:
            print("Game is a draw!")
        ch=input("If you want to play again press <y>")
