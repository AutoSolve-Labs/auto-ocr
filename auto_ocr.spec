# auto_ocr_dev.spec
# -*- mode: python ; coding: utf-8 -*-
import os
project_dir = os.getcwd()

tesseract_datas = [
    (os.path.join(project_dir, 'tesseract_portable', 'tesseract.exe'), 'tesseract_portable'),
    (os.path.join(project_dir, 'tesseract_portable', '*.dll'), 'tesseract_portable'),
    (os.path.join(project_dir, 'tesseract_portable', 'tessdata', '*.traineddata'), 'tesseract_portable/tessdata'),
    (os.path.join(project_dir, "config.json"), ".")
]

a = Analysis(
    ['auto_ocr.py'],
    pathex=[],
    binaries=[],
    datas=tesseract_datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,   # don’t archive, keeps unpacked pyc → faster
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='auto_ocr',
    debug=True,                 # enables faster builds + debug info
    strip=False,
    upx=False,                  # disable compression → faster builds
    console=False,               # see logs during testing
)
