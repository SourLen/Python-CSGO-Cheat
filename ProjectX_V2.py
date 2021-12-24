import pymem
from nets.get_netvars import *
from Utils.Bhop import *
from Utils.Aimbot import *
from Utils.Autostrafe import *
from Utils.Triggerbot import *
from Classes.PlayerVars import *
from Utils.rcs import *
from Utils.Chams import Chams, ResetChams
import threading
from Utils.WallhackFunctions import *
from Classes.Ui1 import *
from Utils.Utilities import *



def main():

    try:
        pm = pymem.Pymem("csgo.exe")
    except:
        print("CSGO not open, closing cheat")
        exit()
    gn = get_netvars(pm)
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
    engine_pointer = pm.read_uint( engine + dwClientState )
    cham = False
    oldpunch = Vec3(0, 0, 0)
    newrcs = Vec3(0, 0, 0)
    punch = Vec3(0, 0, 0)
    rcs = Vec3(0, 0, 0)
    fovex = False
    First = True
    oldviewangle = 0.0
    print("DUMPING NETVARS")
    print("DUMPING OFFSETS SUCCESFUL")
    print("CHEAT STARTED")
    while True:
        try:
            if not GetWindowText( GetForegroundWindow() ).decode( 'cp1252' ) == "Counter-Strike: Global Offensive - Direct3D 9":
                time.sleep( 1 )
                continue

            pm.write_uchar( engine + dwbSendPackets, 1 )
            player = pm.read_uint(client + dwLocalPlayer)

            if client and engine and pm:
                try:
                    player, engine_pointer, glow_manager, crosshairID, getcrosshairTarget,immunitygunganme, localTeam, crosshairTeam, y_angle = GetPlayerVars(pm, client, engine, engine_pointer, player)
                except:
                    print("Round not started yet")
                    time.sleep(5)
                    continue
            if ui.Aimbot and keyboard.is_pressed(ui.Aimbotkey) and player:
                target, localpos, targetpos = GetBestTarget(pm, client, engine, player, ui.spotted, ui.Baim, ui.Aimfov)
                if target is not None and localpos is not None and targetpos is not None:
                    shootatTarget(pm,client,engine,localpos,targetpos,player,engine_pointer, ui.Silentaim, ui.AimRCS, ui.Aimbotkey)

            if ui.Trigger:
                shootTrigger(pm, crosshairID, client, localTeam, crosshairTeam, ui.Triggerkey)
            if ui.Noflash:
                flash_value = player + m_flFlashMaxAlpha
                if flash_value:
                    pm.write_float( flash_value, float( 0 ) )
            if ui.RCS:
                oldpunch = rcse(pm,player,engine_pointer,oldpunch, newrcs, punch, rcs)

            if not ui.Holdfov:
                if ui.Togglefov and fovex:
                    fovshit = player + m_iDefaultFOV
                    pm.write_int( fovshit, ui.Fovvaluke )
                if not ui.Togglefov or not fovex:
                    fovshit = player + m_iDefaultFOV
                    pm.write_int( fovshit, 90 )
                if ui.Togglefov and keyboard.is_pressed(ui.Fovkey):
                    fovex = not fovex
                    time.sleep(0.25)

            if ui.Holdfov:
                fovshit = player + m_iDefaultFOV
                if keyboard.is_pressed(ui.Fovkey):
                    pm.write_int( fovshit, ui.Fovvaluke )
                else:
                    pm.write_int( fovshit, 90)

            if ui.Bhop:
                if keyboard.is_pressed("space"):
                    Bhop(pm, client, player)

            if ui.auto_strafe and y_angle:
                y_angle = AutoStrafe(pm,client,player,y_angle,oldviewangle)

                oldviewangle = y_angle

            for i in range( 0, 64 ):
                entity = pm.read_uint( client + dwEntityList + i * 0x10 )

                if entity:
                    entity_glow, entity_team_id, entity_isdefusing, entity_hp, entity_dormant = GetEntityVars(pm, entity)
                    if ui.Wallhack:

                        SetEntityGlow(pm, entity_hp, entity_team_id, entity_dormant, localTeam, glow_manager, entity_glow, ui.Eteam)

                    if ui.Radar:
                        pm.write_int(entity + m_bSpotted, 1)
                    if ui.Chams:
                        Chams(pm, engine, entity, ui.Healthbased, ui.Ergb, ui. Argb, ui.Allies, ui.Enemies, entity_team_id, entity_hp, First, player)
                        First = False

                    if not ui.Chams and cham:
                        ResetChams(pm, engine, entity, entity_team_id, player)

            if ui.Chams:
                cham = True
            elif not ui.Chams:
                cham = False
                First = True

        except Exception as e:
            continue



if __name__ == "__main__":
    update()
    import sys
    app = QtWidgets.QApplication( sys.argv )
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi( Dialog )
    Dialog.show()
    threading.Thread(target=main).start()
    sys.exit( app.exec_() )


