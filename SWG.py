while True:
    a = input("Player 1: snake, water or gun? ")
    b = input("Player 2: snake, water or gun? ")
    if a.lower() in ['snake','water','gun'] and b.lower() in ['snake','water','gun']:
        if a.lower() == 'snake' and b.lower() == 'water':
            print("PLAYER ONE WINS")
        elif a.lower() == 'snake' and b.lower() == 'gun':
            print("PLAYER TWO WINS")
        elif a.lower() == 'water' and b.lower() == 'snake':
            print("PLAYER TWO WINS")
        elif a.lower() == 'water' and b.lower() == 'gun':
            print("PLAYER ONE WINS")
        elif a.lower() == 'gun' and b.lower() == 'water':
            print("PLAYER TWO WINS")
        elif a.lower() == 'gun' and b.lower() == 'snake':
            print("PLAYER ONE WINS")
        else:
            print("IT IS A DRAW")
    else:
        print("INVALID INPUT. GAME TERMINATED")
    h = input("DO YOU WANT TO CONTINUE? yes/no ")
    if h.lower() == 'yes' or h.lower() == 'no':
        if h.lower() == 'no':
            print("THANK YOU FOR PLAYING")
            break
    else:
        print("INVALID INPUT. GAME TERMINATED.")
