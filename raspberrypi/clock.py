from rgb_matrix.rgb_matrix import RGB_Matrix
import time
import numpy as np


if __name__ == "__main__":
    rr = RGB_Matrix(0X74)
    i = 0
    rectangle_coor = [0,0,7,7]
    coor_1 = np.array((0,0))
    coor_2 = np.array((1,0))
    coor_3 = np.array((2,0))
    coor_4 = np.array((3,0))
    coor_5 = np.array((4,0))
    coor_6 = np.array((5,0))
    coor_list = [coor_1,coor_2,coor_3,coor_4,coor_5,coor_6]

    clock_list = [[3,1],[4,1],[5,2],[6,3],[6,4],[5,5],[4,6],[3,6],[2,5],[1,4],[1,3],[2,2]]
    while True:
        start = time.time()
        rr.draw_rectangle(rectangle_coor,fill=(0,0,0),outline=None, width=0)   #flash picture
        for i in clock_list:
            rr.draw_point(i,fill=(0,51,51))
        for i in coor_list:
            if i[0] < 7 and i[1]==0:
                i[0] = i[0] + 1
            elif  i[0] == 7 and i[1]<7: 
                i[1] = i[1] + 1  
            elif  i[0] >= 1 and i[1]==7: 
                i[0] = i[0] - 1 
            elif  i[0] == 0 and i[1]>0: 
                i[1] = i[1] - 1   
        
        coor_list_lenth = len(coor_list)
        for i in clock_list:
            rr.draw_point(i,fill=(0,51,51))

        for i in range(coor_list_lenth):
            rr.draw_point(list(coor_list[i]),fill=(int(240/(i+1)),0,0))


        rr.display()
        # 
        while True:
            during = time.time() - start
            if during >= 1/28.0:
                break
        # time.sleep(0.001)