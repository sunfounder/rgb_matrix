#include <rgbMatrix.h>

byte eye[] = {3, 3, 4, 4};
byte rectangle_arry[] = {0, 0, 7, 7};
byte point_arry[][2] = {{0, 0}, {1, 0}, {0, 1}, {6, 0}, {7, 0}, {7, 1},
  {0, 6}, {0, 7}, {1, 7}, {7, 6}, {7, 7}, {6, 7}
};

void up(byte eye[4], int count = 1) {
  for (int i = 0; i < count; i++) {
    draw_rectangle(eye, 251, 248, 40);
    eye[1] -= 1;
    eye[3] -= 1;
    draw_rectangle(eye, 0, 0, 0);
    for (int i = 0; i < sizeof(point_arry); i++) {
      draw_point(point_arry[i], 0, 0, 0);
    }
    image();
    delay(30);
  }
}
void down(byte eye[4], int count = 1) {
  for (int i = 0; i < count; i++) {
    draw_rectangle(eye, 251, 248, 40);
    eye[1] += 1;
    eye[3] += 1;
    draw_rectangle(eye, 0, 0, 0);
    for (int i = 0; i < sizeof(point_arry); i++) {
      draw_point(point_arry[i], 0, 0, 0);
    }
    image();
    delay(30);
  }
}
void left(byte eye[4], int count = 1) {
  for (int i = 0; i < count; i++) {
    draw_rectangle(eye, 251, 248, 40);
    eye[0] -= 1;
    eye[2] -= 1;
    draw_rectangle(eye, 0, 0, 0);
    for (int i = 0; i < sizeof(point_arry); i++) {
      draw_point(point_arry[i], 0, 0, 0);
    }
    image();
    delay(30);
  }
}
void right(byte eye[4], int count = 1) {
  for (int i = 0; i < count; i++) {
    draw_rectangle(eye, 251, 248, 40);
    eye[0] += 1;
    eye[2] += 1;
    draw_rectangle(eye, 0, 0, 0);
    for (int i = 0; i < sizeof(point_arry); i++) {
      draw_point(point_arry[i], 0, 0, 0);
    }
    image();
    delay(30);
  }
}
void left_down(byte eye[4], int count = 1) {
  for (int i = 0; i < count; i++) {
    draw_rectangle(eye, 251, 248, 40);
    eye[0] -= 1;
    eye[2] -= 1;
    eye[1] += 1;
    eye[3] += 1;
    draw_rectangle(eye, 0, 0, 0);
    for (int i = 0; i < sizeof(point_arry); i++) {
      draw_point(point_arry[i], 0, 0, 0);
    }
    image();
    delay(30);
  }
}
void left_up(byte eye[4], int count = 1) {
  for (int i = 0; i < count; i++) {
    draw_rectangle(eye, 251, 248, 40);
    eye[0] -= 1;
    eye[2] -= 1;
    eye[1] -= 1;
    eye[3] -= 1;
    draw_rectangle(eye, 0, 0, 0);
    for (int i = 0; i < sizeof(point_arry); i++) {
      draw_point(point_arry[i], 0, 0, 0);
    }
    image();
    delay(30);
  }
}
void right_up(byte eye[4], int count = 1) {
  for (int i = 0; i < count; i++) {
    draw_rectangle(eye, 251, 248, 40);
    eye[0] += 1;
    eye[2] += 1;
    eye[1] -= 1;
    eye[3] -= 1;
    draw_rectangle(eye, 0, 0, 0);
    for (int i = 0; i < sizeof(point_arry); i++) {
      draw_point(point_arry[i], 0, 0, 0);
    }
    image();
    delay(30);
  }
}
void right_down(byte eye[4], int count = 1) {
  for (int i = 0; i < count; i++) {
    draw_rectangle(eye, 251, 248, 40);
    eye[0] += 1;
    eye[2] += 1;
    eye[1] += 1;
    eye[3] += 1;
    draw_rectangle(eye, 0, 0, 0);
    //image();
    for (int i = 0; i < sizeof(point_arry); i++) {
      draw_point(point_arry[i], 0, 0, 0);
    }
    image();
    delay(30);
  }
}
void setup() {
  // put your setup code here, to run once:
  RGBMatrixInit();
  draw_rectangle(rectangle_arry, 251, 248, 40);
  for (int i = 0; i < sizeof(point_arry); i++) {
    draw_point(point_arry[i], 0, 0, 0);
  }
  draw_rectangle(eye, 0, 0, 0);
  image();
}

void loop() {
  // put your main code here, to run repeatedly:
  up(eye, 3);
  delay(100);
  down(eye, 6);
  delay(100);
  up(eye, 6);
  delay(100);
  down(eye, 6);
  delay(100);
  up(eye, 3);
  delay(1000);
  right_down(eye, 3);
  delay(100);
  up(eye, 4);
  delay(100);
  left(eye, 4);
  delay(100);
  down(eye, 4);
  delay(100);
  right(eye, 4);
  delay(100);
  left_up(eye, 2);
  delay(1000);
}
