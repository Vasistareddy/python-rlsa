from typing import List
import numpy

def rlsa(image: List[int], horizontal: bool = True, vertical: bool = True, value: int = 0) -> List[int]:
    # image must be binary
    if isinstance(image, numpy.ndarray):
        value = value if value>=0 else 0
        try:
            X, Y = image.shape

            # RUN LENGTH SMOOTHING ALGORITHM working horizontal on the image
            if horizontal:
                for i in range(0,X):
                    c = 0
                    for j in range(0, Y):
                        if image[i, j] == 0:
                            if (j-c) < value:
                                image[i, c:j] = 0               
                            c = j    

            # RUN LENGTH SMOOTHING ALGORITHM working vertical on the image
            if vertical:
                for i in range(0, Y):
                    c = 0
                    for j in range(0, X):
                        if image[j, i] == 0:
                            if (j-c) < value:
                                image[c:j, i] = 0
                            c = j

        except (AttributeError, ValueError) as e:
            print("ERROR:\n")
            print('Image must be an numpy array and must be in "binary". Use Opencv/PIL to convert the image to binary.\n')
            print("import cv2;\nimage=cv2.imread('path_of_the_image');\ngray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);\n\
                (thresh, image_binary) = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)\n")
            print("pass like this -- rlsa.rlsa(True, False, image_binary, 10)")
    else:
        print('Image must be an numpy array and must be in binary')
    return image