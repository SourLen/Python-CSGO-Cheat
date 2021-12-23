import ctypes, requests, warnings
from Classes.Vector3 import Vec3

versioncontrol = "1.0"
cham = False
oldpunch = Vec3(0,0,0)
newrcs = Vec3( 0, 0, 0 )
punch = Vec3( 0, 0, 0 )
rcs = Vec3( 0, 0, 0 )
fovex = False
First = True
oldviewangle = 0.0
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
    vc = raw.splitlines()[1]
    if vc == versioncontrol:
        print("Cheat up to date")
    else:
        warnings.warn("Cheat is not updated!")
