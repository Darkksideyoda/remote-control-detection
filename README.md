# remote-control-detection :control_knobs:
Remote Control Devices analysis and Detection with Image Processing and Computer Vision Techniques
### Goals
- Controlling Whether Users Send Remote Control or Another Image to the System in the Infrastructure to be Established in the Future.

- If the Sent Image is a Remote Control, Detection Without Asking the User How Many Buttons There Are.

### Working Principle

- I ran and tested the project in Python 3.7.6 in Conda. :snake:
- In order to Run the Project, you must download the below file yolo.h5 and store it in the same directory as the script files https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5/
Imageai From here Thank you very much.
- An example of a remote that I photographed and its output are as follows.

<p align="center">
<img src="https://raw.githubusercontent.com/Darkksideyoda/Darkksideyoda.github.io/master/Urlimages/orgin1.PNG" width="200" height="200" />
</p>

- At this point, if the photo sent by the user is not a remote control or the probability of it being a remote control is below 40%, we block the photo to be sent from the beginning.

- As the next step, in order to prepare for basic image processing techniques, the texts on the control must be deleted. Otherwise, it may accept "O, Ö, C," or similar letters as buttons while scanning the buttons.

- The First Part of Image Processing is Using an Edge Detection Algorithm. The reason for this is that detecting buttons, etc. elements from the Raw Image will be more complex and erroneous, so we only need borders. There are multiple edge detection algorithms, but in my opinion, the most optimal algorithm in this project is sobel.

<p align="center">
<img src="https://raw.githubusercontent.com/Darkksideyoda/Darkksideyoda.github.io/master/Urlimages/output1.png" width="200" height="200" />
  
<img src="https://raw.githubusercontent.com/Darkksideyoda/Darkksideyoda.github.io/master/Urlimages/output2.png" width="200" height="200" />
</p>

