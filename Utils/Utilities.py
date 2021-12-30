import ctypes, requests, warnings, pymem
from nets.get_netvars import *

versioncontrol = "2.0"


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
    gn = get_netvars(pymem.Pymem("csgo.exe"))
    raw = requests.get("https://raw.githubusercontent.com/XanOpiat/Python-CSGO-Cheat/main/Utils/Utilities.py").text
    vc = raw.splitlines()[3].split("=")[-1][2:-1]
    if vc == versioncontrol:
        print("Cheat up to date")
        return True
    else:
        response = ctypes.windll.user32.MessageBoxW(0,"Do you want to download the latest version now?", "Cheat not updated", 0x00000004)
        if response == 6:
            return False
        elif response == 7:
            return True


def strtobool(string):
    return string.lower() in ("true", 1)
