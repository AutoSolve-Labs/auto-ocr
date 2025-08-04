import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image
import pytesseract
import pyperclip

# FIX: Point to Tesseract manually
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

SCREENSHOT_DIR = r'C:\Users\laksh\Pictures\Screenshots'

class ScreenshotHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith((".png", ".jpg", ".jpeg")):
            print(f"New screenshot: {event.src_path}")
            time.sleep(1)  # Let file save completely
            try:
                text = pytesseract.image_to_string(Image.open(event.src_path),lang='eng+hin')
                print("Extracted text:\n", text.strip())
                pyperclip.copy(text)
                print("Text copied to clipboard!")
            except Exception as e:
                print("Error processing image:", e)

if __name__ == "__main__":
    print("Watching for screenshots in:", SCREENSHOT_DIR)
    print("Tesseract version:", pytesseract.get_tesseract_version())
    event_handler = ScreenshotHandler()
    observer = Observer()
    observer.schedule(event_handler, path=SCREENSHOT_DIR, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
