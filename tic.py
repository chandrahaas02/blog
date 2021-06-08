import numpy as np 

board = np.zeros((3,3))


def Print(board):
    for  i in range(3):
        print("|",end="")
        for j in range(3):
            if board[i][j]==1:
                print("X",end="")
            if board[i][j]==0:
                print(" ",end="")
            if board[i][j]==-1:
                print("O",end="")
            print("|",end="")
        print("\n")



def isEnd(board) :
    if(board[0][0]==board[1][1]==board[2][2])and board[0][0]!=0:
        z=board[0][0]
        return z
    if(board[0][2]==board[1][1]==board[2][0])and board[0][2]!=0:
        z=board[0][2]
        return z
    for i in range(board.shape[0]):
        if np.all(board[i]==board[i][0])and board[i][0]!=0:
            z=board[i][0]
            return z
    trans_arr = board.T
    for i in range(trans_arr.shape[0]):
        if np.all(trans_arr[i] == trans_arr[i][0])and trans_arr[i][0]!=0:
            z=board[0][i]
            return z
    
    if draw(board):
        #print("it is a draw")
        return 2
    return 0


def draw(board):
    for i in range(3):
        for j in range(3):
            if(board[i][j]==0):
                return 0
    return 1


def comp_play():
    worst=100
    x=0
    y=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==0:
                board[i][j]=-1
                score=minimax(board,0,True)
                board[i][j]=0
                if score < worst :
                    worst=score
                    x,y=i,j
    return x,y


def minimax(board,depth,isMaximizing):
    z=isEnd(board)
    if z==1 :
        return 1
    if z==-1 :
        return -1
    if draw(board) :
        return 0
    
    if isMaximizing :
        best= -100
        for i in range(3):
            for j in range(3):
                if board[i][j]==0:
                    board[i][j]=1
                    score=minimax(board,depth+1,False)
                    board[i][j]=0
                    if score>best :
                        best=score
        return best
    if not isMaximizing :
        worst=100
        for i in range(3):
            for j in range(3):
                if board[i][j]==0:
                    board[i][j]= -1
                    score=minimax(board,depth+1,True)
                    board[i][j]=0
                    if score<worst :
                        worst=score
        return worst
    




k=0
while  isEnd(board)==0:
       j=k%2
       if j==0:
           x,y=input("Player"+str(j)+" Please enter your move in x,y co-ordinates").split()
           board[int(x)][int(y)]=1
       else:
           x,y= comp_play()
           board[x][y]=-1
       k+=1
       Print(board)

z=isEnd(board)
if z == 1 :
    print("player 0 is winner")
if z == -1 :
    print("player 1 is winner")
if z== 2 :
    print("it is a draw")