# Description

	- RUN LENGTH SMOOTHING ALGORITHM(RLSA) is a method mainly used for block segmentation and text discrimination.

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

# Method

	- rlsa

# Parameters

	- horizantal - boolean
	- vertial - boolean
	- image - matrix/array
	- value - any positive integer(int)


