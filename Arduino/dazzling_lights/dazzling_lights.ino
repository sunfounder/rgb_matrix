#include <rgbMatrix.h>


byte line[8][4] = {{0, 0, 0, 7},
  {1, 0, 1, 7},
  {2, 0, 2, 7},
  {3, 0, 3, 7},
  {4, 0, 4, 7},
  {5, 0, 5, 7},
  {6, 0, 6, 7},
  {7, 0, 7, 7}
};

byte color[7][3] = {{255, 0, 0},
  {255, 102, 0},
  {255, 255, 0},
  {0, 255, 0},
  {0, 128, 128},
  {0, 0, 255},
  {128, 0, 128}
};

int i = 0;
void dazzling_light() {
  for (int j = 0; j < 8; j++) {
    draw_line(line[j], color[i][0], color[i][1], color[i][2]);
    i++;
    if (i == 7) {
      i = 0;
    }
  }
  image();
  delay(200);
}

void dazzling_light2() {
  for (long firstPixelHue = 0; firstPixelHue < 65536; firstPixelHue += 500) {
    for (int j = 0; j < 8; j++) {
      long pixelHue = firstPixelHue + (j * 65536L / 16);
      draw_line(line[j], gamma32(ColorHSV(pixelHue)));
    }
    image();
  }
}


void setup() {
  // put your setup code here, to run once:
  RGBMatrixInit();
}

void loop() {
  for (int i = 0; i < 50; i++) {
    dazzling_light();
  }
  for (int i = 0; i < 5; i++) {
    dazzling_light2();
  }
}
