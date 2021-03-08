#include <rgbMatrix.h>
void setup() {
  // put your setup code here, to run once:
    RGBMatrixInit();
}
void loop() {
   for(int i = 0;i < 19; i++)
   {
       DispShowPic(i,0,51,51);
       delay(1000);
    }
}
