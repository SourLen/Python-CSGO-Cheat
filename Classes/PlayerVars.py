from Utils.Offsets import *


def GetPlayerVars(pm, client, engine, engine_pointer):
    player = pm.read_uint(client + dwLocalPlayer)
    engine_pointer = pm.read_uint(engine + dwClientState)
    glow_manager = pm.read_uint(client + dwGlowObjectManager)
    crosshairid = pm.read_uint(player + m_iCrosshairId)
    getcrosshairtarget = pm.read_uint(client + dwEntityList + (crosshairid - 1) * 0x10)
    immunitygunganme = pm.read_uint(getcrosshairtarget + m_bGunGameImmunity)
    localteam = pm.read_uint(player + m_iTeamNum)
    crosshairteam = pm.read_uint(getcrosshairtarget + m_iTeamNum)
    y_angle = pm.read_float(engine_pointer + dwClientState_ViewAngles + 0x4)

    return player, engine_pointer, glow_manager, crosshairid, getcrosshairtarget, immunitygunganme, localteam, \
        crosshairteam, y_angle

# Cleaned most of this file,
# This file is now working.
# Last update 2022,Jan,10
