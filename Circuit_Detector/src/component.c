#include "Detect.h"

/*
 * CheckDc - check if it's a DC source.
 *
 * @img: Pointer to the image data (2D array of unsigned characters)
 * @rows: Number of rows in the image
 * @cols: Number of columns in the image
 *
 * Return: state of the DC component.
 *         - 0 if it's not a DC source
 *         - 1 if it's +- left to right (x-axis)
 *         - 2 if it's -+ left to right (x-axis)
 *         - 3 if it's +- top to bottom (y-axis)
 *         - 4 if it's -+ top to bottom (y-axis)
 */

int CheckDc(unsigned char *img, int rows, int cols){
    int n, l, r, state;
    int *L, *R, *tmp;
    
    l = r = state = 0;
    tmp = NULL;

    L = malloc(sizeof(int) * rows);
    R = malloc(sizeof(int) * cols);
    for (int i = 0; i < rows; i++) L[i] = 0;
    for (int i = 0; i < cols; i++) R[i] = 0;
    
    for (int i = 0; i < rows; ++i)
        for (int j = 0; j < cols; ++j)
            if (img[i * cols + j]) L[i]++, R[j]++;

    for (int i = 0; i < rows; i++)
        if (!L[i]) l++;
    for (int i = 0; i < cols; i++)
        if (!R[i]) r++;
    
    if (l > r) state = 3, tmp = L, n = rows;
    else if (l < r) state = 1, tmp = R, n = cols;
    l = r = 0;
    if (tmp){
        for (int i = 0; tmp[i] ; i++) l = MAX(l, tmp[i]);
        for (int i = n - 1; tmp[i] ; i--) r = MAX(r, tmp[i]);
    }
    
    free(L); free(R);
    state += (r > l);
    return (state);
}