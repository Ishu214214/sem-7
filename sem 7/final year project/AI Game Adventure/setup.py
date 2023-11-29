import sys
import os
from cx_Freeze import setup, Executable

# Get the path to the DLL dynamically
system32_path = os.path.join(os.environ['SystemRoot'], 'System32')
dll_path = os.path.join(system32_path, 'vcomp140.dll')


build_exe_options = {
    "packages": ["os", "cv2", "matplotlib", "pyautogui", "time", "math", "mediapipe", "speech_recognition", "pyttsx3", "nltk", "webbrowser", "queue", "gtts", "pygame"],
    "excludes": ["module_to_exclude", "another_module"],
    "include_msvcr": True,
}


base = None
if sys.platform == "win32":
    base = "Win32GUI"


setup(
    name="guifoo",
    version="0.1",
    description="My GUI application!",
    options={"build_exe": build_exe_options},
    executables=[Executable("app.py", base=base)],
)
