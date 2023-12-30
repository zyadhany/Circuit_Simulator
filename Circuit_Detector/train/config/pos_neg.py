import os
import cv2

opj = 'DCS'
directory = 'data/images'
files = os.listdir(directory)

pos = open(f'data/{opj}pos.txt', 'w')
neg = open(f'data/{opj}neg.txt', 'w')
cnt = 0

for file in files:
    path = f"{directory}/{file}"
    cnt += 1
    if opj in file:

        img = cv2.imread(path, 0)

        w1, w2, h1, h2 = 120, 0, 120 ,0

        for i in range(len(img)):
            for j in range(len(img[0])):
                if img[i][j]:
                    w1 = min(w1, j)
                    w2 = max(w2, j)
                    h1 = min(h1, i)
                    h2 = max(h2, i)

        pos.write(f'{path[5:]} 1 {w1} {h1} {w2 - w1} {h2 - h1}\n')
    else:
        neg.write(f'{path[5:]}\n')

pos.close()
neg.close()
