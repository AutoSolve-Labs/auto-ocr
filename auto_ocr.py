import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image
import pytesseract
import pyperclip
import sys, os
import json

if getattr(sys, 'frozen', False):  
    base_path = sys._MEIPASS
    config_path = os.path.join(base_path, 'config.json')
else:
    config_path = os.path.join(os.getcwd(), 'config.json')

with open(config_path) as f:
    config = json.load(f)


if getattr(sys, 'frozen', False):  
    base_path = sys._MEIPASS  
    pytesseract.pytesseract.tesseract_cmd = os.path.join(base_path, 'tesseract_portable', 'tesseract.exe')
else:
    pytesseract.pytesseract.tesseract_cmd = r"C:\path\to\tesseract_portable\tesseract.exe"


SCREENSHOT_DIR = config["SCREENSHOT_DIR"]
lang = config["lang"]

class ScreenshotHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.lower().endswith((".png", ".jpg", ".jpeg")):
            print(f"New screenshot detected: {event.src_path}")
            time.sleep(1)
            try:
                text = pytesseract.image_to_string(Image.open(event.src_path), lang)
                pyperclip.copy(text)
            except Exception as e:
                print("Error while processing the screenshot:", e)

if __name__ == "__main__":
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
