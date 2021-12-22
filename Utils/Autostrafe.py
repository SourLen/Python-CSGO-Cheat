
from Utils.Offsets import *

def AutoStrafe(pm, client, player, y_angle, oldviewangle):
    on_ground = pm.read_uint( player + m_fFlags )

    if player and (on_ground == 256 or on_ground == 262):

        if y_angle > oldviewangle:
            pm.write_int( client + dwForceLeft, 6 )

        elif y_angle < oldviewangle:
            pm.write_int( client + dwForceRight, 6 )

    return y_angle