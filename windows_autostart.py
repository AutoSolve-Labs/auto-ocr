import os
import shutil
from pathlib import Path

exe_path = Path("dist/autoOcr.exe").resolve()
startup_dir = Path(os.environ["APPDATA"]) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"

shutil.copy(exe_path, startup_dir / exe_path.name)
