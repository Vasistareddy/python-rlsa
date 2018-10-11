# Description

	- RUN LENGTH SMOOTHING ALGORITHM(RLSA) is a method mainly used for block segmentation and text discrimination.
	- It mainly uses in Document Image Processing to extract out the ROI(region of interest) like block-of-text/title/content with applied heuristics.

# Input & Output
![Input](https://github.com/Vasistareddy/python-rlsa/blob/master/images/image.jpeg)
- **Input**-------------------------------**Horizontal RLSA**----------------------**Vertical RLSA**------------------------**Horizontal and Vertical RLSA**

# Prerequisites

	- Image must be a binary(255's/1's/0's)
	- Must pass a predefined limit, a certain "value"

# How it works

	- '255'(white pixel) wil be converted to '0'(black pixel) in a image, if the number of adjacent 255's are less than the predefined limit "value".
	- The "value" varies among the different images.

# Test Case

	- value = 3
	- input - [0, 0, 255, 255, 255, 0, 0, 255, 0, 0, 255, 0, 255]
	- output - [0, 0, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 255]

# Install requirements

	- pip install -r requirements.txt
	- if python.__version__ < 3.5: pip install typing
**https://pypi.org/project/typing/**

# Method

	- rlsa

# Parameters

	- image - numpy.ndarray(required)
	- horizantal - boolean
	- vertial - boolean
	- value - any positive integer(int)
	- rlsa(image(ndarray), horizontal=True/False, vertical=True/False, value(int))

# IPython Usage

	- # convert the image to binary
	- import cv2
	- image = cv2.imread('image.jpg')
	- gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	- (thresh, image_binary) = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	- import rlsa
	- image_rlsa_horizontal = rlsa.rlsa(image_binary, True, False, 10)



