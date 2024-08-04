# Face Recognition Attendance System

## Description
This project is a Face Recognition Attendance System that utilizes OpenCV and machine learning to identify individuals and log their attendance automatically. When a user is recognized, their name, along with the current date and time, is recorded in an Excel sheet. This system is designed to be scalable, allowing it to recognize and log the attendance of multiple users efficiently.

## Features
- **Real-time Face Detection and Recognition**: Uses the Haar Cascade classifier for face detection and LBPH (Local Binary Patterns Histograms) for face recognition.
- **Scalable User Management**: Capable of handling the recognition of hundreds of different users.
- **Automated Attendance Logging**: Logs the user's name, date, and time of recognition into an Excel sheet.
- **Interactive User Registration**: Captures face images from a webcam and associates them with user IDs and names.

## Technologies Used
- **Python**: The core programming language for the project.
- **OpenCV**: Used for face detection and recognition.
- **OpenPyXL**: For handling Excel file operations.
- **Pickle**: For saving and loading user data.

## Setup and Installation

### Prerequisites
- Python 
- OpenCV
- OpenPyXL

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/kishore-klassy/Attendance-System.git
   cd Attendance-System
   ```

2. Install the required packages:
   ```bash
   pip install opencv-python opencv-contrib-python openpyxl
   ```

## Usage

### Step 1: Capture Face Images
Run the `capture_faces.py` script to capture face images for each user. You will be prompted to enter a user ID and name. The script will capture 100 images of the user's face and save them in the `face_data` directory.
```bash
python capture_faces.py
```

### Step 2: Train the Model
Run the `train_model.py` script to train the face recognition model using the captured images.
```bash
python train_model.py
```

### Step 3: Recognize Faces and Log Attendance
Run the `recognize_faces.py` script to start the real-time face recognition attendance system. When a user is recognized, their name, along with the current date and time, will be logged in the `attendance.xlsx` file.
```bash
python recognize_faces.py
```

## Files and Directories
- `capture_faces.py`: Script for capturing face images from the webcam.
- `train_model.py`: Script for training the face recognition model.
- `recognize_faces.py`: Script for recognizing faces and logging attendance.
- `haarcascade_frontalface_default.xml`: Pre-trained Haar Cascade classifier for face detection.
- `face_data/`: Directory to store captured face images.
- `trained_model.yml`: File to store the trained face recognition model.
- `user_names.pkl`: Pickle file to store user names associated with their IDs.
- `attendance.xlsx`: Excel file to log attendance.

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License.
```
