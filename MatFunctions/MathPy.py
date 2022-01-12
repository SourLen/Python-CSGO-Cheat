from math import *
from Classes.Vector3 import Vec3
from Utils.Offsets import *

# Cleaned most of this file,
# This file is working.
# Last update 2022,Jan,10


def checkangles(x, y):
    if x > 89:
        return False
    elif x < -89:
        return False
    elif y > 360:
        return False
    elif y < -360:
        return False
    else:
        return True


def nanchecker(first, second):
    if isnan(first) or isnan(second):
        return False
    else:
        return True


def normalizeAngles(angle: Vec3):
    if angle.x > 89:
        angle.x -= 360
    elif angle.x < -89:
        angle.x += 360
    if angle.y > 180:
        angle.y -= 360
    elif angle.y < -180:
        angle.y += 360
    return angle


def CalcAngle(local: Vec3, enemy: Vec3):
    delta = Vec3(0, 0, 0)
    delta.x = local.x - enemy.x
    delta.y = local.y - enemy.y
    delta.z = local.z - enemy.z

    hyp = sqrt(delta.x * delta.x + delta.y * delta.y + delta.z * delta.z)
    new = Vec3(0, 0, 0)
    new.x = asin(delta.z / hyp) * 57.295779513082
    new.y = atan(delta.y / delta.x) * 57.295779513082

    if delta.x >= 0.0:
        new.y += 180.0

    return new


def CalcDistance(current: Vec3, new: Vec3):
    distance = Vec3(0, 0, 0)

    distance.x = new.x - current.x

    if distance.x < -89:
        distance.x += 360
    elif distance.x > 89:
        distance.x -= 360
    if distance.x < 0.0:
        distance.x = -distance.x

    distance.y = new.y - current.y
    if distance.y < - 180:
        distance.y += 360
    elif distance.y > 180:
        distance.y -= 360
    if distance.y < 0.0:
        distance.y = -distance.y

    mag = sqrt(distance.x * distance.x + distance.y * distance.y)
    return mag


def checkindex(pm, engine):
    clientstate = pm.read_uint(engine + dwClientState)
    id = pm.read_uint(clientstate + dwClientState_GetLocalPlayer)
    return id


def GetBestTarget(pm, client, engine, localPlayer, spotted, baim, aimfov, random):
    while True:
        olddist = 111111111
        newdist = 0
        target = None
        PlayerID = checkindex(pm, engine)
        player_team = pm.read_int(localPlayer + m_iTeamNum)
        engine_pointer = pm.read_uint(engine + dwClientState)
        for i in range(1, 32):
            entity = pm.read_uint(client + dwEntityList + i * 0x10)

            if entity and entity != localPlayer:
                entity_hp = pm.read_uint(entity + m_iHealth)
                entity_dormant = pm.read_uint(entity + m_bDormant)
                entity_team = pm.read_uint(entity + m_iTeamNum)
                if spotted:
                    Entspotted = pm.read_uint(entity + m_bSpottedByMask)
                else:
                    Entspotted = True

                if entity_hp > 0 and not entity_dormant and Entspotted and entity_team != player_team:
                    localAngle = Vec3(0, 0, 0)
                    localAngle.x = pm.read_float(engine_pointer + dwClientState_ViewAngles)
                    localAngle.y = pm.read_float(engine_pointer + dwClientState_ViewAngles + 0x4)
                    localAngle.z = pm.read_float(localPlayer + m_vecViewOffset + 0x8)

                    localpos = Vec3(0, 0, 0)
                    localpos.x = pm.read_float(localPlayer + m_vecOrigin)

                    localpos.y = pm.read_float(localPlayer + m_vecOrigin + 4)
                    localpos.z = pm.read_float(localPlayer + m_vecOrigin + 8) + localAngle.z
                    entity_bone = pm.read_uint(entity + m_dwBoneMatrix)
                    entitypos = Vec3(0, 0, 0)
                    if baim is True:
                        entitypos.x = pm.read_float(entity_bone + 0x30 * 5 + 0xC) + random.x
                        entitypos.y = pm.read_float(entity_bone + 0x30 * 5 + 0x1C) + random.y
                        entitypos.z = pm.read_float(entity_bone + 0x30 * 5 + 0x2C) + random.z
                    else:
                        entitypos.x = pm.read_float(entity_bone + 0x30 * 8 + 0xC) + random.x
                        entitypos.y = pm.read_float(entity_bone + 0x30 * 8 + 0x1C) + random.y
                        entitypos.z = pm.read_float(entity_bone + 0x30 * 8 + 0x2C) + random.z
                    new = CalcAngle(localpos, entitypos)

                    newdist = CalcDistance(localAngle, new)

                    if newdist < olddist and newdist < aimfov:
                        olddist = newdist
                        target = entity
                        targetpos = entitypos
        if target is not None:
            return target, localpos, targetpos
        else:
            return None, None, None


def smoothing(t):
    return t * t * (3.0 - 2.0 * t)
