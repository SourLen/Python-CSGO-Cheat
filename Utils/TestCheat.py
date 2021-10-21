import pymem
import threading
import time
import datetime
from Utils.Offsets import *
pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll" ).lpBaseOfDll
engine = pymem.process.module_from_name(pm.process_handle, "engine.dll" ).lpBaseOfDll
entities = []
localplayer = int()
lTeam = int()
def main():
    glow_manager = pm.read_int( client + dwGlowObjectManager )

    while True:
        t1 = datetime.datetime.now()
        try:
            localPlayer = localplayer
            localPlayerTeam = lTeam

            for entity in entities:
                entity_glow = pm.read_int( entity + m_iGlowIndex )
                address_glow = glow_manager + entity_glow * 0x38 + 0x4

                # pm.write_float(glow_manager + entity_glow * 0x38 + 0x4,  float(1))
                # pm.write_float(glow_manager + entity_glow * 0x38 + 0x8,  float(0))
                # pm.write_float(glow_manager + entity_glow * 0x38 + 0xC,  float(0))
                # pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0.7))
                pm.write_bytes( address_glow,
                                b"\x00\x00\x80\x3F\x00\x00\x00\x00\x00\x00\x00\x00\x33\x33\x33\x3F", 16 )

                # print(address_glow)
                pm.write_int( glow_manager + entity_glow * 0x38 + 0x24, 1 )
        except Exception as e:
            print(e)
            pass
        t2 = datetime.datetime.now()
        print(t2 - t1)


def grabber():
    while True:
        try:
            localplayer = pm.read_int(client + dwLocalPlayer)
            lTeam = pm.read_int(localplayer + m_iTeamNum)

            for i in range(0, 32):
                entity = pm.read_int(client + dwEntityList + i * 0x10)

                if entity:
                    entity_team = pm.read_int(entity + m_iTeamNum)
                    if entity_team != lTeam:
                        if entity not in entities:
                            entities.append(entity)



        except Exception as e:
            print(e)
            pass

threading.Thread(target=grabber).start()
threading.Thread(target=main).start()