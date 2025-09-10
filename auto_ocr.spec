# -*- mode: python ; coding: utf-8 -*-

import os
from PyInstaller.utils.hooks import collect_data_files
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
    noarchive=False,
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
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # True if you want to see logs in a terminal
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
