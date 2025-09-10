# Auto-OCR

## Problem Statement

Extracting text from images often requires manually uploading screenshots to external tools (like Gemini or other OCR services). This is slow and inconvenient.

**Auto-OCR** solves this by running locally on your system. It automatically captures text from screenshots and copies it to your clipboard within seconds—no need to manually upload files or download large models.

---

## Key Features

* **No extra downloads**: The OCR model is bundled with the `.exe` file.
* **Auto-start**: Can be placed in `shell:startup` so it runs automatically when your computer boots.
* **Screenshot detection**: Whenever you take a screenshot, Auto-OCR extracts the text and copies it to your clipboard.
* **Multi-language support**: Supports 30+ languages.
* **Fast**: Reduces OCR workflow from minutes to seconds.

---

## Installation & Setup

### Step 0: Clone the repo
```bash
git clone https://github.com/AutoSolve-Labs/auto-ocr.git
cd .\auto-ocr\
```

### Step 1: Install Python

If Python is not installed, download and install it from [python.org](https://www.python.org/downloads/).

### Step 2: Create a Virtual Environment and Install Dependencies
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
#### Linux Clipboard Note
On Linux, pyperclip requires an external clipboard utility. Install one of these:

```bash
sudo apt install xclip     # Option 1
sudo apt install xsel 
```


### Step 3: Configure OCR

Run the CLI to set up your preferred language and screenshot folder:

```bash
python cli.py
```

* It will ask which language you want to use (30+ supported).
* It will ask for the screenshot folder path.

  * On **Windows 11**: Open File Explorer → `Pictures` → `Screenshots` → copy the folder path.
  * On other OS, the screenshot folder may differ.

### Step 4: Build Executable

```bash
python -m PyInstaller --clean auto_ocr.spec
```

### Step 5: Run the Executable

From the `dist` folder, either:

```bash
.\auto_ocr.exe      # Windows
./auto_ocr          # Linux/macOS
```

or simply double-click the file.

Now, whenever you take a screenshot, extracted text will be automatically copied to your clipboard.

### Step 6: Enable Auto-Start (Optional)

To make Auto-OCR run automatically when your PC starts:

* Move the executable to the Windows Startup folder (`shell:startup`), or
* Run:

```bash
python windows_autostart.py
```

---

## Example Workflow

1. Take a screenshot.
2. Auto-OCR detects it instantly.
3. Extracted text is available in your clipboard.
4. Paste anywhere—ready to use.

