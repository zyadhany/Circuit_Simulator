import cv2
import os

opj = 'gnd'
rotate = 1
dist = 'data/images'
directory = 'data/archive/SolvaDataset_200_v3/gnd_1'
files = os.listdir(directory)

def getline(img):
    for row in range(len(img)):
        for col in range(len(img[row])):
            img[row][col] = (img[row][col] >= 128) * 255  # Modify pixel value based on condition

for file in files:
    input_image_path = f"{directory}/{file}"
    output_image_path = f'{dist}/{opj}{file[:-4]}.jpg'

    img = cv2.imread(input_image_path, 0)
    getline(img)
    cv2.imwrite(output_image_path, img)

    for i in range(1, rotate):
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        output_image_path = f'{dist}/{opj}{file[:-4]}{"R"*i}.jpg'
        cv2.imwrite(output_image_path, img)
