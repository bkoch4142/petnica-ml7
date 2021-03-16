import numpy as np


def update_danger_matrix(color, i_cp, j_cp,danger_matrix):
    if color=='white':
        if danger_matrix[i_cp][j_cp]==2:
            danger_matrix[i_cp][j_cp]=3
        elif danger_matrix[i_cp][j_cp]==0:
            danger_matrix[i_cp][j_cp]=1
    else:
        if danger_matrix[i_cp][j_cp]==1:
            danger_matrix[i_cp][j_cp]=3
        elif danger_matrix[i_cp][j_cp]==0:
            danger_matrix[i_cp][j_cp]=2


def get_danger_matrix(figure_matrix):
    danger_matrix=np.zeros((8,8))

    for i in range(8):
        for j in range(8):
            figure=figure_matrix[i][j]
            position=i,j

            if figure=='B' or figure=='Q':
                #checking down right diagonal
                i_cp,j_cp=position
                i_cp+=1
                j_cp+=1
                while(i_cp<8 and j_cp<8):

                    if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                        update_danger_matrix('white', i_cp, j_cp,danger_matrix)
                        break
                    else:
                        update_danger_matrix('white', i_cp, j_cp,danger_matrix)
                            
                    i_cp+=1
                    j_cp+=1
                
                #checking up left diagonal
                i_cp,j_cp=position
                i_cp-=1
                j_cp-=1
                while(i_cp>-1 and j_cp>-1):

                    if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                        update_danger_matrix('white', i_cp, j_cp,danger_matrix)
                        break
                    else:
                        update_danger_matrix('white', i_cp, j_cp,danger_matrix)

                            
                    i_cp-=1
                    j_cp-=1 
                    
                #checking up right diagonal
                i_cp,j_cp=position
                i_cp-=1
                j_cp+=1
                while(i_cp>-1 and j_cp<8):

                    if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                        update_danger_matrix('white', i_cp, j_cp,danger_matrix)

                        break
                    else:
                        update_danger_matrix('white', i_cp, j_cp,danger_matrix)

                            
                    i_cp-=1
                    j_cp+=1
                    
                #checking up right diagonal
                i_cp,j_cp=position
                i_cp+=1
                j_cp-=1
                while(i_cp<8 and j_cp>-1):

                    if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                        update_danger_matrix('white', i_cp, j_cp,danger_matrix)
                        break
                    else:
                        update_danger_matrix('white', i_cp, j_cp,danger_matrix)
                            
                    i_cp+=1
                    j_cp-=1
        #############################################################
            if figure=='N':

                #right up
                i_cp,j_cp=position
                i_cp-=1
                j_cp+=2
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('white', i_cp, j_cp,danger_matrix)
                            
                
                #right down
                i_cp,j_cp=position
                i_cp+=1
                j_cp+=2
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('white', i_cp, j_cp,danger_matrix)

                    
                #left down
                i_cp,j_cp=position
                i_cp+=1
                j_cp-=2
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('white', i_cp, j_cp,danger_matrix)
                            

                    
                #left up
                i_cp,j_cp=position
                i_cp-=1
                j_cp-=2
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('white', i_cp, j_cp,danger_matrix)



                #up right
                i_cp,j_cp=position
                i_cp-=2
                j_cp+=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('white', i_cp, j_cp,danger_matrix)
                        
                
                #up left
                i_cp,j_cp=position
                i_cp-=2
                j_cp-=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('white', i_cp, j_cp,danger_matrix)

                    
                #down  right
                i_cp,j_cp=position
                i_cp+=2
                j_cp+=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('white', i_cp, j_cp,danger_matrix)
                            

                #down left 
                i_cp,j_cp=position
                i_cp+=2
                j_cp-=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('white', i_cp, j_cp,danger_matrix)

        #############################################################
            if figure=='P':
                
                #up left 
                i_cp,j_cp=position
                i_cp-=1
                j_cp-=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('white', i_cp, j_cp,danger_matrix)

                #up right
                i_cp,j_cp=position
                i_cp-=1
                j_cp+=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('white', i_cp, j_cp,danger_matrix)
        #############################################################
            if figure=='R' or figure=='Q':
                #checking right
                i_cp,j_cp=position
                j_cp+=1
                while(j_cp<8):

                    if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                        update_danger_matrix('white', i_cp, j_cp,danger_matrix)
                        break
                    else:
                        update_danger_matrix('white', i_cp, j_cp,danger_matrix)
                    j_cp+=1

                #checking left
                i_cp,j_cp=position
                j_cp-=1
                while(j_cp>-1):

                    if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                        update_danger_matrix('white', i_cp, j_cp,danger_matrix)
                        break
                    else:
                        update_danger_matrix('white', i_cp, j_cp,danger_matrix)
                    j_cp-=1

                #checking up
                i_cp,j_cp=position
                i_cp-=1
                while(i_cp>-1):

                    if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                        update_danger_matrix('white', i_cp, j_cp,danger_matrix)
                        break
                    else:
                        update_danger_matrix('white', i_cp, j_cp,danger_matrix)
                    i_cp-=1

                #checking down
                i_cp,j_cp=position
                i_cp+=1
                while(i_cp<8):

                    if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                        update_danger_matrix('white', i_cp, j_cp,danger_matrix)
                        break
                    else:
                        update_danger_matrix('white', i_cp, j_cp,danger_matrix)
                    i_cp+=1



        #############################################################
            if figure=='K':
                #up left 
                i_cp,j_cp=position
                i_cp-=1
                j_cp-=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('white', i_cp, j_cp,danger_matrix)

                #up right
                i_cp,j_cp=position
                i_cp-=1
                j_cp+=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('white', i_cp, j_cp,danger_matrix)

                #up 
                i_cp,j_cp=position
                i_cp-=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('white', i_cp, j_cp,danger_matrix)

                #down
                i_cp,j_cp=position
                i_cp+=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('white', i_cp, j_cp,danger_matrix)

                #right
                i_cp,j_cp=position
                j_cp+=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('white', i_cp, j_cp,danger_matrix)

                #left 
                i_cp,j_cp=position
                j_cp-=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('white', i_cp, j_cp,danger_matrix)


                #down left 
                i_cp,j_cp=position
                i_cp+=1
                j_cp-=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('white', i_cp, j_cp,danger_matrix)

                #down right
                i_cp,j_cp=position
                i_cp+=1
                j_cp+=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('white', i_cp, j_cp,danger_matrix)
            
        #############################################################
            if figure=='b' or figure=='q':
                #checking down right diagonal
                i_cp,j_cp=position
                i_cp+=1
                j_cp+=1
                while(i_cp<8 and j_cp<8):

                    if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                        update_danger_matrix('black', i_cp, j_cp,danger_matrix)
                        break
                    else:
                        update_danger_matrix('black', i_cp, j_cp,danger_matrix)
                            
                    i_cp+=1
                    j_cp+=1
                
                #checking up left diagonal
                i_cp,j_cp=position
                i_cp-=1
                j_cp-=1
                while(i_cp>-1 and j_cp>-1):

                    if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                        update_danger_matrix('black', i_cp, j_cp,danger_matrix)
                        break
                    else:
                        update_danger_matrix('black', i_cp, j_cp,danger_matrix)
                            
                    i_cp-=1
                    j_cp-=1 
                    
                #checking up right diagonal
                i_cp,j_cp=position
                i_cp-=1
                j_cp+=1
                while(i_cp>-1 and j_cp<8):

                    if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                        update_danger_matrix('black', i_cp, j_cp,danger_matrix)
                        break
                    else:
                        update_danger_matrix('black', i_cp, j_cp,danger_matrix)
                            
                    i_cp-=1
                    j_cp+=1
                    
                #checking up right diagonal
                i_cp,j_cp=position
                i_cp+=1
                j_cp-=1
                while(i_cp<8 and j_cp>-1):

                    if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                        update_danger_matrix('black', i_cp, j_cp,danger_matrix)
                        break
                    else:
                        update_danger_matrix('black', i_cp, j_cp,danger_matrix)
                            
                    i_cp+=1
                    j_cp-=1
                
            if figure=='n':

                #right up
                i_cp,j_cp=position
                i_cp-=1
                j_cp+=2
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('black', i_cp, j_cp,danger_matrix)
                            
                
                #right down
                i_cp,j_cp=position
                i_cp+=1
                j_cp+=2
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('black', i_cp, j_cp,danger_matrix)

                    
                #left down
                i_cp,j_cp=position
                i_cp+=1
                j_cp-=2
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('black', i_cp, j_cp,danger_matrix)
                            

                    
                #left up
                i_cp,j_cp=position
                i_cp-=1
                j_cp-=2
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('black', i_cp, j_cp,danger_matrix)



                #up right
                i_cp,j_cp=position
                i_cp-=2
                j_cp+=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('black', i_cp, j_cp,danger_matrix)
                        
                
                #up left
                i_cp,j_cp=position
                i_cp-=2
                j_cp-=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('black', i_cp, j_cp,danger_matrix)

                    
                #down  right
                i_cp,j_cp=position
                i_cp+=2
                j_cp+=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('black', i_cp, j_cp,danger_matrix)
                            

                #down left 
                i_cp,j_cp=position
                i_cp+=2
                j_cp-=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('black', i_cp, j_cp,danger_matrix)

            if figure=='p':
                #down left 
                i_cp,j_cp=position
                i_cp+=1
                j_cp-=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('black', i_cp, j_cp,danger_matrix)

                #down right
                i_cp,j_cp=position
                i_cp+=1
                j_cp+=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('black', i_cp, j_cp,danger_matrix)
            if figure=='r' or figure=='q':
                #checking right
                i_cp,j_cp=position
                j_cp+=1
                while(j_cp<8):

                    if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                        update_danger_matrix('black', i_cp, j_cp,danger_matrix)
                        break
                    else:
                        update_danger_matrix('black', i_cp, j_cp,danger_matrix)
                    j_cp+=1

                #checking left
                i_cp,j_cp=position
                j_cp-=1
                while(j_cp>-1):

                    if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                        update_danger_matrix('black', i_cp, j_cp,danger_matrix)
                        break
                    else:
                        update_danger_matrix('black', i_cp, j_cp,danger_matrix)
                    j_cp-=1

                #checking up
                i_cp,j_cp=position
                i_cp-=1
                while(i_cp>-1):

                    if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                        update_danger_matrix('black', i_cp, j_cp,danger_matrix)
                        break
                    else:
                        update_danger_matrix('black', i_cp, j_cp,danger_matrix)
                    i_cp-=1

                #checking down
                i_cp,j_cp=position
                i_cp+=1
                while(i_cp<8):

                    if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                        update_danger_matrix('black', i_cp, j_cp,danger_matrix)
                        break
                    else:
                        update_danger_matrix('black', i_cp, j_cp,danger_matrix)
                    i_cp+=1

            if figure=='k':
                #up left 
                i_cp,j_cp=position
                i_cp-=1
                j_cp-=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('black', i_cp, j_cp,danger_matrix)

                #up right
                i_cp,j_cp=position
                i_cp-=1
                j_cp+=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('black', i_cp, j_cp,danger_matrix)

                #up 
                i_cp,j_cp=position
                i_cp-=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('black', i_cp, j_cp,danger_matrix)

                #down
                i_cp,j_cp=position
                i_cp+=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('black', i_cp, j_cp,danger_matrix)

                #right
                i_cp,j_cp=position
                j_cp+=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('black', i_cp, j_cp,danger_matrix)

                #left 
                i_cp,j_cp=position
                j_cp-=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('black', i_cp, j_cp,danger_matrix)


                #down left 
                i_cp,j_cp=position
                i_cp+=1
                j_cp-=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('black', i_cp, j_cp,danger_matrix)

                #down right
                i_cp,j_cp=position
                i_cp+=1
                j_cp+=1
                if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                    update_danger_matrix('black', i_cp, j_cp,danger_matrix)
            
    return danger_matrix

