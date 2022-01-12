import sys
import subprocess
import os

# Vars
missingPkgs = 0


# Cleaned most of this file,
# This file is now working.
# Last update 2022,Jan,10

def setup():
    global missingPkgs
    # Testing imports
    try:
        import pymem
        print(pymem.__name__)
    except ImportError:
        missingPkgs += 1

    try:
        import keyboard
        print(keyboard.__name__)
    except ImportError:
        missingPkgs += 1

    try:
        import PyQt5
        print(PyQt5.__name__)
    except ImportError:
        missingPkgs += 1

    try:
        import threaded
        print(threaded.__name__)
    except ImportError:
        missingPkgs += 1

    try:
        import requests
        print(requests.__name__)
    except ImportError:
        missingPkgs += 1

    try:
        import mouse
        print(mouse.__name__)
    except ImportError:
        missingPkgs += 1

    # Ask to install missing packages!
    if missingPkgs == 0:
        os.system("cls")
        print("You already installed the required packages!")
        quit(0)
    else:
        os.system("cls")
        print(f"You are missing [{missingPkgs}] packages! \n\tWould you like to install them? \n\t(Y/N)")
        installSTR = str(input("Install? > "))
        if installSTR.lower() == "y":
            os.system("cls")
            try:
                import pymem
            except ImportError:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pymem'])
            try:
                import keyboard
            except ImportError:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'keyboard'])
            try:
                import PyQt5
            except ImportError:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'PyQt5'])
            try:
                import threaded
            except ImportError:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'threaded'])
            try:
                import requests
            except ImportError:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
            try:
                import mouse
            except ImportError:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'mouse'])
            os.system("cls")
            print("Finished installing packages!")
            quit(0)
        elif installSTR.lower() == "n":
            os.system("cls")
            print("Process aborted!")
            quit(0)
        else:
            os.system("cls")
            print("Process aborted! \n\t(Y/N) Y = Yes | N = No")
            quit(0)


if __name__ == '__main__':
    setup()
else:
    print("Installer Is not allowed to be ran, by other programs!")
    quit(0)
