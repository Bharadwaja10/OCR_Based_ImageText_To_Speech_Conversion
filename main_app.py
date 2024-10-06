import tkinter as tk
from tkinter import filedialog
from ocr import OCRProcessor
from text_to_speech import TextToSpeech
from PIL import Image, ImageTk


class OCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OCR BASED IMAGE TEXT TO SPEECH CONVERSION")

        # Window dimensions
        self.windowWidth = 1200
        self.windowHeight = 800
        self.root.geometry(f"{self.windowWidth}x{self.windowHeight}")

        # Set larger font size
        self.font_style = ("Helvetica", 16, "bold")

        # Create a canvas to ensure the background image fills the entire frame
        self.canvas = tk.Canvas(self.root, width=self.windowWidth, height=self.windowHeight, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Load and resize background image (replace with your image path)
        image_path = r"D:\python\Python_Projects\OCR_Project\bg1.png"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((self.windowWidth, self.windowHeight), Image.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(resized_image)

        # Place image on canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.image_tk)

        self.extract_image_button = tk.Button(self.root, text="Extract from Image",
                                              command=self.extract_text_from_image, font=self.font_style, height=2,
                                              width=20, bg="lightgreen", fg="black")
        self.extract_image_button.place(relx=0.3, rely=0.05)

        self.extract_video_button = tk.Button(self.root, text="Extract from Video",
                                              command=self.extract_text_from_video, font=self.font_style, height=2,
                                              width=20, bg="lightcoral", fg="black")
        self.extract_video_button.place(relx=0.5, rely=0.05)

        self.about_us_button = tk.Button(self.root, text="About Us", command=self.about_us, font=self.font_style,
                                         height=2, width=20, bg="lightyellow", fg="black")
        self.about_us_button.place(relx=0.7, rely=0.05)

        self.ocr_processor = OCRProcessor()
        self.text_to_speech = TextToSpeech()

    def extract_text_from_image(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select Image",
                                               filetypes=(("Image files", ".jpg *.png"), ("All files", ".*")))
        if file_path:
            extracted_text = self.ocr_processor.extract_text_from_image(file_path)
            self.show_extracted_text(extracted_text)

    def extract_text_from_video(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select Video",
                                               filetypes=(("Video files", ".mp4 *.avi"), ("All files", ".*")))
        if file_path:
            extracted_text = self.ocr_processor.extract_text_from_video(file_path)
            self.show_extracted_text(extracted_text)

    def show_extracted_text(self, text):
        top = tk.Tk()
        font_c = ("Century Gothic", 10, "normal")
        top.title('Extracted Text')
        text_box = tk.Text(top, font=font_c)
        text_box.insert('1.0', text)
        text_box.pack()

        # Speech Options
        tk.Button(top, text="David (US)", command=lambda: self.text_to_speech.speak(text, 0)).pack()
        tk.Button(top, text="Hazel (UK)", command=lambda: self.text_to_speech.speak(text, 1)).pack()
        tk.Button(top, text="Zira (US)", command=lambda: self.text_to_speech.speak(text, 2)).pack()

        top.mainloop()

    def about_us(self):
        # Create a new window for About Us
        about_window = tk.Toplevel(self.root)
        about_window.title("About Us")

        # Add content to the About Us window
        about_text = """\
        Welcome to our OCR Based Image Text to Speech Conversion application!

        This application is designed to help users extract text from images and videos 
        and convert it to speech. 

        Our mission is to make information accessible to everyone, including those with 
        visual impairments. 

        Thank you for using our app!
        """
        about_label = tk.Label(about_window, text=about_text, font=("Helvetica", 14), justify=tk.LEFT)
        about_label.pack(padx=20, pady=20)

        # Add a button to close the About Us window
        close_button = tk.Button(about_window, text="Close", command=about_window.destroy)
        close_button.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()

