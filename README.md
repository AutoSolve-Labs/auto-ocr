
# Auto OCR Clipboard Watcher

This tool automatically watches your **Screenshots folder** and extracts text from newly added image files (`.png`, `.jpg`, `.jpeg`) using Tesseract OCR. The extracted text is copied directly to your clipboard.

Useful for quickly grabbing text from screenshots — no manual steps needed.

---

## Features

- ✅ Automatically detects new screenshots
- ✅ OCR text extraction using `pytesseract` (supports English + Hindi)
- ✅ Text copied to clipboard
- ✅ Runs silently in the background (no console window)
- ✅ Built using `uv`, `PyInstaller`, and `watchdog`

---

## Prerequisites

### 1. Install [Tesseract OCR for Windows](https://github.com/tesseract-ocr/tesseract)

Install to the default path:  
```

C:\Program Files\Tesseract-OCR\tesseract.exe

````

Make sure it supports languages:  
- English (`eng`)
- Hindi (`hin`)

Download Hindi language pack if not already present:
```bash
# Inside the Tesseract tessdata folder
# Download: https://github.com/tesseract-ocr/tessdata
````

---

### 2. Install `uv`

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

or follow instructions at [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/auto-ocr-clipboard-watcher.git
cd auto-ocr-clipboard-watcher
```

### 2. Create virtual environment and install dependencies

```bash
uv venv
uv pip install -r requirements.txt
```

If you're starting fresh:

```bash
uv pip install watchdog pytesseract pillow pyperclip
uv pip freeze > requirements.txt
```

---

## Run the Script (Dev Mode)

```bash
uv venv
uv pip install -r requirements.txt
python auto_ocr.py
```

Make sure your screenshots folder is set to:

```python
SCREENSHOT_DIR = r'C:\Users\<yourname>\Pictures\Screenshots'
```

---

## Build Executable (Silent Mode)

```bash
pyinstaller --noconsole --onefile auto_ocr.spec
```

This will create a standalone `auto_ocr.exe` in the `dist/` folder — double-click to run in background mode (no terminal window).

Make sure `auto_ocr.spec` includes:

* `watchdog.observers.windows` in `hiddenimports`
* `collect_submodules('watchdog')` if needed

---

## Folder Structure

```
.
├── auto_ocr.py
├── auto_ocr.spec
├── requirements.txt
└── README.md
```

---

## Troubleshooting

### Error: `ModuleNotFoundError: watchdog.observers`

**Fix**: Use `--hidden-import=watchdog.observers.windows` with PyInstaller or update your `.spec` file accordingly.

---

## License

MIT License

---

## Author

Lakshay
Built with Python, frustration, and coffee.

