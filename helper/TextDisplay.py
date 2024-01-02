import cv2
import numpy as np

class TextDisplay:
    def __init__(self):
        self.window_name = "Text Window"

    def display_text(self, file_path):
        with open(file_path, 'r') as file:
            text_content = file.read()
        if text_content:
            image = self.render_text_to_image(text_content)
            cv2.imshow(self.window_name, image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("File content is empty.")

    def render_text_to_image(self, text, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=0.5, font_color=(255, 255, 255),
                             line_type=1):
        image_height = 800
        image_width = 800
        image = np.zeros((image_height, image_width, 3), dtype=np.uint8)

        position = (50, 50)
        y_offset = 30 

        lines = text.split('\n')
        for line in lines:
            cv2.putText(image, line, position, font, font_scale, font_color, lineType=line_type)
            position = (position[0], position[1] + y_offset)

        return image
