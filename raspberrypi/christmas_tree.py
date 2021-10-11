from rgb_matrix import RGB_Matrix
import time
from color import Color

def tree():
    
    for i in green_coor:        
        rr.draw_point(i,(0,255,0))
        
    for i in yellow_coor:
        rr.draw_point(i,(255,255,0))    
    
    for i in red_coor:        
        rr.draw_point(i,(255,0,0))
        
    rr.display()

    
def dot():
    col = Color()

    for i in flash_coor:
        rr.draw_point(i,col.random())
    rr.display()
    
    
if __name__ == "__main__":
    rr = RGB_Matrix(0X74)

    rectangle_coor = [0,0,7,7]

    green_coor = [[3,0],[4,0],
                [2,1],[3,1],[5,1],
                [1,2],[2,2],[4,2],[5,2],[6,2],
                [1,3],[2,3],[3,3],[4,3],[6,3],
                [2,4],[4,4],[5,4],
                [1,5],[3,5],[5,5],[6,5],
                [1,6],[2,6],[3,6],[4,6],[5,6],[6,6]
                ]    

    flash_coor = [[4,1],[3,2],[5,3],[3,4],[2,5],[4,5]]
    red_coor = [[0,3],[7,3],[0,6],[7,6]]
    yellow_coor = [[3,0],[4,0],[3,6],[4,6],[3,7],[4,7]]    

    tree()
    while True:        
        dot()    