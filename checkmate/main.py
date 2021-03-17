import numpy as np
import os
import PIL
from PIL import Image
import sys
sys.stdout.reconfigure(encoding='utf-8')

def find_beggining(img):
    beggining_found=False
    beggining_position=None
    offset=None
    for row_px in range(img.shape[0]):
        for col_px in range(img.shape[1]):
            position_px_val=img[row_px,col_px,:]
            if np.array_equal(position_px_val,white_tile_px_val) and not beggining_found:
                beggining_position=np.array([row_px,col_px])
                beggining_found=True
            
            if np.array_equal(position_px_val,black_tile_px_val):
                offset=(np.array([row_px,col_px])-beggining_position)[1]
                break
        if beggining_found:
            break
    
    return beggining_position, offset

def cut_chessboard(img, begging_position, offset):
    return img[begging_position[0]:begging_position[0]+8*offset,
              begging_position[1]:begging_position[1]+8*offset,
              :]

def get_tiles(img, offset):
    
    crops=[]
    for i in range(0,offset*8, offset):
        for j in range(0,offset*8, offset):
            crop=img[i:i+offset,j:j+offset]
            crops.append(crop)
    return crops

def get_figure_array(img_pth):
    return np.asarray((Image.open(img_pth).convert('RGB').resize((30,30))))



def recognize_figure(tile):
    px_sum=np.sum(tile)
    figure_name=px_sum_to_figname[px_sum]
                
    return figure_name


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
                    can_move=False

                    #up left 
                    i_cp,j_cp=i,j
                    i_cp-=1
                    j_cp-=1
                    if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                        if danger_matrix[i_cp][j_cp]==0 or danger_matrix[i_cp][j_cp]==1:
                            can_move=True
                            return f"{check}\n{int(not can_move)}"

                    #up right
                    i_cp,j_cp=i,j
                    i_cp-=1
                    j_cp+=1
                    if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                        if danger_matrix[i_cp][j_cp]==0 or danger_matrix[i_cp][j_cp]==1:
                            can_move=True
                            return f"{check}\n{int(not can_move)}"


                    #up 
                    i_cp,j_cp=i,j
                    i_cp-=1
                    if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                        if danger_matrix[i_cp][j_cp]==0 or danger_matrix[i_cp][j_cp]==1:
                            can_move=True
                            return f"{check}\n{int(not can_move)}"
                    #down
                    i_cp,j_cp=i,j
                    i_cp+=1
                    if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                        if danger_matrix[i_cp][j_cp]==0 or danger_matrix[i_cp][j_cp]==1:
                            can_move=True
                            return f"{check}\n{int(not can_move)}"
                    #right
                    i_cp,j_cp=i,j
                    j_cp+=1
                    if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                        if danger_matrix[i_cp][j_cp]==0 or danger_matrix[i_cp][j_cp]==1:
                            can_move=True
                            return f"{check}\n{int(not can_move)}"
                    #left 
                    i_cp,j_cp=i,j
                    j_cp-=1
                    if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                        if danger_matrix[i_cp][j_cp]==0 or danger_matrix[i_cp][j_cp]==1:
                            can_move=True
                            return f"{check}\n{int(not can_move)}"

                    #down left 
                    i_cp,j_cp=i,j
                    i_cp+=1
                    j_cp-=1
                    if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                        if danger_matrix[i_cp][j_cp]==0 or danger_matrix[i_cp][j_cp]==1:
                            can_move=True
                            return f"{check}\n{int(not can_move)}"

                    #down right
                    i_cp,j_cp=i,j
                    i_cp+=1
                    j_cp+=1
                    if (i_cp<8 and j_cp<8 and i_cp>-1 and j_cp>-1):
                        if danger_matrix[i_cp][j_cp]==0 or danger_matrix[i_cp][j_cp]==1:
                            can_move=True
                            return f"{check}\n{int(not can_move)}"

                    return f"{check}\n{int(not can_move)}"

    return f"-\n0"

