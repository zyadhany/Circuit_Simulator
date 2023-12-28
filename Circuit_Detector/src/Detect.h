#ifndef Detect_h
#define Detect_h

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define MIN(a, b) (((a) < (b)) ? (a) : (b))
#define MAX(a, b) (((a) > (b)) ? (a) : (b))

#define boxwire 8
#define wire_lenght 200

typedef struct{
    int key;
    int val;
} Dict;

/* edit */
void BreakImg(unsigned char *src, int rows, int cols);
void RemovePart(unsigned char *src, int rows, int cols, int x, int y, int w, int h);

/* segment */
int *CompSize(unsigned char *img, int rows, int cols, int x, int y, int w, int h);
int CirDfs(unsigned char *skel, int *vis, int rows, int cols, int l, int r, int val);
Dict *SimplfySkel(unsigned char *img, int *vis, int rows,int cols);

/* Array */
void free_array(int* arr);
void free_dict(Dict* arr);

#endif
