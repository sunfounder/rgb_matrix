# class RGB_Matrix - display by the RGB_Matrix

Usage:
```python
from sensor_hat import RGB_Matrix

rr = RGB_Matrix(0x74)                     # create an RGB_Matrix object 

text = 'hi sir'
rr.show_text(text, delay=0.1,color=(0,15,0))   # show text 

point_coor = [1,3]
rr.draw_point(point_coor,fill=(10,10,10))   #draw a point

line_coor = [0,0,4,0]
rr.draw_line(line_coor,fill=(0,0,0),width=0, joint=None)  # draw a line

rectangle_coor = [1,1,2,2]
rr.draw_rectangle(coor,fill=(10,0,0),outline=None, width=0)   #draw a rectangle
                    
ellipse_coor = [5,5]
radius = 2
rr.draw_ellipse(coor,radius,fill=(0,5,0),outline=None, width=0)   #draw a rectangle

rr.display()  #display the picture which you draw

```
## Constructors
```class sensor_hat.RGB_Matrix()```
Create an RGB Matrix screen object.This screen size is 8x8 and it has 64 RGB LEDs,set R.G.B corresponding PWM value to control each LED color,and then display various images.

## Methods
- show_text - show the text what you want to show
```python
RGB_Matrix().show_text('Hello', delay=0.1,color=(0,15,0))
```

- draw_point - draw a point
```python
RGB_Matrix().draw_point((0,0),fill=(10,10,10))
```

- draw_line - draw a line
```python
RGB_Matrix().draw_line((0,0,4,0),fill=(10,10,10))
```

- draw_rectangle - draw a rectangle
```python
RGB_Matrix().draw_rectangle((0,0,4,4),fill=(10,0,10))
```

- draw_ellipse - draw a ellipse
```python
RGB_Matrix().draw_ellipse((4,4),3,fill=(0,10,10))
```

- display - display the picture
```python
RGB_Matrix().display()
```