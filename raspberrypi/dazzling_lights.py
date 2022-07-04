from rgb_matrix.rgb_matrix import RGB_Matrix

# source: https://github.com/adafruit/Adafruit_NeoPixel/blob/216ccdbff399750f5b02d4cc804c598399e39713/Adafruit_NeoPixel.cpp#L2414

def ColorHSV(hue):

    if hue < 510:  # Red to Green-1
        b = 0
        if hue < 255:  #   Red to Yellow-1
            r = 255
            g = hue  #     g = 0 to 254
        else:  #   Yellow to Green-1
            r = 510 - hue  #     r = 255 to 1
            g = 255

    elif hue < 1020:  # Green to Blue-1
        r = 0
        if hue < 765:  #   Green to Cyan-1
            g = 255
            b = hue - 510  #     b = 0 to 254
        else:  #   Cyan to Blue-1
            g = 1020 - hue  #     g = 255 to 1
            b = 255

    elif hue < 1530:  # Blue to Red-1
        g = 0
        if hue < 1275:  #   Blue to Magenta-1
            r = hue - 1020  #     r = 0 to 254
            b = 255
        else:  #   Magenta to Red-1
            r = 255
            b = 1530 - hue  #     b = 255 to 1

    else:  # Last 0.5 Red (quicker than % operator)
        r = 255
        g = b = 0

    list = [r, g, b]
    return list


def flash():
    list = [[0, 0, 0, 7], 
            [1, 0, 1, 7], 
            [2, 0, 2, 7], 
            [3, 0, 3, 7],
            [4, 0, 4, 7], 
            [5, 0, 5, 7], 
            [6, 0, 6, 7], 
            [7, 0, 7, 7]]

    firsthue = 0
    hue = 0
    while firsthue < 1530:
        j = 0
        for i in list:
            hue = firsthue + j * 95
            j = j + 1
            if hue > 1530:
                hue = hue - 1530
            temp = ColorHSV(hue)
            #print(temp[0],temp[1],temp[2])
            #time.sleep(2)
            rr.draw_line(i, (temp[0], temp[1], temp[2]))
        rr.display()
        firsthue = firsthue + 11


if __name__ == "__main__":
    rr = RGB_Matrix(0X74)

    while True:
        flash()
