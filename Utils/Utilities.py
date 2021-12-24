import ctypes, requests, warnings
versioncontrol = "1.0"


def GetWindowText(handle, length=100):
    user32 = ctypes.windll.user32
    window_text = ctypes.create_string_buffer(length)
    user32.GetWindowTextA(
        handle,
        ctypes.byref(window_text),
        length
    )

    return window_text.value


def GetForegroundWindow():
    user32 = ctypes.windll.user32
    return user32.GetForegroundWindow()

def update():
    raw = requests.get("https://raw.githubusercontent.com/XanOpiat/Python-CSGO-Cheat/main/Utils/Utilities.py").text
    vc = raw.splitlines()[1].split("=")[-1][2:-1]
    if vc == versioncontrol :
        print("Cheat up to date")
    else:
        warnings.warn("Cheat is not updated!")
