
from MatFunctions.MathPy import *
from Utils.Offsets import *


sens = int()


def shootatTarget(pm, client, engine, localpos, targetpos, player, engine_pointer, Silent, aimrcs, aimkey):
    Unnormal = CalcAngle(localpos, targetpos)
    Normal = normalizeAngles(Unnormal)
    punchx = pm.read_float(player + m_aimPunchAngle)
    punchy = pm.read_float(player + m_aimPunchAngle + 0x4)
    if Silent:
        pm.write_uchar(engine + dwbSendPackets, 0)
        Commands = pm.read_int(client + dwInput + 0x0108)
        VerifedCommands = pm.read_int(client + dwInput + 0x010C)
        Desired = pm.read_int(engine_pointer + clientstate_last_outgoing_command) + 2
        OldUser = Commands + ((Desired - 1) % 150) * 100
        VerifedOldUser = VerifedCommands + ((Desired - 1) % 150) * 0x68
        m_buttons = pm.read_int(OldUser + 0x30)
        Net_Channel = pm.read_uint(engine_pointer + clientstate_net_channel)
        if pm.read_int(Net_Channel + 0x18) < Desired:
            pass
        elif aimrcs:
            pm.write_float(OldUser + 0x0C, Normal.x)
            pm.write_float(OldUser + 0x10, Normal.y)
            pm.write_int(OldUser + 0x30, m_buttons | (1 << 0))
            pm.write_float(VerifedOldUser + 0x0C, Normal.x - (punchx * 2))
            pm.write_float(VerifedOldUser + 0x10, Normal.y - (punchy * 2))
            pm.write_int(VerifedOldUser + 0x30, m_buttons | (1 << 0))
            pm.write_uchar(engine + dwbSendPackets, 1)
        else:
            pm.write_float(OldUser + 0x0C, Normal.x)
            pm.write_float(OldUser + 0x10, Normal.y)
            pm.write_int(OldUser + 0x30, m_buttons | (1 << 0))
            pm.write_float(VerifedOldUser + 0x0C, Normal.x)
            pm.write_float(VerifedOldUser + 0x10, Normal.y)
            pm.write_int(VerifedOldUser + 0x30, m_buttons | (1 << 0))
            pm.write_uchar(engine + dwbSendPackets, 1)
    elif aimrcs and pm.read_int(player + m_iShotsFired) > 1:
        pm.write_float(engine_pointer + dwClientState_ViewAngles, Normal.x - (punchx * 2))
        pm.write_float(engine_pointer + dwClientState_ViewAngles + 0x4,
                       Normal.y - (punchy * 2))

    else:
        pm.write_float(engine_pointer + dwClientState_ViewAngles, Normal.x)
        pm.write_float(engine_pointer + dwClientState_ViewAngles + 0x4,
                       Normal.y)


def AimStep(pm, engine_pointer, smooth, CurrLocal, CurrTarget, LocalAngle, i, n):
    AngDiff = normalizeAngles(CalcAngle(CurrLocal, CurrTarget))
    AngDiff.x = AngDiff.x - LocalAngle.x
    AngDiff.y = AngDiff.y - LocalAngle.y
    AngDiff.z = AngDiff.z - LocalAngle.z
    normalizeAngles(AngDiff)
    Dist = sqrt(AngDiff.x * AngDiff.x + AngDiff.y * AngDiff.y + AngDiff.z * AngDiff.z)
    if i == 0:
        n = Dist * smooth
    AddAngl = Vec3(AngDiff.x / (n - i), AngDiff.y / (n - i), AngDiff.z / (n - i))
    writeang = Vec3(LocalAngle.x + AddAngl.x, LocalAngle.y + AddAngl.y, 0)
    pm.write_float(engine_pointer + dwClientState_ViewAngles, writeang.x)
    pm.write_float(engine_pointer + dwClientState_ViewAngles + 0x4, writeang.y)
    return n
