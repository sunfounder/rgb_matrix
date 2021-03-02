# sled1734 func

## example
```c
#include <rgbtest.h>


void setup() {
  // put your setup code here, to run once:
    RGBMatrixInit();
}

void loop() {
    for(int i = 0;i < 19; i++){
        DispShowPic(i,0,51,51);
        delay(1000);
}
```

## Methods
- RGBMatrixInit() - Init the RGB Module.
```c
RGBMatrixInit()
```

- DispShowColor(byte R , byte G , byte B) - show one color on the screen.
```c
 DispShowColor(255,255,255)
```

- DispShowPic (byte Index , byte R , byte G , byte B) - show one picture on the screen.
```c
 DispShowPic(0,0,50,50);
```

