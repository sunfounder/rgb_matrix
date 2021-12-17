import sys
import tty
import termios
from rgb_matrix.rgb_matrix import RGB_Matrix
import numpy as np
import time 
import threading
import random



key = 'n'
def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def Keyboard_control():
    while True:
        
        global power_val,key
        # key = 'n'
        key=readchar()
        time.sleep(0.22)
        if key=='q':
            print("quit")  
            break  

def snake_game():
    global key
    rr = RGB_Matrix(0X74)
    rectangle_coor = [0,0,7,7]
    rr.draw_rectangle(rectangle_coor,fill=(51,51,0))   #draw a rectangle
    coor_1 = np.asarray([0,2])
    coor_2 = np.asarray([1,2])
    coor_3 = np.asarray([2,2])
    coor_4 = np.asarray([3,2])
    coor_list = [coor_1,coor_2,coor_3,coor_4]
 

    eat_flag = False
    b =  random.randint(1,255)
    g =  random.randint(1,255)
    r =  random.randint(1,255)
    random_coor = [4,4]
    game_time = 20            #second
    game_count = 0
    while True:
        if game_count < 50:   
            rr.draw_rectangle(rectangle_coor,fill=(0,51,51))   #draw a rectangle
        else:
            rr.draw_rectangle(rectangle_coor,fill=(0,0,51))   #draw a rectangle   
        if eat_flag == False:
            random_x_list = [i for i in range(8)]
            random_x_list.remove(coor_list[0][0])
            random_y_list = [i for i in range(8)]
            random_y_list.remove(coor_list[0][1])
            random_coor[0] = random.choice(random_x_list)
            random_coor[1] = random.choice(random_y_list)       
            eat_flag = True

        rr.draw_point((random_coor[0],random_coor[1]),fill=(0,255,0))
        game_count +=1
        
        if key == 'a':
            key = 'n'
            if coor_list[0][0] == coor_list[1][0]:
                if coor_list[0][1] > coor_list[1][1]:
                    for i in range(len(coor_list)-1,0,-1):
                        coor_list[i][1] = coor_list[i-1][1] 
                        coor_list[i][0] = coor_list[i-1][0]
                    coor_list[0][0] += 1
                    if coor_list[0][0] > 7:
                        coor_list[0][0] = 0
                else:
                    for i in range(len(coor_list)-1,0,-1):
                        coor_list[i][1] = coor_list[i-1][1] 
                        coor_list[i][0] = coor_list[i-1][0]
                    coor_list[0][0] -= 1
                    if coor_list[0][0] < 0:
                        coor_list[0][0] = 7

            elif coor_list[0][1] == coor_list[1][1]:
                if coor_list[0][0] > coor_list[1][0]:
                    for i in range(len(coor_list)-1,0,-1):
                        coor_list[i][1] = coor_list[i-1][1] 
                        coor_list[i][0] = coor_list[i-1][0]
                    coor_list[0][1] -= 1
                    if coor_list[0][1] < 0:
                        coor_list[0][1] = 7
                else:
                    for i in range(len(coor_list)-1,0,-1):
                        coor_list[i][1] = coor_list[i-1][1] 
                        coor_list[i][0] = coor_list[i-1][0]
                    coor_list[0][1] += 1
                    if coor_list[0][1] > 7:
                        coor_list[0][1] = 0

        elif key == 'd':
            key = 'n'
            if coor_list[0][0] == coor_list[1][0]:
                if coor_list[0][1] > coor_list[1][1]:
                    for i in range(len(coor_list)-1,0,-1):
                        coor_list[i][1] = coor_list[i-1][1] 
                        coor_list[i][0] = coor_list[i-1][0]
                    coor_list[0][0] -= 1
                    if coor_list[0][0] < 0:
                        coor_list[0][0] = 7
                else:
                    for i in range(len(coor_list)-1,0,-1):
                        coor_list[i][1] = coor_list[i-1][1] 
                        coor_list[i][0] = coor_list[i-1][0]
                    coor_list[0][0] += 1
                    if coor_list[0][0] > 7:
                        coor_list[0][0] = 0

            elif coor_list[0][1] == coor_list[1][1]:
                if coor_list[0][0] > coor_list[1][0]:
                    for i in range(len(coor_list)-1,0,-1):
                        coor_list[i][1] = coor_list[i-1][1] 
                        coor_list[i][0] = coor_list[i-1][0] 
                    coor_list[0][1] += 1
                    if coor_list[0][1] > 7:
                        coor_list[0][1] = 0
                else:
                    for i in range(len(coor_list)-1,0,-1):
                        coor_list[i][1] = coor_list[i-1][1] 
                        coor_list[i][0] = coor_list[i-1][0]  
                    coor_list[0][1] -= 1
                    if coor_list[0][1] < 0:
                        coor_list[0][1] = 7

        elif key == 'q':
            break

        else:
            if coor_list[0][0] == coor_list[1][0]:
    
                if coor_list[0][1] - coor_list[1][1] == 1:
                    for i in range(len(coor_list)-1,0,-1):
                        coor_list[i][1] = coor_list[i-1][1] 
                        coor_list[i][0] = coor_list[i-1][0]
                    coor_list[0][1] +=1
                    if coor_list[0][1] > 7:
                        coor_list[0][1] = 0
                elif coor_list[0][1] - coor_list[1][1] == -1:
                    for i in range(len(coor_list)-1,0,-1):
                        coor_list[i][1] = coor_list[i-1][1] 
                        coor_list[i][0] = coor_list[i-1][0]
                    coor_list[0][1] -=1
                    if coor_list[0][1] < 0:
                        coor_list[0][1] = 7
                
                elif coor_list[0][1] - coor_list[1][1] > 1:
                    for i in range(len(coor_list)-1,0,-1):
                        coor_list[i][1] = coor_list[i-1][1] 
                        coor_list[i][0] = coor_list[i-1][0]
                    coor_list[0][1] -=1
                    if coor_list[0][1] < 0:
                        coor_list[0][1] = 7

                elif coor_list[0][1] - coor_list[1][1] < -1:
                    for i in range(len(coor_list)-1,0,-1):
                        coor_list[i][1] = coor_list[i-1][1] 
                        coor_list[i][0] = coor_list[i-1][0]
                    coor_list[0][1] +=1
                    if coor_list[0][1] > 7:
                        coor_list[0][1] = 0
                # break
            if coor_list[0][1] == coor_list[1][1]:

                if coor_list[0][0] - coor_list[1][0] == 1:
                    for i in range(len(coor_list)-1,0,-1):
                        coor_list[i][1] = coor_list[i-1][1] 
                        coor_list[i][0] = coor_list[i-1][0]
                    coor_list[0][0] +=1
                    if coor_list[0][0] > 7:
                        coor_list[0][0] = 0
                elif coor_list[0][0] - coor_list[1][0] == -1:
                    for i in range(len(coor_list)-1,0,-1):
                        coor_list[i][1] = coor_list[i-1][1] 
                        coor_list[i][0] = coor_list[i-1][0]
                    coor_list[0][0] -=1
                    if coor_list[0][0] < 0:
                        coor_list[0][0] = 7
                
                elif coor_list[0][0] - coor_list[1][0] > 1:
                    for i in range(len(coor_list)-1,0,-1):
                        coor_list[i][1] = coor_list[i-1][1] 
                        coor_list[i][0] = coor_list[i-1][0]
                    coor_list[0][0] -=1
                    if coor_list[0][0] < 0:
                        coor_list[0][0] = 7

                elif coor_list[0][0] - coor_list[1][0] < -1:
                    for i in range(len(coor_list)-1,0,-1):
                        coor_list[i][1] = coor_list[i-1][1] 
                        coor_list[i][0] = coor_list[i-1][0]
                    coor_list[0][0] +=1
                    if coor_list[0][0] > 7:
                        coor_list[0][0] = 0


        if coor_list[0][0] == random_coor[0] and coor_list[0][1] == random_coor[1]:
            eat_flag =False
            if coor_list[-1][0] == coor_list[-2][0]:
                if coor_list[-1][1] > coor_list[-2][1]:
                    new_x = coor_list[-1][0]
                    new_y = coor_list[-1][1] + 1
                    if new_y > 7:
                        new_y = 0
                elif coor_list[-1][1] < coor_list[-2][1]:
                    new_x = coor_list[-1][0]
                    new_y = coor_list[-1][1] - 1
                    if new_y < 0:
                        new_y = 7
                coor_list.append([new_x,new_y])

            elif coor_list[-1][1] == coor_list[-2][1]:
                if coor_list[-1][0] > coor_list[-2][0]:
                    new_x = coor_list[-1][0] + 1
                    new_y = coor_list[-1][1]
                    if new_x > 7:
                        new_x = 0
                elif coor_list[-1][0] < coor_list[-2][0]:
                    new_x = coor_list[-1][0] - 1
                    new_y = coor_list[-1][1]
                    if new_x < 0:
                        new_x = 7
                coor_list.append([new_x,new_y])  

        for i in range(len(coor_list)-1,0,-1):
            if (coor_list[0]  == coor_list[i]).all():
                coor_list = [coor_1,coor_2,coor_3,coor_4]
                break
        coor_list_lenth = len(coor_list)
        for i in range(coor_list_lenth):
            rr.draw_point(tuple(coor_list[i]),fill=(int(240/(i+1)),0,0))

        if game_count >= game_time*5:
            rr.draw_rectangle(rectangle_coor,fill=(51,51,51),outline=None, width=0) 
            for i in range(2):
                rr.show_text("Score: %s"%(len(coor_list)-4),100,(51,51,51))
                time.sleep(0.5)
            game_count = 0
            coor_list = [coor_1,coor_2,coor_3,coor_4]

        rr.display()
        time.sleep(0.2)


if __name__ == "__main__":
    t1 = threading.Thread(target=Keyboard_control)
    t2 = threading.Thread(target=snake_game)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    while True:
        pass


