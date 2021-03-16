import numpy as np


def update(color, i_cp, j_cp):
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


def update_danger_matrix(figure, position, figure_matrix, danger_matrix):
#############################################################
    if figure=='B' or figure=='Q':
        #checking down right diagonal
        i_cp,j_cp=position
        i_cp+=1
        j_cp+=1
        while(i_cp<8 and j_cp<8):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                update('white', i_cp, j_cp)
                break
            else:
                update('white', i_cp, j_cp)
                    
            i_cp+=1
            j_cp+=1
        
        #checking up left diagonal
        i_cp,j_cp=position
        i_cp-=1
        j_cp-=1
        while(i_cp>-1 and j_cp>-1):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                update('white', i_cp, j_cp)
                break
            else:
                update('white', i_cp, j_cp)

                    
            i_cp-=1
            j_cp-=1 
            
        #checking up right diagonal
        i_cp,j_cp=position
        i_cp-=1
        j_cp+=1
        while(i_cp>-1 and j_cp<8):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                update('white', i_cp, j_cp)

                break
            else:
                update('white', i_cp, j_cp)

                    
            i_cp-=1
            j_cp+=1
            
        #checking up right diagonal
        i_cp,j_cp=position
        i_cp+=1
        j_cp-=1
        while(i_cp<8 and j_cp>-1):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                update('white', i_cp, j_cp)
                break
            else:
                update('white', i_cp, j_cp)
                    
            i_cp+=1
            j_cp-=1
#############################################################
    if figure=='N':

        #right up
        i_cp,j_cp=position
        i_cp-=1
        j_cp+=2
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('white', i_cp, j_cp)
                    
        
        #right down
        i_cp,j_cp=position
        i_cp+=1
        j_cp+=2
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('white', i_cp, j_cp)

            
        #left down
        i_cp,j_cp=position
        i_cp+=1
        j_cp-=2
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('white', i_cp, j_cp)
                    

            
        #left up
        i_cp,j_cp=position
        i_cp-=1
        j_cp-=2
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('white', i_cp, j_cp)



        #up right
        i_cp,j_cp=position
        i_cp-=2
        j_cp+=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('white', i_cp, j_cp)
                
        
        #up left
        i_cp,j_cp=position
        i_cp-=2
        j_cp-=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('white', i_cp, j_cp)

            
        #down  right
        i_cp,j_cp=position
        i_cp+=2
        j_cp+=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('white', i_cp, j_cp)
                    

        #down left 
        i_cp,j_cp=position
        i_cp+=2
        j_cp-=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('white', i_cp, j_cp)

#############################################################
    if figure=='P':
        
        #up left 
        i_cp,j_cp=position
        i_cp-=1
        j_cp-=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('white', i_cp, j_cp)

        #up right
        i_cp,j_cp=position
        i_cp-=1
        j_cp+=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('white', i_cp, j_cp)
#############################################################
    if figure=='R' or figure=='Q':
        #checking right
        i_cp,j_cp=position
        j_cp+=1
        while(j_cp<8):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                update('white', i_cp, j_cp)
                break
            else:
                update('white', i_cp, j_cp)
            j_cp+=1

        #checking left
        i_cp,j_cp=position
        j_cp-=1
        while(j_cp>-1):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                update('white', i_cp, j_cp)
                break
            else:
                update('white', i_cp, j_cp)
            j_cp-=1

        #checking up
        i_cp,j_cp=position
        i_cp-=1
        while(i_cp>-1):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                update('white', i_cp, j_cp)
                break
            else:
                update('white', i_cp, j_cp)
            i_cp-=1

        #checking down
        i_cp,j_cp=position
        i_cp+=1
        while(i_cp<8):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                update('white', i_cp, j_cp)
                break
            else:
                update('white', i_cp, j_cp)
            i_cp+=1



#############################################################
    if figure=='K':
        #up left 
        i_cp,j_cp=position
        i_cp-=1
        j_cp-=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('white', i_cp, j_cp)

        #up right
        i_cp,j_cp=position
        i_cp-=1
        j_cp+=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('white', i_cp, j_cp)

        #up 
        i_cp,j_cp=position
        i_cp-=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('white', i_cp, j_cp)

        #down
        i_cp,j_cp=position
        i_cp+=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('white', i_cp, j_cp)

        #right
        i_cp,j_cp=position
        j_cp+=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('white', i_cp, j_cp)

        #left 
        i_cp,j_cp=position
        j_cp-=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('white', i_cp, j_cp)


        #down left 
        i_cp,j_cp=position
        i_cp+=1
        j_cp-=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('white', i_cp, j_cp)

        #down right
        i_cp,j_cp=position
        i_cp+=1
        j_cp+=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('white', i_cp, j_cp)
    
