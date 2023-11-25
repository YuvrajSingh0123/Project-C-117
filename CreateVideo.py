import os
import cv2

path = "Images/"
images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)
output = cv2.VideoWriter("project.avi",cv2.VideoWriter_fourcc(*"DIVX"),0.8,(400,400))
for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    output.write(frame)
output.release()