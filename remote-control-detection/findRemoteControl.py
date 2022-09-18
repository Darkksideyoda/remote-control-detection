from imageai.Detection import ObjectDetection
import PIL.Image
from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("100x100")

def showMessage(isRemote):
   messagebox.showinfo("Remote Info",isRemote)

obj_detect  = ObjectDetection()
obj_detect.setModelTypeAsYOLOv3()


obj_detect.setModelPath("yolo.h5")
obj_detect.loadModel()


obj_detect.CustomObjects(remote=True)


detected_obj = obj_detect.detectObjectsFromImage(
    input_image="data/myImageData/img9.jpg",
    output_image_path="test_image_output.jpg",
    minimum_percentage_probability=20
)


for obj in detected_obj:
    if obj["name"] == "remote":
        showMessage("Kumanda Tespit Edildi !")
        print("Remote Control Detected !\n")
        print(obj["percentage_probability"])
        print(obj["box_points"])

    else:
        print("Ne Yazık ki Kumanda Bulunamadi !")

im = PIL.Image.open("test_image_output.jpg")
im.show()
