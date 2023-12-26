#ifndef Detect_h
#define Detect_h

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define MIN(a, b) (((a) < (b)) ? (a) : (b))
#define MAX(a, b) (((a) > (b)) ? (a) : (b))

/* edit */
void BreakImg(unsigned char *src, int rows, int cols);
void RemovePart(unsigned char *src, int rows, int cols, int x, int y, int w, int h);

/* segment */
int *CompSize(unsigned char *img, int rows, int cols, int x, int y, int w, int h);

/* Array */
void free_array(int* arr);

#endif
