# Load necessary packages
import cv2
import numpy as np
import matplotlib.pyplot as plt


def preprocess_image(img):
    """
        This method for preprocessing the image.
        First convert the image into gray scale image then apply binary thresholding to get
        better result on contour detection.
    parameters::
     img: a image.

    returns::
        Return a tuple contain a gray image and a binary image respectively.
    """

    # Converting image color BGR to GRAY
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plt.imshow(gray)  # display the gray image
    plt.show()

    # Using binary threshold
    _, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    plt.imshow(binary, cmap='gray')  # display the threshold image
    plt.show()

    return gray, binary


def find_contours(binary_img):
    """
        Find a list of  contours present in the image. Binary image/ gray scale image
        is recommended by openCV.
    parameters::
     binary_img: a image where pixels are settled with thresholding.
    returns::
        A list of contours.
    """
    # Finding the contours
    cnts, _ = cv2.findContours(binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print("Number of contours: %d" % (len(cnts)))

    return cnts


def extract_pixels(img, cnts):
    """
        Extract pixel values of the image.
    parameters::
     img: a image. if this is a RGB or BGR image pixel will be a numpy array with 3 elements.
     cnts: a list of contours extracted with cv2.findContours function.
    returns::
     A list contain pixel value for each of the contour.
    """

    cnts_px = []

    for i, contour in enumerate(cnts):
        # Create numpy array with image height and width
        mask = np.zeros(img.shape[:2], dtype=np.uint8)

        # Draw the contour on the mask
        cv2.drawContours(mask, cnts, i, color=255, thickness=cv2.FILLED)

        # Find the coordinates of pixels and pixel values
        px = np.where(mask == 255)  # get the (x,y) position of each pixel which has value 255

        # Extract coordinates value from the image
        cnts_px.append(img[px[0], px[1]])  # store pixels into the list

    return cnts_px

if __name__=='__main__':

    # Reading an image
    file_name = 'images/test2.jpg'
    image = cv2.imread(file_name)

    # Preprocess the image
    gray_img, bin_img = preprocess_image(image)

    # Find contours
    contours = find_contours(bin_img)

    # Find pixel  values of each contour
    cont_pxvalues = extract_pixels(gray_img, contours)
