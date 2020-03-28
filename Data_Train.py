import cv2
import numpy as np
from os import listdir
from os.path import isfile,join


data_path='E:\\SOFTWARE\\Face_Recognition\\venv\\Opencv_Face_Data\\Faces\\'
onlyfiles=[f for f in listdir(data_path) if isfile(join(data_path,f))]
Trainig_Data,Labels=[],[]


for i,files  in enumerate(onlyfiles):
    image_path=data_path + onlyfiles[i]
    images=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    Trainig_Data.append(np.asarray(images,dtype=np.uint8))
    Labels.append(i)

Labels  = np.asarray(Labels,dtype= np.int32)


model = cv2.face.LBPHFaceRecognizer_create()
model.train(np.asarray(Trainig_Data),np.asarray(Labels))
print("\n\n\t\t Data Successfuly Trained .\n\t\t")
