from Utils.Offsets import *


def getClassID(pm, entity):
    buf = pm.read_int( entity + 8 )
    buf = pm.read_int( buf + 2 * 4 )
    buf = pm.read_int( buf + 1 )
    buf = pm.read_int( buf + 20 )
    return buf


def Chams(pm, engine, entity, healthbased, Ergb, Argb, Allies, Enemies, entityTeam, entityHP, first, localPlayer):
    localTeam = pm.read_int( localPlayer + m_iTeamNum )
    if entity and entity != 0:
        if getClassID( pm, entity ) == 40:

            if healthbased:
                if entityHP == 100:
                    Argb = [0, 255, 0]
                    Ergb = [0, 255, 0]
                elif entityHP > 75:
                    Argb = [0, 255, 255]
                    Ergb = [0, 255, 255]
                elif entityHP > 25:
                    Argb = [255, 165, 0]
                    Ergb = [255, 165, 0]
                else:
                    Argb = [255, 0, 0]
                    Ergb = [255, 0, 0]
            if Allies:
                if entityTeam == localTeam and entityTeam != 0 and entity != localPlayer:
                    pm.write_uchar( entity + 112, Argb[0] )
                    pm.write_uchar( entity + 113, Argb[1] )
                    pm.write_uchar( entity + 114, Argb[2] )
            elif not Allies:
                if entityTeam == localTeam and entityTeam != 0 and entity != localPlayer:
                    pm.write_uchar( entity + 112, 255 )
                    pm.write_uchar( entity + 113, 255 )
                    pm.write_uchar( entity + 114, 255 )
            if Enemies:
                if entityTeam != localTeam and entityTeam != 0 and entity != localPlayer:
                    pm.write_uchar( entity + 112, Ergb[0] )
                    pm.write_uchar( entity + 113, Ergb[1] )
                    pm.write_uchar( entity + 114, Ergb[2] )
            elif not Enemies:
                if entityTeam != localTeam and entityTeam != 0 and entity != localPlayer:
                    pm.write_uchar( entity + 112, 255 )
                    pm.write_uchar( entity + 113, 255 )
                    pm.write_uchar( entity + 114, 255 )

            if first:
                buf = 1084227584
                point = pm.read_int( engine + model_ambient - 44 )
                xored = buf ^ point
                pm.write_int( engine + model_ambient, xored )


def ResetChams(pm, engine, entity, entityTeam, localPlayer):
    if entity and entity != 0:
        if getClassID( pm, entity ) == 40:
            if entityTeam != 0 and entity != localPlayer:
                pm.write_uchar( entity + 112, 255 )
                pm.write_uchar( entity + 113, 255 )
                pm.write_uchar( entity + 114, 255 )

            b = 0
            pointer = pm.read_int(engine + model_ambient - 44)
            xo = b ^ pointer
            pm.write_int(engine + model_ambient, xo)



