import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": [], "excludes": ["tkinter", "ssl", "bz2"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="wei-dev",
    version="0.1",
    description="Wei-Dev",
    options={"build_exe": build_exe_options},
    executables=[Executable("weidev.py", base=base)]
)
