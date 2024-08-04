# capture_faces.py
import cv2
import os

# Create a directory to store face images
if not os.path.exists('face_data'):
    os.makedirs('face_data')

user_id = input("Enter user ID: ")
user_name = input("Enter user name: ")

video = cv2.VideoCapture(0)
trainedDataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
count = 0

while True:
    success, frame = video.read()
    if success:
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = trainedDataset.detectMultiScale(gray_image)
        for (x, y, w, h) in faces:
            count += 1
            face = gray_image[y:y + h, x:x + w]
            file_name_path = f'face_data/user_{user_id}_{count}.jpg'
            cv2.imwrite(file_name_path, face)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow('Capturing Faces', frame)
        key = cv2.waitKey(1)
        if key == 27 or count >= 300:  # Press 'ESC' to exit or capture 100 images
            break
    else:
        print("Video completed or frame nill")
        break

video.release()
cv2.destroyAllWindows()
