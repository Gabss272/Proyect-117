import os 
import cv2

path = "Images"
Images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file
        print(file_name)
        Images.append(file_name)

count = len(Images)
print(count)

frame = cv2.imread(Images[0])
width,height,channels = frame.shape
size = (width,height)
print(size)

out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count):
    frame = cv2.imread(Images[i])
    frame = cv2.resize(frame, size)
    out.write(frame)


out.release()
print("End")