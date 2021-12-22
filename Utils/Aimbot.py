import keyboard
from MatFunctions.MathPy import *
from Utils.Offsets import *



def shootatTarget(pm, client, engine, localpos, targetpos, player, engine_pointer, Silent, aimrcs, aimkey):
    Unnormal = CalcAngle( localpos, targetpos )
    Normal = normalizeAngles( Unnormal )
    punchx = pm.read_float( player + m_aimPunchAngle )
    punchy = pm.read_float( player + m_aimPunchAngle + 0x4 )
    if Silent:
        pm.write_uchar( engine + dwbSendPackets, 0 )
        Commands = pm.read_int( client + dwInput + 0x0108 )
        VerifedCommands = pm.read_int( client + dwInput + 0x010C )
        Desired = pm.read_int( engine_pointer + clientstate_last_outgoing_command ) + 2
        OldUser = Commands + ((Desired - 1) % 150) * 100
        VerifedOldUser = VerifedCommands + ((Desired - 1) % 150) * 0x68
        m_buttons = pm.read_int( OldUser + 0x30 )
        Net_Channel = pm.read_uint( engine_pointer + clientstate_net_channel )
        if pm.read_int( Net_Channel + 0x18 ) < Desired:
            pass
        elif aimrcs and keyboard.is_pressed( aimkey ):
            pm.write_float( OldUser + 0x0C, Normal.x )
            pm.write_float( OldUser + 0x10, Normal.y )
            pm.write_int( OldUser + 0x30, m_buttons | (1 << 0) )
            pm.write_float( VerifedOldUser + 0x0C, Normal.x - (punchx * 2) )
            pm.write_float( VerifedOldUser + 0x10, Normal.y - (punchy * 2) )
            pm.write_int( VerifedOldUser + 0x30, m_buttons | (1 << 0) )
            pm.write_uchar( engine + dwbSendPackets, 1 )
        elif keyboard.is_pressed( aimkey ):
            pm.write_float( OldUser + 0x0C, Normal.x )
            pm.write_float( OldUser + 0x10, Normal.y )
            pm.write_int( OldUser + 0x30, m_buttons | (1 << 0) )
            pm.write_float( VerifedOldUser + 0x0C, Normal.x )
            pm.write_float( VerifedOldUser + 0x10, Normal.y )
            pm.write_int( VerifedOldUser + 0x30, m_buttons | (1 << 0) )
            pm.write_uchar( engine + dwbSendPackets, 1 )
    elif aimrcs and pm.read_int( player + m_iShotsFired ) > 1 and keyboard.is_pressed( aimkey ):
        pm.write_float( engine_pointer + dwClientState_ViewAngles, Normal.x - (punchx * 2) )
        pm.write_float( engine_pointer + dwClientState_ViewAngles + 0x4,
                        Normal.y - (punchy * 2) )

    elif keyboard.is_pressed( aimkey ):
        pm.write_float( engine_pointer + dwClientState_ViewAngles, Normal.x )
        pm.write_float( engine_pointer + dwClientState_ViewAngles + 0x4,
                        Normal.y )