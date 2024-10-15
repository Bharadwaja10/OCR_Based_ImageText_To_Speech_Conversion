# OCR-Based Image-to-Speech Project

## 1. Main Components of the Project

### Frontend (GUI with Tkinter):
- **GUI Interface**: Built using Tkinter, provides an intuitive interface for user interaction.
- **Key Buttons**:
  - **Extract from Image**: Allows the user to select an image for OCR processing.
  - **Extract from Video**: Allows the user to select a video for OCR processing.
  - **About Us**: Displays information about the application.
- **Background Image**: Managed with Tkinter's canvas and layout managers for an appealing look.

### Backend (OCR and Text-to-Speech Processing):
- **OCRProcessor Class**: Handles text extraction from images and videos using Tesseract OCR.
- **TextToSpeech Class**: Converts the extracted text into speech using the `pyttsx3` library.

---

## 2. Project Flow
1. The user selects an image or video for text extraction.
2. The `OCRProcessor` processes the selected file, extracts the text, and displays it in a separate window.
3. The user can choose to hear the extracted text with available voice options (US Male, UK Female, or US Female).
4. The extracted text is converted to speech using the `pyttsx3` library.

---

## 3. Key Features

### OCR (Optical Character Recognition):
- **Image Extraction**: Uses OpenCV to read images and Tesseract to extract text.
- **Video Frame Extraction**: Processes every 300th frame from the video and applies OCR on the frames.

### Text-to-Speech:
- Converts extracted text into speech with multiple voice options using the `pyttsx3` library.

### GUI (Graphical User Interface):
- A user-friendly interface built with Tkinter, displaying buttons and a visually appealing background.

---

## 4. Folder Structure and Organization
- **src Folder**: Contains the Python source files (`main.py`, `frontend.py`, `backend.py`).
- **assets Folder**: Stores the background image for the GUI.
- **Tesseract-OCR Path**: Links the Tesseract executable to the project, stored outside the virtual environment for easy access.
- **image_frames Folder**: Holds frames extracted from videos for text processing.

---

## 5. Main Code Components
- **main.py**: Initializes the application, creates the GUI, and handles user interactions.
- **ocr.py**: Contains the `OCRProcessor` class for text extraction from images and videos using Tesseract.
- **text_to_speech.py**: Contains the `TextToSpeech` class for converting text to speech using `pyttsx3`.

---

## 6. Key Libraries Used
- **Tkinter**: For creating the GUI.
- **OpenCV (cv2)**: For image and video processing.
- **Pillow (PIL)**: For image handling and resizing in the GUI.
- **Pytesseract**: For text extraction from images and video frames.
- **Pyttsx3**: For converting text into speech.

---

## 7. Potential Enhancements
- Add advanced options for video processing (e.g., controlling the frame extraction frequency).
- Enhance the GUI with additional features, such as the ability to save extracted text to a file.

---

![](PyProject_img.png)