#############################################################
    if figure=='b' or figure=='q':
        #checking down right diagonal
        i_cp,j_cp=position
        i_cp+=1
        j_cp+=1
        while(i_cp<8 and j_cp<8):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                update('black', i_cp, j_cp)
                break
            else:
                update('black', i_cp, j_cp)
                    
            i_cp+=1
            j_cp+=1
        
        #checking up left diagonal
        i_cp,j_cp=position
        i_cp-=1
        j_cp-=1
        while(i_cp>-1 and j_cp>-1):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                update('black', i_cp, j_cp)
                break
            else:
                update('black', i_cp, j_cp)
                    
            i_cp-=1
            j_cp-=1 
            
        #checking up right diagonal
        i_cp,j_cp=position
        i_cp-=1
        j_cp+=1
        while(i_cp>-1 and j_cp<8):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                update('black', i_cp, j_cp)
                break
            else:
                update('black', i_cp, j_cp)
                    
            i_cp-=1
            j_cp+=1
            
        #checking up right diagonal
        i_cp,j_cp=position
        i_cp+=1
        j_cp-=1
        while(i_cp<8 and j_cp>-1):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                update('black', i_cp, j_cp)
                break
            else:
                update('black', i_cp, j_cp)
                    
            i_cp+=1
            j_cp-=1
        
    if figure=='n':

        #right up
        i_cp,j_cp=position
        i_cp-=1
        j_cp+=2
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('black', i_cp, j_cp)
                    
        
        #right down
        i_cp,j_cp=position
        i_cp+=1
        j_cp+=2
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('black', i_cp, j_cp)

            
        #left down
        i_cp,j_cp=position
        i_cp+=1
        j_cp-=2
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('black', i_cp, j_cp)
                    

            
        #left up
        i_cp,j_cp=position
        i_cp-=1
        j_cp-=2
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('black', i_cp, j_cp)



        #up right
        i_cp,j_cp=position
        i_cp-=2
        j_cp+=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('black', i_cp, j_cp)
                
        
        #up left
        i_cp,j_cp=position
        i_cp-=2
        j_cp-=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('black', i_cp, j_cp)

            
        #down  right
        i_cp,j_cp=position
        i_cp+=2
        j_cp+=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('black', i_cp, j_cp)
                    

        #down left 
        i_cp,j_cp=position
        i_cp+=2
        j_cp-=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('black', i_cp, j_cp)

    if figure=='p':
        #down left 
        i_cp,j_cp=position
        i_cp+=1
        j_cp-=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('black', i_cp, j_cp)

        #down right
        i_cp,j_cp=position
        i_cp+=1
        j_cp+=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('black', i_cp, j_cp)
    if figure=='r' or figure=='q':
        #checking right
        i_cp,j_cp=position
        j_cp+=1
        while(j_cp<8):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                update('black', i_cp, j_cp)
                break
            else:
                update('black', i_cp, j_cp)
            j_cp+=1

        #checking left
        i_cp,j_cp=position
        j_cp-=1
        while(j_cp>-1):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                update('black', i_cp, j_cp)
                break
            else:
                update('black', i_cp, j_cp)
            j_cp-=1

        #checking up
        i_cp,j_cp=position
        i_cp-=1
        while(i_cp>-1):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                update('black', i_cp, j_cp)
                break
            else:
                update('black', i_cp, j_cp)
            i_cp-=1

        #checking down
        i_cp,j_cp=position
        i_cp+=1
        while(i_cp<8):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                update('black', i_cp, j_cp)
                break
            else:
                update('black', i_cp, j_cp)
            i_cp+=1

    if figure=='k':
        #up left 
        i_cp,j_cp=position
        i_cp-=1
        j_cp-=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('black', i_cp, j_cp)

        #up right
        i_cp,j_cp=position
        i_cp-=1
        j_cp+=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('black', i_cp, j_cp)

        #up 
        i_cp,j_cp=position
        i_cp-=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('black', i_cp, j_cp)

        #down
        i_cp,j_cp=position
        i_cp+=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('black', i_cp, j_cp)

        #right
        i_cp,j_cp=position
        j_cp+=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('black', i_cp, j_cp)

        #left 
        i_cp,j_cp=position
        j_cp-=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('black', i_cp, j_cp)


        #down left 
        i_cp,j_cp=position
        i_cp+=1
        j_cp-=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('black', i_cp, j_cp)

        #down right
        i_cp,j_cp=position
        i_cp+=1
        j_cp+=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
            update('black', i_cp, j_cp)
    
    
    
    return danger_matrix

mtx=[
['1', '1', '1', '1', '1', '1', '1', '1'],
['1', '1', '1', '1', '1', '1', '1', '1'],
['1', '1', '1', '1', '1', '1', '1', '1'],
['1', '1', '1', '1', '1', '1', '1', '1'],
['1', '1', '1', '1', '1', '1', '1', '1'],
['1', '1', '1', '1', '1', '1', '1', '1'],
['1', '1', '1', '1', '1', '1', '1', '1'],
['1', '1', '1', '1', '1', '1', '1', '1'],
]

danger_matrix=np.zeros((8,8))

# dng_mtx=update_danger_matrix('p', (1,2), mtx, dng_mtx)
# dng_mtx=update_danger_matrix('P', (5,6), mtx, dng_mtx)
# danger_matrix=update_danger_matrix('p', (6,2), mtx, danger_matrix)
# danger_matrix=update_danger_matrix('p', (5,3), mtx, danger_matrix)
danger_matrix=update_danger_matrix('k', (4,3), mtx, danger_matrix)
danger_matrix=update_danger_matrix('K', (5,4), mtx, danger_matrix)
# danger_matrix=update_danger_matrix('r', (4,3), mtx, danger_matrix)


for i in danger_matrix:
    print(i)