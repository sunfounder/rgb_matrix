from rgb_matrix.rgb_matrix import RGB_Matrix
import time


def pacman():

    rectangle_coor = [0,0,7,7]

    list = [[2,0,5,0],
            [1,1,6,1],
            [0,2,1,2],
            [3,2,5,2],
            [0,3,4,3],
            [0,4,4,4],
            [0,5,5,5],
            [1,6,6,6],
            [2,7,5,7]]
            
    fill = (144,192,22)
    for i in list:        
        rr.draw_line(i,fill)

    rr.display()
    time.sleep(1)

    rr.draw_rectangle(rectangle_coor,fill=(0,0,0))               

def pacman2():

    rectangle_coor = [0,0,7,7]

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
    time.sleep(1)
        
    rr.draw_rectangle(rectangle_coor,fill=(0,0,0))                        
        
if __name__ == "__main__":
    rr = RGB_Matrix(0X74)

    rectangle_coor = [0,0,7,7]
    
    while True:
        pacman()
        time.sleep(0.5)
        pacman2()
