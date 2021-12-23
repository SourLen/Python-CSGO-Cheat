from Utils.Offsets import *



def GetPlayerVars(pm, client, engine, engine_pointer, player):
    player = pm.read_uint( client + dwLocalPlayer )
    engine_pointer = pm.read_uint( engine + dwClientState )
    glow_manager = pm.read_uint( client + dwGlowObjectManager )
    crosshairID = pm.read_uint( player + m_iCrosshairId )
    getcrosshairTarget = pm.read_uint( client + dwEntityList + (crosshairID - 1) * 0x10 )
    immunitygunganme = pm.read_uint( getcrosshairTarget + m_bGunGameImmunity )
    localTeam = pm.read_uint( player + m_iTeamNum )
    crosshairTeam = pm.read_uint( getcrosshairTarget + m_iTeamNum )
    y_angle = pm.read_float( engine_pointer + dwClientState_ViewAngles + 0x4 )

    return player, engine_pointer, glow_manager, crosshairID, getcrosshairTarget,immunitygunganme, localTeam, crosshairTeam, y_angle
