#include <rgbMatrix.h>

byte pacman[] = {0x3c, 0x7e, 0xdc, 0xf8, 0xf8, 0xfc, 0x7e, 0x3c};
byte pacman2[] = {0x3c, 0x7e, 0xdf, 0xff, 0xf8, 0xff, 0x7e, 0x3c};

void setup() {
  // put your setup code here, to run once:
  RGBMatrixInit();
}

void loop() {
  // put your main code here, to run repeatedly:
  ShowHex(pacman, 255, 255, 0);
  delay(1000);
  ShowHex(pacman2, 255, 255, 0, 1);
  delay(1000);
}
