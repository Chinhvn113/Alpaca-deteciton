#Create an environment to work on google colab
#import os
#home=os.getcwd()

#mount drive on google colab
#from google.colab import drive
#drive.mount('/content/drive')

#Create a root path 
#ROOT_DIR=os.path.join(home,'/content/drive/MyDrive/Colab Notebooks/Alpacadataset')

#Install ultralytics on google colab
#!pip install ultralytics


from ultralytics import YOLO


#load model
model = YOLO("yolov8n.yaml")

#use model
#results = model.train(os.path.join.data=(ROOT_DIR,"config.yaml"), epochs=25)
results = model.train(data='config.yaml', epochs=20)