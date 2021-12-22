from Utils.Offsets import *

def Bhop(pm, client, player):
    force_jump = client + dwForceJump
    on_ground = pm.read_uint( player + m_fFlags )
    if player and on_ground == 257 or on_ground == 263:
        pm.write_int( force_jump, 6 )

