#include <rgbMatrix.h>

byte rectangle_coor[] = {0, 0, 7, 7};

byte green[][2] = {{2, 1}, {3, 1}, {5, 1},
  {1, 2}, {2, 2}, {4, 2}, {5, 2}, {6, 2},
  {1, 3}, {2, 3}, {3, 3}, {4, 3}, {6, 3},
  {2, 4}, {4, 4}, {5, 4},
  {1, 5}, {3, 5}, {5, 5}, {6, 5},
  {1, 6}, {2, 6}, {5, 6}, {6, 6}
};

byte flash[][2] = {{4, 1}, {3, 2}, {5, 3}, {3, 4}, {2, 5}, {4, 5}};
byte red[][2] = {{0, 3}, {7, 3}, {0, 6}, {7, 6}};
byte yellow[][2] = {{3, 0}, {4, 0}, {3, 6}, {4, 6}, {3, 7}, {4, 7}};
byte color[7][3] = {{255, 0, 0},
  {255, 102, 0},
  {255, 255, 0},
  {0, 255, 0},
  {0, 128, 128},
  {0, 0, 255},
  {128, 0, 128}
};

void tree() {
  int lenTotal_green = sizeof(green) / sizeof(byte);
  int lenLow_green = sizeof(green[0]) / sizeof(byte);
  int lenHigh_green = lenTotal_green / lenLow_green;
  for (int i = 0; i < lenHigh_green; i++) {
    draw_point(green[i], 0, 255, 0);
  }
  image();
  int lenTotal_yellow = sizeof(yellow) / sizeof(byte);
  int lenLow_yellow = sizeof(yellow[0]) / sizeof(byte);
  int lenHigh_yellow = lenTotal_yellow / lenLow_yellow;
  for (int i = 0; i < lenHigh_yellow; i++) {
    draw_point(yellow[i], 255, 255, 0);
  }
  image();
  int lenTotal_red = sizeof(red) / sizeof(byte);
  int lenLow_red = sizeof(red[0]) / sizeof(byte);
  int lenHigh_red = lenTotal_red / lenLow_red;
  for (int i = 0; i < lenHigh_red; i++) {
    draw_point(red[i], 255, 0, 0);
  }
  image();
}

int i = 0;
void dot() {
  int lenTotal_flash = sizeof(flash) / sizeof(byte);
  int lenLow_flash = sizeof(flash[0]) / sizeof(byte);
  int lenHigh_flash = lenTotal_flash / lenLow_flash;
  //for (int i=0; i<lenHigh_flash; i++){
  //  draw_point(flash[i],100,100,100);
  //}
  //image();
  for (int j = 0; j < lenHigh_flash; j++) {
    draw_point(flash[j], color[i][0], color[i][1], color[i][2]);
    i++;
    if (i == 7) {
      i = 0;
    }
  }
  image();
  delay(200);
}

void setup() {
  // put your setup code here, to run once:
  RGBMatrixInit();
  draw_rectangle(rectangle_coor, 0, 0, 0);
  tree();
}

void loop() {
  // put your main code here, to run repeatedly:
  dot();
}
