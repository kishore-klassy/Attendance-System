# recognize_faces.py
import cv2
import pickle
import openpyxl
from datetime import datetime

# Load the trained model and the face dataset
trainedDataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('trained_model.yml')

# Load user names
with open('user_names.pkl', 'rb') as f:
    user_names = pickle.load(f)

# Initialize Excel file for attendance
file_path = 'attendance.xlsx'
try:
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
except FileNotFoundError:
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(["Name", "Date", "Time"])


# Function to log attendance
def log_attendance(name):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    sheet.append([name, date, time])
    workbook.save(file_path)


video = cv2.VideoCapture(0)
recognized_names = set()

while True:
    success, frame = video.read()
    if success:
        frame = cv2.flip(frame, 1)
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = trainedDataset.detectMultiScale(gray_image)
        for (x, y, w, h) in faces:
            face = gray_image[y:y + h, x:x + w]
            label, confidence = face_recognizer.predict(face)
            if confidence < 50:
                name = user_names.get(label, "Unknown")
                if name not in recognized_names:
                    log_attendance(name)
                    recognized_names.add(name)
                cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                cv2.putText(frame, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow('Face Recognition Attendance', frame)
        key = cv2.waitKey(1)
        if key == 27:  # Press 'ESC' to exit
            break
    else:
        print("Video completed or frame nill")
        break

video.release()
cv2.destroyAllWindows()
