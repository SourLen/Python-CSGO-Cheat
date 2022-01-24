import keyboard
from Utils.Offsets import *
from Utils.Utilities import is_pressed
# Cleaned all of this file,
# This file is working.
# Last update 2022,Jan,10


def shootTrigger(pm, CrossID, client, lTeam, CTeam, triggerkey):
    if is_pressed(triggerkey) and 0 < CrossID < 64 and lTeam != CTeam:
        pm.write_int(client + dwForceAttack, 6)
