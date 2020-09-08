# Description

	- RUN LENGTH SMOOTHING ALGORITHM(RLSA) is a method mainly used for block segmentation and text discrimination.
	- It mainly uses in Document Image Processing to extract out the ROI(region of interest) like block-of-text/title/content with applied heuristics.

# Input & Output
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**output of 3 cases with value "10" are in the below image**
![Input&Output](https://github.com/Vasistareddy/python-rlsa/blob/master/test_images/image1.jpeg)

# Sample Test Case

	- value = 3
	- input - [0, 0, 255, 255, 255, 0, 0, 255, 0, 0, 255, 0, 255]
	- output - [0, 0, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 255]

# Unittest Results

![Unittest](https://github.com/Vasistareddy/python-rlsa/blob/master/test_images/unittest.png)

# Prerequisites
	
	- python3.5+
	- Image must be a binary ndarray(255's/1's/0's)
	- Must pass a predefined limit, a certain integer "value"

# How it works

	- '255'(white pixel) wil be converted to '0'(black pixel) in a image, if the number of adjacent 255's are less than the predefined limit "value".
	- The "value" varies among the different images.

# Install requirements

	- pip install -r requirements.txt
	- if python.__version__ < 3.5: pip install typing
	- Read the docs here !(https://pypi.org/project/typing/)

# Method

	- rlsa

# Parameters

	- image - numpy.ndarray(required)
	- horizantal - boolean(required)
	- vertial - boolean(required)
	- value - any positive integer(int)(required)

# IPython Usage to convert Image to Binary and RLSA application

	- # convert the image to binary
	- import cv2
	- image = cv2.imread('image.jpg')
	- gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	- (thresh, image_binary) = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	- # function call
	- import rlsa
	- image_rlsa_horizontal = rlsa.rlsa(image_binary, True, False, 10)



