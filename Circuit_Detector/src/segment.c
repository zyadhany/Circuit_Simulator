#include "Detect.h"


int* CompSize(unsigned char *img, int rows, int cols, int x, int y, int w, int h) {
    int w1 = 2400, w2 = -1, h1 = 2400, h2 = -1;

    for (int i = x; i < x + w; ++i) {
        for (int j = y; j < y + h; ++j) {
            if (img[i * cols + j]) {
                w1 = MIN(w1, j);
                w2 = MAX(w2, j);
                h1 = MIN(h1, i);
                h2 = MAX(h2, i);
            }
        }
    }

    int* result = (int*)malloc(4 * sizeof(int));

    result[1] = w1;
    result[0] = h1;
    result[3] = w2 - w1;
    result[2] = h2 - h1;

    return (result);
}

