# import os module for reading and creating directories
import os
# import opencv-python to perform binarization on input images
import cv2
# import pythonRLSA to perform run-length smearing on images
import pythonRLSA as rlsa
# import the time module for calculating how long each operation takes
from time import time as timer

# get the list of all images stored in the folder images/in/
input_images = os.listdir("images/in/")
# sort the input image files in alphabetical order (just for aesthetics)
input_images.sort()

# variable to calculate how long the whole program took
start_time = timer()

# repeat the following for all images in the images/in/ folder
for image_name in input_images:
    # print the name of file currently being processed
    print(" [ INFO ] NOW READING :: ", image_name)
    
    # start the timer, i.e., store the current time in a variable
    begin = timer()
    
    # read the image in grayscale format
    image = cv2.imread("images/in/" + image_name, 0)
    
    # print how long it took to read the image
    print(" [ INFO ] read the image to numpy array in ", timer() - begin, " seconds")
    # reset the timer
    begin = timer()
    
    # binarize the image using adaptive thresholding
    image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 7)
    
    # print how long it took to binarize the image
    print(" [ INFO ] binarized image in ", timer() - begin, " seconds")
    # reset the timer
    begin = timer()
    
    # perform horizontal and vertical smearing on the image
    out = rlsa.rlsa(image, True, True, 10)
    
    # print how long it took to perform smearing
    print(" [ INFO ] performed horizontal and vertical smearing in ", timer() - begin, "seconds")
    
    # save this output as image
    cv2.imwrite("images/out/HV_" + image_name, out)
    
    # reset the timer
    begin = timer()
    
    # perform horizontal and vertical smearing on the image
    out = rlsa.rlsa(image, True, False, 10)
    
    # print how long it took to perform smearing
    print(" [ INFO ] performed horizontal smearing in ", timer() - begin, "seconds")
    
    # save this output as image
    cv2.imwrite("images/out/H_" + image_name, out)
    
    # reset the timer
    begin = timer()
    
    # perform horizontal and vertical smearing on the image
    out = rlsa.rlsa(image, False, True, 10)
    
    # print how long it took to perform smearing
    print(" [ INFO ] performed vertical smearing in ", timer() - begin, "seconds")
    
    # save this output as image
    cv2.imwrite("images/out/V_" + image_name, out)
    
    # reset the timer
    begin = timer()
    
    # perform horizontal and vertical smearing on the image
    out = rlsa.rlsa(image, False, False, 10)
    
    # print how long it took to perform smearing
    print(" [ INFO ] performed neither smearing in ", timer() - begin, "seconds")
    
    # save this output as image
    cv2.imwrite("images/out/_" + image_name, out)
    
    print("\n\n")
    
print(" [ INFO ] processed ", len(input_images), " images in ", timer() - start_time, " seconds")
