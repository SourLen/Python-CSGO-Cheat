import ctypes
import requests
import pymem
import keyboard, mouse
from nets.get_netvars import *

# Cleaned all of this file,
# This file is working.
# Last update 2022,Jan,10


versioncontrol = "2.3"


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
    vc = raw.splitlines()[11].split("=")[-1][2:-1]
    if vc == versioncontrol:
        print("Cheat up to date")
        return True
    else:
        response = ctypes.windll.user32.MessageBoxW(0, "Do you want to download the latest version now?", "Cheat not updated", 0x00000004)
        if response == 6:
            return False
        elif response == 7:
            return True


def strtobool(string):
    return string.lower() in ("true", 1)


def is_key(string):
    if keyboard.is_modifier(string) or (string.isalpha() and len(string) == 1):
        return True
    else:
        return False

def is_mouse(string):
    list = ["left", "right", "middle", "wheel", "mouse4", "mouse5"]
    if string in list:
        return True
    else:
        return False

def is_pressed(key):
    if is_key(key):
        return is_pressed(key)
    elif is_mouse(key):
        if key == "mouse4":
            return mouse.is_pressed("x")
        elif key == "mouse5":
            return mouse.is_pressed("x2")
        else:
            return mouse.is_pressed(key)
    else:
        MessageBox = ctypes.windll.user32.MessageBoxW(0, "Not a valid Key", "Config Error", 0)
        return False
