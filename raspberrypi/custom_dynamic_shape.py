from rgb_matrix.rgb_matrix import RGB_Matrix
import time


def pacman(a,k):
    
    list2 = [[a-4,0,a-1,0],
            [a-5,1,a,1],
            [a-6,2,a-5,2],
            [a-3,2,a-1,2],
            [a-6,3,a-2,3],
            [a-6,4,a-2,4],
            [a-6,5,a-1,5],
            [a-5,6,a,6],
            [a-4,7,a-1,7]]    
                    
    fill = (144,192,22)          
    for i in range(0,k+1):
        for j in list2:    
            rr.draw_line(j,fill)
            
        rr.display()

        for j in list2:    
            rr.draw_line(j,fill=(0,0,0))        
        
        for i in range(0,9):
            list2[i][0] += 1
            list2[i][2] += 1
                
        time.sleep(0.1)        

def pacman2():

    rr.draw_rectangle(rectangle_coor,fill=(0,0,0))
    
    list = [[2,0,5,0],
            [1,1,6,1],
            [0,2,1,2],
            [3,2,7,2],
            [0,3,7,3],
            [0,4,3,4],
            [0,5,7,5],
            [1,6,6,6],
            [2,7,5,7]]

    fill = (144,192,22)
    for i in list:        
        rr.draw_line(i,fill)
            
    rr.display()
    time.sleep(0.1)
        
    rr.draw_rectangle(rectangle_coor,fill=(0,0,0))

def pac():
    
    coor = [6,3,7,4]    
    rr.draw_rectangle(coor,fill=(82,52,25))

if __name__ == "__main__":
    rr = RGB_Matrix(0X74)

    rectangle_coor = [0,0,7,7]
    
    while True:
        pac()
        pacman(0,6)    
        pacman2()
        pacman(6,7)