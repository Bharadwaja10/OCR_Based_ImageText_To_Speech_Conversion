import cv2
import os
import pytesseract
from PIL import Image

class OCRProcessor:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = r'D:\python\Python_Projects\OCR_Project\Tesseract-OCR\tesseract.exe'
        self.image_frames = 'image_frames/'

    def extract_text_from_image(self, image_path):
        img = cv2.imread(image_path)
        return pytesseract.image_to_string(img)

    def extract_text_from_video(self, video_path):
        if not os.path.exists(self.image_frames):
            os.makedirs(self.image_frames)

        self.collect_frames(video_path, frameno=300)
        return self.read_text_from_frames()

    def collect_frames(self, video_path, frameno):
        vid = cv2.VideoCapture(video_path)
        index = 0
        while vid.isOpened():
            ret, frame = vid.read()
            if not ret:
                break
            if index % frameno == 0:
                cv2.imwrite(f'./{self.image_frames}/frame{index}.png', frame)
            index += 1
        vid.release()

    def read_text_from_frames(self):
        text = ""
        for img_file in os.listdir(self.image_frames):
            img_path = os.path.join(self.image_frames, img_file)
            img = Image.open(img_path)
            text += pytesseract.image_to_string(img)
        return text
