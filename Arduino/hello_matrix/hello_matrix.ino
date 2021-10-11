#include <rgbMatrix.h>
byte dot[2] = {3, 1};
byte line[4] = {0, 3, 7, 3};
byte line2[4] = {1, 2, 6, 2};
byte rectangle[4] = {3, 5, 5, 7};
byte heart[] = {0x00, 0x66, 0xff, 0xff, 0x7e, 0x3c, 0x18, 0x00};

void setup() {
  // put your setup code here, to run once:
  RGBMatrixInit();
}

void loop() {

  draw_point(dot, 0, 255, 255);
  image();
  delay(3000);
  draw_line(line, 0, 255, 255);
  image();
  delay(3000);
  draw_rectangle(rectangle, 0, 255, 255);
  image();
  delay(3000);
  ShowHex(heart, 255, 0, 0);
  delay(3000);
  DispShowChar('A', 0, 0, 255);
  delay(3000);
  //Showtext("Hi!Sunfounder",0,0,255);
  flow_text("Hi!Sunfounder", 0, 0, 255);
  delay(6000);
}
