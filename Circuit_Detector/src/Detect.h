#ifndef Detect_h
#define Detect_h

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <windows.h>

#define MIN(a, b) (((a) < (b)) ? (a) : (b))
#define MAX(a, b) (((a) > (b)) ? (a) : (b))

#define GRAY_SCALE 70

#define boxwire 1
#define wire_lenght 100
#define max_lenght 10000
#define MAX_IMG_SIZE 10000
#define CAP_RATIO 10

typedef struct{
    int key;
    int val;
} Dict;

/* edit */
void BreakImg(unsigned char *src, int rows, int cols);
void RemovePart(unsigned char *src, int rows, int cols, int x, int y, int w, int h);

/* segment */
int *CompSize(unsigned char *img, int rows, int cols, int x, int y, int w, int h);
int *nodeScale(int *nodes, int *vis, int rows, int cols, int n);
int CirDfs(unsigned char *skel, int *vis, int rows, int cols, int l, int r, int val, int deep);
Dict *SimplfySkel(unsigned char *img, int *vis, int rows,int cols, int state);

/* components */
int CheckDc(unsigned char *img, int rows, int cols);

/* Array */
void free_array(int* arr);
void free_dict(Dict* arr);

#endif