mtx=[
['1', '1', '1', '1', '1', '1', '1', 'k'],
['1', '1', '1', '1', '1', '1', 'Q', '1'],
['1', '1', '1', '1', '1', '1', '1', '1'],
['1', '1', '1', 'r', '1', '1', '1', '1'],
['1', '1', '1', '1', '1', '1', '1', '1'],
['1', '1', '1', '1', '1', '1', '1', '1'],
['1', '1', '1', '1', '1', '1', 'R', '1'],
['1', '1', '1', '1', '1', '1', '1', '1'],
]

danger_matrix=get_danger_matrix(mtx)

# def is_checkmate()

def is_someone_giving_check_or_checkmate(figure_matrix, danger_matrix):
    for i in range(8):
        for j in range(8):
            if figure_matrix[i][j]=='k':
                if danger_matrix[i][j]==1 or danger_matrix[i][j]==3:
                    check='W'

                    #checking checkmate
                    can_move=False

                    #up left 
                    i_cp,j_cp=i,j
                    i_cp-=1
                    j_cp-=1
                    if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                        if danger_matrix[i_cp][j_cp]==0 or danger_matrix[i_cp][j_cp]==2:
                            can_move=True
                            return f"{check}\n{int(not can_move)}"

                    #up right
                    i_cp,j_cp=i,j
                    i_cp-=1
                    j_cp+=1
                    if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                        if danger_matrix[i_cp][j_cp]==0 or danger_matrix[i_cp][j_cp]==2:
                            can_move=True
                            return f"{check}\n{int(not can_move)}"


                    #up 
                    i_cp,j_cp=i,j
                    i_cp-=1
                    if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                        if danger_matrix[i_cp][j_cp]==0 or danger_matrix[i_cp][j_cp]==2:
                            can_move=True
                            return f"{check}\n{int(not can_move)}"
                    #down
                    i_cp,j_cp=i,j
                    i_cp+=1
                    if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                        if danger_matrix[i_cp][j_cp]==0 or danger_matrix[i_cp][j_cp]==2:
                            can_move=True
                            return f"{check}\n{int(not can_move)}"
                    #right
                    i_cp,j_cp=i,j
                    j_cp+=1
                    if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                        if danger_matrix[i_cp][j_cp]==0 or danger_matrix[i_cp][j_cp]==2:
                            can_move=True
                            return f"{check}\n{int(not can_move)}"
                    #left 
                    i_cp,j_cp=i,j
                    j_cp-=1
                    if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                        if danger_matrix[i_cp][j_cp]==0 or danger_matrix[i_cp][j_cp]==2:
                            can_move=True
                            return f"{check}\n{int(not can_move)}"

                    #down left 
                    i_cp,j_cp=i,j
                    i_cp+=1
                    j_cp-=1
                    if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                        if danger_matrix[i_cp][j_cp]==0 or danger_matrix[i_cp][j_cp]==2:
                            can_move=True
                            return f"{check}\n{int(not can_move)}"

                    #down right
                    i_cp,j_cp=i,j
                    i_cp+=1
                    j_cp+=1
                    if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                        if danger_matrix[i_cp][j_cp]==0 or danger_matrix[i_cp][j_cp]==2:
                            can_move=True
                            return f"{check}\n{int(not can_move)}"

                    return f"{check}\n{int(not can_move)}"

            if figure_matrix[i][j]=='K':
                if danger_matrix[i][j]==2 or danger_matrix[i][j]==3:
                    check='B'

                    #checking checkmate
    return '-'

for i in danger_matrix:
    print(i)

print(is_someone_giving_check_or_checkmate(mtx, danger_matrix))