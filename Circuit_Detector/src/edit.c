#include "Detect.h"

void BreakImg(unsigned char *src, int rows, int cols) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            src[i * cols + j] = (src[i * cols + j] < 128) ? 255 : 0;
        }
    }
}

void RemovePart(unsigned char *src, int rows, int cols, int x, int y, int w, int h) {
    for (int i = x; i <= x + w; ++i) {
        for (int j = y; j <= y + h; ++j) {
            src[i * cols + j] = 0;
        }
    }
}
