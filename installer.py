import os
import sys
import subprocess

clear = lambda: os.system('cls')

def install(package: str):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

def is_installed(package: str):
    try:
        __import__(package)
        return True
    
    except ImportError:
        return False
    
    except Exception as e:
        print(f'Unexpected error: {e} while checking if {package} is installed')
        return True

def get_pending_packages():
    pending = []
    with open('requirements.txt', 'rt') as f:
        requirements = f.read().splitlines()
        for package in requirements:
            if package and not is_installed(package):
                pending.append(package)
    return pending

def setup():
    pending = get_pending_packages()

    if not pending:
        return print('All packages are installed')

    print(f'{len(pending)} missing packages.\n\tWould you like to install them? (y/n)')

    if input().lower() == 'y':
        for package in pending:
            print(f'Installing {package}...')
            install(package)
        print('Installation complete')
    else:
        print('Installation cancelled')   

def main():
    try:
        clear()
        setup()

    except KeyboardInterrupt:
        print('Installation cancelled by user')

if __name__ == '__main__':
    main()
else:
    print("Installer is not allowed to be ran, by other programs!")
