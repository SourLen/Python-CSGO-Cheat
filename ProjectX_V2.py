import io
import shutil
import threading
import time
import zipfile
from random import randint

from Classes.PlayerVars import *
from Classes.Ui import *
from Classes.Vector3 import Vec3
from MatFunctions.MathPy import GetBestTarget, CalcAngle, CalcDistance
from Utils.Aimbot import shootatTarget, AimStep
from Utils.Autostrafe import AutoStrafe
from Utils.Bhop import Bhop
from Utils.Chams import Chams, ResetChams
from Utils.Triggerbot import shootTrigger
from Utils.Utilities import GetWindowText, GetForegroundWindow, update, is_pressed
from Utils.WallhackFunctions import SetEntityGlow, GetEntityVars
from Utils.rcs import rcse


def main():
    # getting handle to csgo process
    try:
        pm = pymem.Pymem("csgo.exe")
    except Exception as e:
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'Could not find the csgo.exe process !', 'Error', 16)  
        quit(0)
    # getting client and engine dll modules as well as updating netvars
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
    engine_pointer = pm.read_uint(engine + dwClientState)
    # Initialising Variable
    cham = False
    oldpunch = Vec3(0, 0, 0)
    newrcs = Vec3(0, 0, 0)
    punch = Vec3(0, 0, 0)
    rcs = Vec3(0, 0, 0)
    random = Vec3(0, 0, 0)
    fovex = False
    First = True
    first = True
    oldviewangle = 0.0
    print("DUMPING NETVARS")
    print("DUMPING OFFSETS SUCCESFUL")
    print("CHEAT STARTED")
    s = 0
    n = 0
    while True:
        time.sleep(0.005)
        try:
            if not GetWindowText(GetForegroundWindow()).decode(
                    'cp1252') == "Counter-Strike: Global Offensive - Direct3D 9":
                time.sleep(1)
                continue
            pm.write_uchar(engine + dwbSendPackets, 1)
            player = pm.read_uint(client + dwLocalPlayer)
            if client and engine and pm:
                try:  # Getting variables
                    player, engine_pointer, glow_manager, crosshairid, getcrosshairTarget, immunitygunganme,\
                    localTeam, crosshairTeam, y_angle = GetPlayerVars(pm, client, engine, engine_pointer)
                except Exception as e:
                    print("Round not started yet")
                    time.sleep(2)
                    continue

            if ui.Aimbot and is_pressed(ui.Aimbotkey) and player:  # Aimbot
                if ui.random != 0 and random.x == 0 and random.y == 0 and random.z == 0 and first:
                    random = Vec3(randint(-ui.random, ui.random), randint(-ui.random, ui.random), 0)
                target, localpos, targetpos = GetBestTarget(pm, client, engine, player, ui.spotted, ui.Baim, ui.Aimfov,
                                                            random)
                if target is not None and localpos is not None and targetpos is not None:
                    if ui.smooth and not (
                            pm.read_int(player + m_iShotsFired) > 1 and ui.AimRCS):  # If smooth and not shooting
                        localAngle = Vec3(0, 0, 0)
                        localAngle.x = pm.read_float(engine_pointer + dwClientState_ViewAngles)
                        localAngle.y = pm.read_float(engine_pointer + dwClientState_ViewAngles + 0x4)
                        localAngle.z = pm.read_float(player + m_vecViewOffset + 0x8)
                        if s <= int(n) and CalcDistance(CalcAngle(localpos, targetpos), localAngle) > 0.7:
                            n = AimStep(pm, engine_pointer, ui.sens, localpos, targetpos, localAngle, s, n)
                            s += 1
                        elif s >= int(n) or CalcDistance(CalcAngle(localpos, targetpos), localAngle):
                            s = 0
                            n = 0
                            random = Vec3(0, 0, 0)
                            first = False
                            shootatTarget(pm, client, engine, localpos, targetpos, player, engine_pointer, ui.Silentaim,
                                          ui.AimRCS, ui.Aimbotkey)
                    else:
                        shootatTarget(pm, client, engine, localpos, targetpos, player, engine_pointer, ui.Silentaim,
                                      ui.AimRCS, ui.Aimbotkey)

            if ui.Aimbot and not is_pressed(ui.Aimbotkey):  # reseting Aimbot
                s = 0
                n = 0
                first = True
                random = Vec3(0, 0, 0)

            if ui.Trigger and is_pressed(ui.Triggerkey):  # Trigger
                shootTrigger(pm, crosshairid, client, localTeam, crosshairTeam, ui.Triggerkey)

            if ui.Noflash:  # Noflash
                flash_value = player + m_flFlashMaxAlpha
                if flash_value:
                    pm.write_float(flash_value, float(0))

            if ui.RCS:  # RCS
                oldpunch = rcse(pm, player, engine_pointer, oldpunch, newrcs, punch, rcs)

            if not ui.Holdfov:  # FOV
                if ui.Togglefov and fovex:
                    fovshit = player + m_iDefaultFOV
                    pm.write_int(fovshit, ui.Fovvaluke)
                if not ui.Togglefov or not fovex:
                    fovshit = player + m_iDefaultFOV
                    pm.write_int(fovshit, 90)
                if ui.Togglefov and is_pressed(ui.Fovkey):
                    fovex = not fovex
                    time.sleep(0.25)

            if ui.Holdfov: # Holdfov
                fovshit = player + m_iDefaultFOV
                if is_pressed(ui.Fovkey):
                    pm.write_int(fovshit, ui.Fovvaluke)
                else:
                    pm.write_int(fovshit, 90)

            if ui.Bhop: # Bhop
                if is_pressed("space"):
                    Bhop(pm, client, player)

            if ui.auto_strafe and y_angle: # Autostrafe
                y_angle = AutoStrafe(pm, client, player, y_angle, oldviewangle)
                oldviewangle = y_angle

            for i in range(0, 64): # Looping through all entities
                entity = pm.read_uint(client + dwEntityList + i * 0x10)
                if entity:
                    entity_glow, entity_team_id, entity_isdefusing, entity_hp, entity_dormant = GetEntityVars(pm,
                                                                                                              entity)
                    if ui.Wallhack: #  Wallhack
                        SetEntityGlow(pm, entity_hp, entity_team_id, entity_dormant, localTeam, glow_manager,
                                      entity_glow, ui.Eteam, ui.healthbasedWH, ui.WRGB)
                    if ui.Radar: #  Radar
                        pm.write_int(entity + m_bSpotted, 1)
                    if ui.Chams: #  Chams
                        Chams(pm, engine, entity, ui.Healthbased, ui.Ergb, ui.Argb, ui.Allies, ui.Enemies,
                              entity_team_id, entity_hp, First, player)
                        First = False
                    if not ui.Chams and cham: #  Reseting Chams
                        ResetChams(pm, engine, entity, entity_team_id, player)
            # Chams variables
            if ui.Chams:
                cham = True
            elif not ui.Chams:
                cham = False
                First = True

        except Exception as e: #  Catching Exceptions
            continue


if __name__ == "__main__":
    if update(): #  Versioncontrol
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(Dialog)
        Dialog.show()
        threading.Thread(target=main).start()  # Mainthread
        sys.exit(app.exec_())
    else:
        dir = os.getcwd()
        clonedir = str(dir).split("\\")[0:-1]
        stringdir = ""
        for x in clonedir:
            stringdir += f"{x}/"
        for filename in os.listdir(dir):
            filepath = os.path.join(dir, filename)
            try:
                if os.path.isfile(filepath) or os.path.islink(filepath):
                    os.unlink(filepath)
                elif os.path.isdir(filepath):
                    shutil.rmtree(filepath, ignore_errors=True)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (filepath, e))
        r = requests.get("https://github.com/XanOpiat/Python-CSGO-Cheat/archive/refs/heads/main.zip", stream=True)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(stringdir)
else:
    print("Program Is not allowed to be ran, by other programs!")
    quit(0)
