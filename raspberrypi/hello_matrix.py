from rgb_matrix import RGB_Matrix
from color import Color
import time

rr = RGB_Matrix(0x74)                     # create an RGB_Matrix object 
col = Color()

point_coor = [3,1]
rr.draw_point(point_coor,fill=(10,10,10))   #draw a point
rr.display()
time.sleep(3)

line_coor = [0,2,7,2]
rr.draw_line(line_coor,fill=(10,0,0))  # draw a line
rr.display()
time.sleep(3)

rectangle_coor = [0,4,2,6]
rr.draw_rectangle(rectangle_coor,fill=(10,0,0))   #draw a rectangle
rr.display()
time.sleep(3)

ellipse_coor = [5,5]
radius = 2
rr.draw_ellipse(ellipse_coor,radius,fill=(0,5,0))   #draw a ellipse
rr.display()  #display the picture which you draw
time.sleep(3)

text = 'hi sir'
rr.show_text(text, delay=200,color=(0,15,0))   # show text 
rr.display()
time.sleep(4)