import numpy as np


def update_danger_matrix(color, i_cp, j_cp):

def update_danger_matrix(figure, position, figure_matrix, danger_matrix):
    i,j=position
    
#############################################################
    if figure=='P':
        #checking down right diagonal
        i_cp,j_cp=position
        i_cp+=1
        j_cp+=1
        while(i_cp<8 and j_cp<8):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                if danger_matrix[i_cp][j_cp]==2:
                    danger_matrix[i_cp][j_cp]=3
                else:
                    danger_matrix[i_cp][j_cp]=1
                break
            else:
                if danger_matrix[i_cp][j_cp]==2:
                    danger_matrix[i_cp][j_cp]=3
                else:
                    danger_matrix[i_cp][j_cp]=1
                    
            i_cp+=1
            j_cp+=1
        
        #checking up left diagonal
        i_cp,j_cp=position
        i_cp-=1
        j_cp-=1
        while(i_cp>-1 and j_cp>-1):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                if danger_matrix[i_cp][j_cp]==2:
                    danger_matrix[i_cp][j_cp]=3
                else:
                    danger_matrix[i_cp][j_cp]=1
                break
            else:
                if danger_matrix[i_cp][j_cp]==2:
                    danger_matrix[i_cp][j_cp]=3
                else:
                    danger_matrix[i_cp][j_cp]=1
                    
            i_cp-=1
            j_cp-=1 
            
        #checking up right diagonal
        i_cp,j_cp=position
        i_cp-=1
        j_cp+=1
        while(i_cp>-1 and j_cp<8):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                if danger_matrix[i_cp][j_cp]==2:
                    danger_matrix[i_cp][j_cp]=3
                else:
                    danger_matrix[i_cp][j_cp]=1
                break
            else:
                if danger_matrix[i_cp][j_cp]==2:
                    danger_matrix[i_cp][j_cp]=3
                else:
                    danger_matrix[i_cp][j_cp]=1
                    
            i_cp-=1
            j_cp+=1
            
        #checking up right diagonal
        i_cp,j_cp=position
        i_cp+=1
        j_cp-=1
        while(i_cp<8 and j_cp>-1):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                if danger_matrix[i_cp][j_cp]==2:
                    danger_matrix[i_cp][j_cp]=3
                else:
                    danger_matrix[i_cp][j_cp]=1
                break
            else:
                if danger_matrix[i_cp][j_cp]==2:
                    danger_matrix[i_cp][j_cp]=3
                else:
                    danger_matrix[i_cp][j_cp]=1
                    
            i_cp+=1
            j_cp-=1
