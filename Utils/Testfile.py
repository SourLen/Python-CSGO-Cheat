import pymem, datetime, time
from Utils.Offsets import *

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll" ).lpBaseOfDll
engine = pymem.process.module_from_name(pm.process_handle, "engine.dll" ).lpBaseOfDll

def main():
    for x in range(0, 100000):
        t1 = datetime.datetime.now()
        if client and engine and pm:

                player = pm.read_int( client + dwLocalPlayer )

                glow_manager = pm.read_int( client + dwGlowObjectManager )


                localTeam = pm.read_int( player + m_iTeamNum )



        for i in range( 0, 32 ):
            entity = pm.read_int( client + dwEntityList + i * 0x10 )

            if entity:
                try:
                    entity_glow = pm.read_int( entity + m_iGlowIndex )
                    entity_team_id = pm.read_int( entity + m_iTeamNum )
                    entity_isdefusing = pm.read_int( entity + m_bIsDefusing )
                    entity_hp = pm.read_int( entity + m_iHealth )
                    entity_dormant = pm.read_int( entity + m_bDormant )
                except:
                    print( "Could not load Players Infos (Should only do this once)" )
                    time.sleep( 2 )
                    continue

                if entity_hp > 50 and not entity_hp == 100:
                    r, g, b = 255, 165, 0
                elif entity_hp < 50:
                    r, g, b = 255, 0, 0
                elif entity_hp == 100 and entity_team_id == 2:
                    r, g, b = 0, 255, 0
                else:
                    r, g, b = 0, 255, 0

                if entity_team_id == 2 and (
                        localTeam != 2) and not entity_dormant:  # Terrorist Glow
                    pm.write_float( glow_manager + entity_glow * 0x38 + 0x4, float( r ) )  # R
                    pm.write_float( glow_manager + entity_glow * 0x38 + 0x8, float( g ) )  # G
                    pm.write_float( glow_manager + entity_glow * 0x38 + 0xC, float( b ) )  # B
                    pm.write_float( glow_manager + entity_glow * 0x38 + 0x10, float( 255 ) )  # A

                    pm.write_int( glow_manager + entity_glow * 0x38 + 0x24, 1 )  # Enable


                elif  entity_team_id == 3 and (
                        localTeam != 3) and not entity_dormant:  # Anti Glow
                    pm.write_float( glow_manager + entity_glow * 0x38 + 0x4, float( r ) )  # R
                    pm.write_float( glow_manager + entity_glow * 0x38 + 0x8, float( g ) )  # G
                    pm.write_float( glow_manager + entity_glow * 0x38 + 0xC, float( b ) )  # B
                    pm.write_float( glow_manager + entity_glow * 0x38 + 0x10, float( 255 ) )  # A

                    pm.write_int( glow_manager + entity_glow * 0x38 + 0x24, 1 )  # Enable
                else:
                    pass
        t2 = datetime.datetime.now()
        t = t2 - t1
        print(t)

main()
