def display(a,b,c):
    print(a)
    print(b)
    print(c)

def pos_cho():
    h = 1
    while h:
        k = int(input("PLEASE ENTER POSITION: "))
        if k not in [1,2,3,4,5,6,7,8,9]:
            print("PLEASE ENTER VALID POSITION")
        else:
            h = 0
    return k

def user_input(a,b,c,k,l):
    if k in [1,2,3]:
        c[k-1] = l
    if k in [4,5,6]:
        b[k-3-1] = l
    if k in [7,8,9]:
        a[k-6-1] = l

def check(a,b,c):
    for i in range(3):
        if a[i] == b[i] == c[i] == play_1:
            print("PLAYER ONE WINS!!")
            return 1
        elif a[i] == b[i] == c[i] == play_2:
            print("PLAYER TWO WINS!!")
            return 2
    if a[0] == a[1] == a[2] == play_1:
        print("PLAYER ONE WINS")
        return 1
    elif b[0] == b[1] == b[2] == play_1:
        print("PLAYER ONE WINS")
        return 1
    elif c[0] == c[1] == c[2] == play_1:
        print("PLAYER ONE WINS")
        return 1
    elif a[0] == a[1] == a[2] == play_2:
        print("PLAYER TWO WINS")
        return 2
    elif b[0] == b[1] == b[2] == play_2:
        print("PLAYER TWO WINS")
        return 2
    elif c[0] == c[1] == c[2] == play_2:
        print("PLAYER TWO WINS")
        return 2
    elif c[0] == b[1] == a[2] == play_1:
        print("PLAYER ONE WINS")
        return 1
    elif c[2] == b[1] == a[0] == play_1:
        print("PLAYER ONE WINS")
        return 1
    elif c[0] == b[1] == a[2] == play_2:
        print("PLAYER TWO WINS")
        return 2
    elif c[2] == b[1] == a[0] == play_2:
        print("PLAYER TWO WINS")
        return 2


def replay():
    w = input("WANNA PLAY AGAIN? Y/N ")
    if w.lower() == 'y':
        return 1
    else:
        return 0

a = [" "," "," "]
b = [" "," "," "]
c = [" "," "," "]

t = 1

while t:
    play_1 = input("PLAYER ONE: ENTER X/O ")
    if play_1 == "X":
        play_2 = "O"
    elif play_1 == "O":
        play_2 = "X"
    
    j = 1
    ct = 0
    print("\n"*100)
    while j in [1,2]:
        if j == 1:
            print("PLAYER ONE TURN")
            display(a,b,c)
            n = pos_cho()
            user_input(a,b,c,n,play_1)
            if check(a,b,c) == 1:
                break
            print("\n"*100)
            j+=1
            ct+=1
            if ct == 9:
                break
            
        if j == 2:
            print("PLAYER TWO TURN")
            display(a,b,c)
            n = pos_cho()
            user_input(a,b,c,n,play_2)
            if check(a,b,c) == 2:
                break
            print("\n"*100)
            j-=1
            ct+=1
            if ct == 9:
                break
    
    if ct == 9:
        print("GAME DRAWN")
    
    t = replay()