#############################################################
    if figure=='N':

        #right up
        i_cp,j_cp=position
        i_cp-=1
        j_cp+=2
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):


            if danger_matrix[i_cp][j_cp]==2:
                danger_matrix[i_cp][j_cp]=3
            else:
                danger_matrix[i_cp][j_cp]=1
                    
        
        #right down
        i_cp,j_cp=position
        i_cp+=1
        j_cp+=2
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):


            if danger_matrix[i_cp][j_cp]==2:
                danger_matrix[i_cp][j_cp]=3
            else:
                danger_matrix[i_cp][j_cp]=1

            
        #left down
        i_cp,j_cp=position
        i_cp+=1
        j_cp-=2
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):


            if danger_matrix[i_cp][j_cp]==2:
                danger_matrix[i_cp][j_cp]=3
            else:
                danger_matrix[i_cp][j_cp]=1
                    

            
        #left up
        i_cp,j_cp=position
        i_cp-=1
        j_cp-=2
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):


            if danger_matrix[i_cp][j_cp]==2:
                danger_matrix[i_cp][j_cp]=3
            else:
                danger_matrix[i_cp][j_cp]=1



        #up right
        i_cp,j_cp=position
        i_cp-=2
        j_cp+=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):


            if danger_matrix[i_cp][j_cp]==2:
                danger_matrix[i_cp][j_cp]=3
            else:
                danger_matrix[i_cp][j_cp]=1
                
        
        #up left
        i_cp,j_cp=position
        i_cp-=2
        j_cp-=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):


            if danger_matrix[i_cp][j_cp]==2:
                danger_matrix[i_cp][j_cp]=3
            else:
                danger_matrix[i_cp][j_cp]=1

            
        #down  right
        i_cp,j_cp=position
        i_cp+=2
        j_cp+=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):


            if danger_matrix[i_cp][j_cp]==2:
                danger_matrix[i_cp][j_cp]=3
            else:
                danger_matrix[i_cp][j_cp]=1
                    

        #down left 
        i_cp,j_cp=position
        i_cp+=2
        j_cp-=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):


            if danger_matrix[i_cp][j_cp]==2:
                danger_matrix[i_cp][j_cp]=3
            else:
                danger_matrix[i_cp][j_cp]=1

    if figure=='B':
        pass
    if figure=='R':
        pass
    if figure=='Q':
        pass
    if figure=='K':
        pass
    
    if figure=='p':
        #checking down right diagonal
        i_cp,j_cp=position
        i_cp+=1
        j_cp+=1
        while(i_cp<8 and j_cp<8):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                if danger_matrix[i_cp][j_cp]==1:
                    danger_matrix[i_cp][j_cp]=3
                else:
                    danger_matrix[i_cp][j_cp]=2
                break
            else:
                if danger_matrix[i_cp][j_cp]==1:
                    danger_matrix[i_cp][j_cp]=3
                else:
                    danger_matrix[i_cp][j_cp]=2
                    
            i_cp+=1
            j_cp+=1
        
        #checking up left diagonal
        i_cp,j_cp=position
        i_cp-=1
        j_cp-=1
        while(i_cp>-1 and j_cp>-1):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                if danger_matrix[i_cp][j_cp]==1:
                    danger_matrix[i_cp][j_cp]=3
                else:
                    danger_matrix[i_cp][j_cp]=2
                break
            else:
                if danger_matrix[i_cp][j_cp]==1:
                    danger_matrix[i_cp][j_cp]=3
                else:
                    danger_matrix[i_cp][j_cp]=2
                    
            i_cp-=1
            j_cp-=1 
            
        #checking up right diagonal
        i_cp,j_cp=position
        i_cp-=1
        j_cp+=1
        while(i_cp>-1 and j_cp<8):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                if danger_matrix[i_cp][j_cp]==1:
                    danger_matrix[i_cp][j_cp]=3
                else:
                    danger_matrix[i_cp][j_cp]=2
                break
            else:
                if danger_matrix[i_cp][j_cp]==1:
                    danger_matrix[i_cp][j_cp]=3
                else:
                    danger_matrix[i_cp][j_cp]=2
                    
            i_cp-=1
            j_cp+=1
            
        #checking up right diagonal
        i_cp,j_cp=position
        i_cp+=1
        j_cp-=1
        while(i_cp<8 and j_cp>-1):

            if figure_matrix[i_cp][j_cp] in 'pnbrqkPNBRQK':
                if danger_matrix[i_cp][j_cp]==1:
                    danger_matrix[i_cp][j_cp]=3
                else:
                    danger_matrix[i_cp][j_cp]=2
                break
            else:
                if danger_matrix[i_cp][j_cp]==1:
                    danger_matrix[i_cp][j_cp]=3
                else:
                    danger_matrix[i_cp][j_cp]=2
                    
            i_cp+=1
            j_cp-=1
        
    if figure=='n':

        #right up
        i_cp,j_cp=position
        i_cp-=1
        j_cp+=2
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):


            if danger_matrix[i_cp][j_cp]==1:
                danger_matrix[i_cp][j_cp]=3
            else:
                danger_matrix[i_cp][j_cp]=2
                    
        
        #right down
        i_cp,j_cp=position
        i_cp+=1
        j_cp+=2
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):


            if danger_matrix[i_cp][j_cp]==1:
                danger_matrix[i_cp][j_cp]=3
            else:
                danger_matrix[i_cp][j_cp]=2

            
        #left down
        i_cp,j_cp=position
        i_cp+=1
        j_cp-=2
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):


            if danger_matrix[i_cp][j_cp]==1:
                danger_matrix[i_cp][j_cp]=3
            else:
                danger_matrix[i_cp][j_cp]=2
                    

            
        #left up
        i_cp,j_cp=position
        i_cp-=1
        j_cp-=2
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):


            if danger_matrix[i_cp][j_cp]==1:
                danger_matrix[i_cp][j_cp]=3
            else:
                danger_matrix[i_cp][j_cp]=2



        #up right
        i_cp,j_cp=position
        i_cp-=2
        j_cp+=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):


            if danger_matrix[i_cp][j_cp]==1:
                danger_matrix[i_cp][j_cp]=3
            else:
                danger_matrix[i_cp][j_cp]=2
                
        
        #up left
        i_cp,j_cp=position
        i_cp-=2
        j_cp-=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):


            if danger_matrix[i_cp][j_cp]==1:
                danger_matrix[i_cp][j_cp]=3
            else:
                danger_matrix[i_cp][j_cp]=2

            
        #down  right
        i_cp,j_cp=position
        i_cp+=2
        j_cp+=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):


            if danger_matrix[i_cp][j_cp]==1:
                danger_matrix[i_cp][j_cp]=3
            else:
                danger_matrix[i_cp][j_cp]=2
                    

        #down left 
        i_cp,j_cp=position
        i_cp+=2
        j_cp-=1
        if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):


            if danger_matrix[i_cp][j_cp]==1:
                danger_matrix[i_cp][j_cp]=3
            else:
                danger_matrix[i_cp][j_cp]=2

#     if figure=='b':
#         pass
#     if figure=='r':
#         pass
#     if figure=='q':
#         pass
#     if figure=='k':
#         pass
    
    
    
    return danger_matrix

mtx=[
['1', '1', '1', '1', '1', '1', '1', 'k'],
['1', '1', '1', '1', '1', '1', '1', '1'],
['1', '1', '1', '1', '1', '1', 'K', '1'],
['1', '1', '1', '1', '1', '1', '1', '1'],
['1', '1', '1', '1', '1', '1', '1', '1'],
['1', '1', '1', '1', '1', '1', '1', '1'],
['1', '1', '1', '1', '1', '1', '1', '1'],
['1', '1', '1', '1', '1', '1', '1', '1'],
]

dng_mtx=np.zeros((8,8))

# dng_mtx=update_danger_matrix('p', (1,2), mtx, dng_mtx)
# dng_mtx=update_danger_matrix('P', (5,6), mtx, dng_mtx)
dng_mtx=update_danger_matrix('N', (5,6), mtx, dng_mtx)
dng_mtx=update_danger_matrix('n', (5,2), mtx, dng_mtx)


for i in dng_mtx:
    print(i)