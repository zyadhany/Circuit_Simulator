#include "Detect.h"

int CheckDc(unsigned char *img, int rows, int cols){
    int *L, *R, state = 0;
    
    L = malloc(sizeof(int) * rows);
    R = malloc(sizeof(int) * cols);
    for (int i = 0; i < rows; i++) L[i] = 0;
    for (int i = 0; i < cols; i++) R[i] = 0;
    
    for (int i = 0; i < rows; ++i)
        for (int j = 0; j < cols; ++j)
            if (img[i * cols + j]) L[i]++, R[j]++;;

    for (int i = 0; i < rows; i++)
        if (!L[i]) state = 1;
    for (int i = 0; i < cols; i++)
        if (!R[i]) state = 1;
    
    free(L); free(R);
    return (state);
}