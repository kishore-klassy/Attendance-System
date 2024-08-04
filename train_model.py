# train_model.py
import cv2
import numpy as np
import os
import pickle

# Load the face recognizer
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Function to get the images and labels from the dataset
def get_images_and_labels(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    face_samples = []
    face_ids = []
    for image_path in image_paths:
        # Extract the image file name without directory
        file_name = os.path.basename(image_path)
        # Split the file name to get the face ID
        face_id = int(file_name.split("_")[1])
        gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        face_samples.append(gray_image)
        face_ids.append(face_id)
    return face_samples, face_ids

# Get the faces and IDs
faces, ids = get_images_and_labels('face_data')

# Train the model
face_recognizer.train(faces, np.array(ids))

# Save the trained model
face_recognizer.save('trained_model.yml')

# Save the user names (this assumes you collect names during data collection)
user_names = {}
for image_path in os.listdir('face_data'):
    user_id = int(image_path.split("_")[1])
    if user_id not in user_names:
        user_names[user_id] = input(f"Enter name for user ID {user_id}: ")

with open('user_names.pkl', 'wb') as f:
    pickle.dump(user_names, f)
