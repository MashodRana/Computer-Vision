## Extraction of interior pixel values of a contour
Interior pixel values may be needed for to detect the color of the contour.

And here is the solution that how we can extract the points of contour which lies inside the contour. From these points 
we can extract the pixel values. We can get the RGB values for 3D image and single value for gray scale image with 
points that we will extract.

### How to do ?
- Convert the image into a gray scale image.
- Apply binary threshold or canny edge detection to get better result on contour detection.
    - OpenCV `findContours` function works on a image which background is black and foreground is white.
- Find contours with OpenCV function `cv2.findContours()` .
- Find pixels of each contour<br>
 _For each of the contour_
    - create a create an empty image (8-bit gray scale image) known as mask with image height, width.
    - draw contour on the mask and fill the contour with 255. So that mask will only have white(255)  on a black(0) 
    background. So we can search each pixel in the mask to see if it is 255 or 0. 
    - find the coordinates of pixels by searching on the mask for value 255.
    - extract pixels from the image with help of coordinates.

### Resources
To get details intuition these links could be helpful.
- [points inside a contour](http://opencv-users.1802565.n2.nabble.com/points-inside-a-contour-td5318979.html)
- [efficient way of counting pixels in a contour - opencv](https://html.developreference.com/article/25267637/efficient+way+of+counting+pixels+in+a+contour)
- [How to print all coordinates inside the Contour opencv - opencv](https://html.developreference.com/article/22683795/How+to+print+all+coordinates+inside+the+Contour+opencv)
- [How to print all coordinates inside the Contour opencv](https://stackoverflow.com/questions/16975509/how-to-print-all-coordinates-inside-the-contour-opencv)
- [Access pixel values within a contour boundary using OpenCV in Python](https://stackoverflow.com/questions/33234363/access-pixel-values-within-a-contour-boundary-using-opencv-in-python)

 
