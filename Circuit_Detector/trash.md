# editor.py
```python
    def breakImg(src):
        for row in range(len(src)):
            for col in range(len(src[row])):
                src[row][col] = (src[row][col] < 128) * 255
        return src

    def remove_part(img, y, x, h, w):
        for i in range(x, x + w):
            for j in range(y, y + h):
                img[i][j] = 0
```
# segment.py
```python
    def DfsCirc(skel, vis, n, m, l, r, val):
        if l < 0 or l >= n or r < 0 or r >= m:
            return 0
        if vis[l][r] != 0 or skel[l][r] == 0:
            return 0
        len = 1
        vis[l][r] = val    

        for i in range(l - boxwire, l + boxwire + 1):
            for j in range(r - boxwire, r + boxwire + 1):
                len += DfsCirc(skel, vis, n, m, i, j, val)
        return (len)

    def simplfySkel(skel):
        sys.setrecursionlimit(1000000)
        n, m = skel.shape
        vis = np.zeros((n, m), dtype=int)
        dist = {0:0}
        result = {}
        cnt = 1
        node = 1


        for i in range(n):
            for j in range(m):
                cnt += 1
                len = DfsCirc(skel, vis, n, m, i, j, cnt)
                dist[cnt] = len
    
        for i in range(n):
            for j in range(m):
                if dist[vis[i][j]] >= wire_lenght:
                    if vis[i][j] not in result:
                        result[vis[i][j]] = node
                        node += 1
                else :
                    skel[i][j] = 0
        return ([result, vis])
```
# componenet.py

```python
    def compSize(self, img, x, y, w, h):
        w1, w2, h1, h2 = 2400, -1, 2400, -1
        for i in range(x, x + w):
            for j in range(y, y + h):
                if img[j][i]:
                    w1 = min(w1, j)
                    w2 = max(w2, j)
                    h1 = min(h1, i)
                    h2 = max(h2, i)
        if w2 == -1:
            return [0, 0]
        return [w1, h1, w2 - w1, h2 - h1]
```

# f1.py
```python

```

# f2.py
```python

```