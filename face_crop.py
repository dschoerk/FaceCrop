import face_recognition
import cv2
import os


path_to_images = "member-images"

filelist=os.listdir(path_to_images)
for f in filelist[:]: 
    img = cv2.imread(path_to_images + "/" + f)

    if img is None:
        continue

    face_locations = face_recognition.face_locations(img)
    if len(face_locations) > 0:
        (top, right, bottom, left) = face_locations[0]    
        
        w = right - left
        h = bottom - top

        w_ext = w * 0.8
        left = int(left - w_ext)
        right = int(right + w_ext)
        
        top = int(top - h * 0.8)
        bottom = int(bottom + h * 1.2)

        #img = cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
        #img = cv2.GaussianBlur(img,(135,135),0)

        #cv2.imshow('Video', img)
        #cv2.waitKey(0)

        cv2.imwrite(f+"_crop.jpg", img[top:bottom, left:right])
    
    print(face_locations)


print(filelist)

