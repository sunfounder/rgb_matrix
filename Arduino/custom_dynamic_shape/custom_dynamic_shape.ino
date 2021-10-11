#include <rgbMatrix.h>

byte pacman[] = {0x3c, 0x7e, 0xdc, 0xf8, 0xf8, 0xfc, 0x7e, 0x3c};
byte pacman2[] = {0x3c, 0x7e, 0xdf, 0xff, 0xf8, 0xff, 0x7e, 0x3c};
byte rotate[] = {0x3c, 0x7e, 0xde, 0xff, 0xc0, 0xff, 0x7e, 0x3c};
byte normal[] = {0x3c, 0x7e, 0xbd, 0xff, 0x81, 0xff, 0x7e, 0x3c};
byte smile[] = {0x3c, 0x7e, 0xbd, 0xff, 0x81, 0xe7, 0x7e, 0x3c};
byte smile2[] = {0x3c, 0x7e, 0xbd, 0xff, 0x81, 0xc3, 0x66, 0x3c};

void moving_pacman() {
  for (int i = -7; i < 2; i++) {
    ShowHex(pacman, 255, 255, 0, i);
    delay(200);
    i++;
    ShowHex(pacman2, 255, 255, 0, i);
    delay(200);
  }
  ShowHex(pacman2, 255, 255, 0, 1);
  delay(800);
}

void smile_man() {
  ShowHex(normal, 255, 255, 0);
  delay(100);
  for (int i = 0; i < 4; i++) {
    ShowHex(smile, 255, 255, 0);
    delay(200);
    ShowHex(smile2, 255, 255, 0);
    delay(200);
  }
  ShowHex(smile, 255, 255, 0);
  delay(100);
  ShowHex(normal, 255, 255, 0);
  delay(200);
}

void moving_pacman2() {
  for (int i = 1; i < 8; i++) {
    ShowHex(pacman, 255, 255, 0, i);
    delay(100);
    i++;
    ShowHex(pacman2, 255, 255, 0, i);
    delay(100);
  }
}

void setup() {
  // put your setup code here, to run once:
  RGBMatrixInit();
}

void loop() {
  // put your main code here, to run repeatedly:
  moving_pacman();
  ShowHex(rotate, 255, 255, 0);
  delay(100);
  smile_man();
  ShowHex(rotate, 255, 255, 0);
  delay(100);
  moving_pacman2();
}