# mtx=[
# ['1', '1', '1', '1', '1', '1', '1', 'K'],
# ['1', '1', '1', '1', '1', '1', 'q', '1'],
# ['1', '1', '1', '1', '1', '1', '1', '1'],
# ['1', '1', '1', 'r', '1', '1', '1', '1'],
# ['1', '1', '1', '1', '1', '1', '1', '1'],
# ['1', '1', '1', '1', '1', '1', '1', '1'],
# ['1', '1', '1', '1', '1', '1', 'r', '1'],
# ['1', '1', '1', '1', '1', '1', '1', '1'],
# ]

# danger_matrix=get_danger_matrix(mtx)
# for i in danger_matrix:
#     print(i)

# print(is_someone_giving_check_or_checkmate(mtx, danger_matrix))




def solve(img):
    
    # task 1
    beggining_position, offset= find_beggining(img)
    print(','.join([str(x) for x in beggining_position]))
    
    # task 2
    chessboard=cut_chessboard(img, beggining_position, offset)
    tiles=get_tiles(chessboard, offset)
    
    chessboard_num=np.zeros((8,8))

    fen_notation=''
    blank_field_cum=0
    for idx,tile in enumerate(tiles):   
        figure_name=recognize_figure(tile)
        if figure_name in 'pnbrqkPNBRQK':
            if blank_field_cum>0:
                fen_notation+=str(blank_field_cum)
                blank_field_cum=0
            fen_notation+=figure_name
        else: 
            blank_field_cum+=1
            
        if (idx+1)%8==0:
            if blank_field_cum>0:
                fen_notation+=str(blank_field_cum)
                blank_field_cum=0
                
            # dont write last slash
            if (idx+1)%64!=0:
                fen_notation+='/'
                
    print(fen_notation)
    
    # task 3 and task 4
    
    figure_matrix=[
                    ['','','','','','','',''],
                    ['','','','','','','',''],
                    ['','','','','','','',''],
                    ['','','','','','','',''],
                    ['','','','','','','',''],
                    ['','','','','','','',''],
                    ['','','','','','','',''],
                    ['','','','','','','',''],
                ]
    # tells where figures can reach for an attack
    # 0 if cant reach, 1 if white can reach, 2 if black can reach, 3 if both can reach
    
    for idx,tile in enumerate(tiles):
        figure_name=recognize_figure(tile)
        pos_2d=((idx)//8, (idx)%8)
        figure_matrix[pos_2d[0]][pos_2d[1]]=figure_name
    
    danger_matrix=get_danger_matrix(figure_matrix)
    print(is_someone_giving_check_or_checkmate(figure_matrix, danger_matrix))
    
    
    # pprint
    # for i in range(8):
    #     print(figure_matrix[i])

    # print() 

    # for i in danger_matrix:
    #     print(i)


if __name__=="__main__":
    
    px_sum_to_figname={
        576000:'1',
        341724:'Q',
        376200:'1',
        314357:'k',
        518109:'K',
        386936:'K',
        384771:'n',
        261591:'n',
        445530:'k',
        555722:'P',
        405205:'P',
        433925:'p',
        283408:'p',
        512160:'R',
        537129:'N',
        365691:'B',
        512395:'B',
        466042:'Q',
        278589:'q',
        295386:'b',
        377478:'R',
        285648:'r',
        413949:'N',
        420330:'r',
        401317:'q',
        442090:'b'
    }

    chessboard_dim=8
    black_tile_px_val=[180, 136, 102]
    white_tile_px_val=[240, 217, 183]
    nothing_px_val=[0,0,0]

    for i in range(0,26,1):
        test_case=i
        data_pth=os.path.join('data/public/set/',str(test_case))
        img_pths={}
        img_pths['input']=os.path.join(data_pth,str(test_case)+'.png')
        for root, dirs, files in os.walk(data_pth, topdown=False):
            for name in files:
                if not name.split('.')[0].isnumeric():
                    desc=os.path.normpath(root).split(os.path.sep)[-1]
                    dict_key_name=desc+'_'+name.split('.')[0]
                    img_pths[dict_key_name]=os.path.join(root,name)


        img=np.asarray(Image.open(img_pths['input']))
        solve(img)
        
        print(open(os.path.join('data/public/outputs/',str(test_case)+'.txt')).read())

        print()
        print()
