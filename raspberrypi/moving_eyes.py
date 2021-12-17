from rgb_matrix.rgb_matrix import RGB_Matrix
import time

def up(list,step=1):
    for i in range(0,step):
        rr.draw_rectangle(list,fill=(251,248,40))
        list[1] -= 1
        list[3] -= 1
        rr.draw_rectangle(list,fill=(0,0,0))
        rr.display()

def down(list,step=1):
    for i in range(0,step):
        rr.draw_rectangle(list,fill=(251,248,40))
        list[1] += 1
        list[3] += 1
        rr.draw_rectangle(list,fill=(0,0,0))
        rr.display()

def left(list,step=1):
    for i in range(0,step):
        rr.draw_rectangle(list,fill=(251,248,40))
        list[0] -= 1
        list[2] -= 1
        rr.draw_rectangle(list,fill=(0,0,0))
        rr.display()

def right(list,step=1):
    for i in range(0,step):
        rr.draw_rectangle(list,fill=(251,248,40))
        list[0] += 1
        list[2] += 1
        rr.draw_rectangle(list,fill=(0,0,0))
        rr.display()

def left_down(list,step=1):
    for i in range(0,step):
        rr.draw_rectangle(list,fill=(251,248,40))
        list[0] -= 1
        list[2] -= 1
        list[1] += 1
        list[3] += 1
        rr.draw_rectangle(list,fill=(0,0,0))
        rr.display()

def left_up(list,step=1):
    for i in range(0,step):
        rr.draw_rectangle(list,fill=(251,248,40))
        list[0] -= 1
        list[2] -= 1
        list[1] -= 1
        list[3] -= 1
        rr.draw_rectangle(list,fill=(0,0,0))
        rr.display()

def right_up(list,step=1):
    for i in range(0,step):
        rr.draw_rectangle(list,fill=(251,248,40))
        list[0] += 1
        list[2] += 1
        list[1] -= 1
        list[3] -= 1
        rr.draw_rectangle(list,fill=(0,0,0))
        rr.display()

def right_down(list,step=1):
    for i in range(0,step):
        rr.draw_rectangle(list,fill=(251,248,40))
        list[0] += 1
        list[2] += 1
        list[1] += 1
        list[3] += 1
        rr.draw_rectangle(list,fill=(0,0,0))
        rr.display()

if __name__ == "__main__":
    rr = RGB_Matrix(0X74)

    rectangle_coor = [0,0,7,7]
    rr.draw_rectangle(rectangle_coor,fill=(251,248,40))

    point_arry = [[0,0],[1,0],[0,1],[6,0],[7,0],[7,1],[0,6],[0,7],[1,7],[7,6],[7,7],[6,7]]
    for i in range(len(point_arry)):
        rr.draw_point(point_arry[i],fill=(0,0,0))

    list = [3,3,4,4]
    rr.draw_rectangle(list,fill=(0,0,0),outline=None, width=0)

    rr.display()
    
    while True:
        up(list,3)
        down(list,6)
        up(list,6)
        down(list,6)
        up(list,3)
        time.sleep(1)
        right_down(list,2)
        up(list,4)
        left(list,4)
        down(list,4)
        right(list,4)
        left_up(list,2)
        time.sleep(1)
