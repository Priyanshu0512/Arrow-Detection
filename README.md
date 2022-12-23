# Arrow-Detection

This project takes live video freed from the Webcam or Secondary video sources and Detect the prescence of any Red arrow of the specified color in the program and the Outline its edges using Contour detection and Approximation.The Functonality of the HSV Trackbars are also provided to detect various objects of of different shades of Red. The program utilises the **OpenCV** and **numpy** to exceute the Detection.


## To Start using the Project

You will need to install python3 and three of its Libraries**(OpenCV, numpy, imutils)** to run the main.py file.
You will also require a code editor of your choice to make improvements or run the program.

Link to Download PyCharm - [https://www.jetbrains.com/pycharm]

Link to Download VSCode - [https://code.visualstudio.com/download]

## Downloading Dependencies 

Install Python3 from the given link- [https://www.python.org/downloads/]
Clone the Repository onto to your Local machine and Copy and Run the following Commands in the Terminal.

```
pip3 install numpy
pip3 install opencv-python
```

## DEMO

### Masking Red Color
<img width="1278" alt="Screenshot 2022-12-23 at 11 51 55 PM" src="https://user-images.githubusercontent.com/112048497/209391542-31e2d5c8-c886-46d1-9c96-bfc8df594e6f.png">


### Trackbars
<img width="196" alt="Screenshot 2022-12-23 at 11 52 32 PM" src="https://user-images.githubusercontent.com/112048497/209391566-cc781626-7a47-40d5-8521-b7f66dd0baa5.png">


### LIVE Detection
<img width="1051" alt="Screenshot 2022-12-23 at 11 55 03 PM" src="https://user-images.githubusercontent.com/112048497/209391592-a5fe8465-55c1-45f8-be73-11bb56fa058f.png">


### Con's of the Program 

1. The code will detect all the objects with Colour red if the HSV of the object matches to that of the specified values.
2. Contours which are being detected does not remain smooth on changing the perspective of the image or object.
3. The code is not able to display the orientation of the object.
