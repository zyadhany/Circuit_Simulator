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

int *nodeScale(int *nodes, int *vis, int rows, int cols, int n){
    int index;
    int *res = malloc(sizeof(int) * 4);
    res[0] = res[1] = 2400;
    res[2] = res[3] = 0;
    for (int i = 0; i < rows; i++){
        for (int j = 0; j < cols; j++){
            index = i * cols + j;
            if (vis[index])
                for (int k = 0; k < n; k++)
                    if (vis[index] == nodes[k]){
                        res[0] = MIN(res[0], j);
                        res[2] = MAX(res[2], j);
                        res[1] = MIN(res[1], i);
                        res[3] = MAX(res[3], i);
                        break;
                    }
        }
    }
    res[2] -= res[0];
    res[3] -= res[1];
    return (res);
}

int CirDfs(unsigned char *skel, int *vis, int rows, int cols, int l, int r, int val, int deep){
    if (l < 0 || l >= rows || r < 0 || r >= cols)
        return (0);

    int index = l * cols + r;
    if (vis[index] || !skel[index]) return (0);
    
    int len = 1;
    vis[index] = val;    

    if (deep > max_lenght) return 1;

    for (int i = l - boxwire; i <= l + boxwire; i++)
        for (int j = r - boxwire; j <= r + boxwire; j++)
            len += CirDfs(skel, vis, rows, cols, i, j, val, deep + 1);

    return (len);
}

Dict *SimplfySkel(unsigned char *img, int *vis, int rows, int cols, int state){
    int node_size, node, cnt, index, isit;
    int len;
    Dict *res;

    node_size = 1;
    node = cnt = 1;

    res = (Dict*)malloc(node_size * sizeof(Dict));
    res[0].key = node_size;

    for (int i = 0; i < rows; i++){
        for (int j = 0; j < cols; j++){
            index = i * cols + j;
            
            if (!img[index]) continue;

            if (vis[index]){
                isit = 0;
                for (int k = 1; k < node_size; k++)
                    if (vis[index] == res[k].key){
                        isit = 1;
                        break;
                    }
                img[index] *= isit;   
                continue;
            }

            len = CirDfs(img, vis, rows, cols, i, j, cnt, 1);
            if (len >= wire_lenght * state && len <= max_lenght){
                node_size++;
                res = (Dict*)realloc(res, node_size * sizeof(Dict));
                res[0].key = node_size;

                res[node_size - 1].key = cnt;
                res[node_size - 1].val = node;
                node++;
            }else img[index] = 0;
            cnt++;
        }
    }  
    return (res);
}
