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

int CirDfs(unsigned char *skel, int *vis, int rows, int cols, int l, int r, int val){
    if (l < 0 || l >= rows || r < 0 || r >= cols)
        return (0);

    int index = l * cols + r;
    if (vis[index] || !skel[index]) return (0);
    
    int len = 1;
    vis[index] = val;    

    for (int i = l - boxwire; i <= l + boxwire; i++)
        for (int j = r - boxwire; j <= r + boxwire; j++)
            len += CirDfs(skel, vis, rows, cols, i, j, val);

    return (len);
}

Dict *SimplfySkel(unsigned char *img, int *vis, int rows,int cols){
    int node_size, node, cnt;
    int len;
    Dict *res;

    node_size = 1;
    node = cnt = 1;

    res = (Dict*)malloc(node_size * sizeof(Dict));
    res[0].key = node_size;

    for (int i = 0; i < rows; i++){
        for (int j = 0; j < cols; j++){
            if (vis[i * cols + j]) continue;
            len = CirDfs(img, vis, rows, cols, i, j, cnt);

            if (len >= wire_lenght){
                node_size++;
                res = (Dict*)realloc(res, node_size * sizeof(Dict));
                res[0].key = node_size;

                res[node_size - 1].key = cnt;
                res[node_size - 1].val = node;
                node++;
            }
            cnt++;
        }
    }

    return (res);
}
