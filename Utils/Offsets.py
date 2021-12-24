import json, pymem, re, requests
file = "./nets/netvars.json"
f = open(file, "r")

response = json.load(f)


m_iCompetitiveWins = int(response["DT_CSPlayerResource"]["m_iCompetitiveWins"])
m_iTeamNum = int(response["DT_BaseEntity"]["m_iTeamNum"])
m_fFlags = int(response["DT_BasePlayer"]["m_fFlags"])
m_flFlashMaxAlpha = int(response["DT_CSPlayer"]["m_flFlashMaxAlpha"])
m_iDefaultFOV = int(response["DT_BasePlayer"]["m_iDefaultFOV"])
m_bGunGameImmunity = int(response["DT_CSPlayer"]["m_bGunGameImmunity"])
m_iHealth = int(response["DT_BasePlayer"]["m_iHealth"])
m_vecOrigin = int(response["DT_BaseEntity"]["m_vecOrigin"])
m_iGlowIndex = int(response["DT_CSPlayer"]["m_flFlashDuration"]) + 24
m_iCrosshairId = int(response["DT_CSPlayer"]["m_bHasDefuser"]) + 92
m_dwBoneMatrix = int(response["DT_BaseAnimating"]["m_nForceBone"]) + 28
m_vecViewOffset = int(response["DT_LocalPlayerExclusive"]["m_vecViewOffset[0]"])
m_bSpotted = int(response["DT_BaseEntity"]["m_bSpotted"])
m_iShotsFired = int(response["DT_CSLocalPlayerExclusive"]["m_iShotsFired"])
m_aimPunchAngle = int(response["DT_Local"]["m_aimPunchAngle"]) + 12236
m_bIsDefusing = int(response["DT_CSPlayer"]["m_bIsDefusing"])
m_iCompetitiveRanking = int(response["DT_CSPlayerResource"]["m_iCompetitiveRanking"])
m_bSpottedByMask = int(response["DT_BaseEntity"]["m_bSpottedByMask"])

f.close()


def get_sig( pm, modulename, pattern, extra=0, offset=0,
            relative=True):  # Get_Sig Function that will let us pattern scan for offsets
    if offset == 0:  # very wierd shit happening with the dwbSendPacketsOffset :)
        module = pymem.process.module_from_name( pm.process_handle, modulename )
        bytes = pm.read_bytes( module.lpBaseOfDll, module.SizeOfImage )
        match = re.search( pattern, bytes ).start()
        res = match + extra
        return res
    module = pymem.process.module_from_name( pm.process_handle, modulename )
    bytes = pm.read_bytes( module.lpBaseOfDll, module.SizeOfImage )
    match = re.search( pattern, bytes ).start()
    non_relative = pm.read_int( module.lpBaseOfDll + match + offset ) + extra
    yes_relative = pm.read_int( module.lpBaseOfDll + match + offset ) + extra - module.lpBaseOfDll
    return "0x{:X}".format( yes_relative ) if relative else "0x{:X}".format( non_relative )
PatternDict = {}
def transform_patterns():#unfinished

    response = requests.get("https://raw.githubusercontent.com/frk1/hazedumper/master/config.json").json()
    for struct in response["signatures"]:
        old = str(struct["pattern"])
        new = old.replace("?", ".")
        new = new.split(" ")
        newone = ""
        for element in new:
            if element != ".":
                element = r'\x'+element
            newone = newone + element
        PatternDict[struct["name"]] = newone




transform_patterns()#not ready yet

pm1 = pymem.Pymem("csgo.exe")
dwLocalPlayer = get_sig( pm1, "client.dll",
                         bytes(PatternDict["dwLocalPlayer"], encoding="raw_unicode_escape"), 4, 3 )
dwLocalPlayer = int( dwLocalPlayer, 0 )
dwEntityList = get_sig( pm1, "client.dll",bytes(PatternDict["dwEntityList"], encoding="raw_unicode_escape"), 0, 1 )
dwEntityList = int( dwEntityList, 0 )
dwGlowObjectManager = get_sig( pm1, "client.dll", bytes(PatternDict["dwGlowObjectManager"], encoding="raw_unicode_escape"), 4, 1 )
dwGlowObjectManager = int( dwGlowObjectManager, 0 )
dwForceJump = get_sig( pm1, "client.dll", bytes(PatternDict["dwForceJump"], encoding="raw_unicode_escape"), 0, 2 )
dwForceJump = int( dwForceJump, 0 )
dwForceAttack = get_sig( pm1, "client.dll", bytes(PatternDict["dwForceAttack"], encoding="raw_unicode_escape"), 0, 2 )
dwForceAttack = int( dwForceAttack, 0 )
dwClientState = get_sig( pm1, "engine.dll", bytes(PatternDict["dwClientState"], encoding="raw_unicode_escape"), 0, 1 )
dwClientState = int( dwClientState, 0 )
dwViewMatrix = get_sig( pm1, "client.dll", bytes(PatternDict["dwViewMatrix"], encoding="raw_unicode_escape"), 176, 3 )
dwViewMatrix = int( dwViewMatrix, 0 )

#dwClientState_ViewAngles = get_sig(pm1, "engine.dll", rb"\xF3\x0F\x11\x86....\xF3\x0F\x10\x44\x24\.\xF3\x0F\x11\x86", 0, 4, False)
#print(dwClientState_ViewAngles)
dwClientState_ViewAngles = 19856
dwbSendPackets = get_sig( pm1, "engine.dll",
                          bytes(PatternDict["dwbSendPackets"], encoding="raw_unicode_escape"),
                          1)

dwInput = get_sig( pm1, "client.dll",bytes(PatternDict["dwInput"], encoding="raw_unicode_escape"), 0, 1 )
dwInput = int( dwInput, 0 )
clientstate_net_channel = get_sig( pm1, "engine.dll", bytes(PatternDict["clientstate_net_channel"], encoding="raw_unicode_escape"), 0, 2, False )
clientstate_net_channel = int( clientstate_net_channel, 0 )
clientstate_last_outgoing_command = get_sig( pm1, "engine.dll", bytes(PatternDict["clientstate_last_outgoing_command"], encoding="raw_unicode_escape"), 0, 2,
                                              False )
clientstate_last_outgoing_command = int( clientstate_last_outgoing_command, 0 )
m_bDormant = get_sig( pm1, "client.dll", bytes(PatternDict["m_bDormant"], encoding="raw_unicode_escape"), 8, 2, False )
m_bDormant = int( m_bDormant, 0 )
dwClientState_PlayerInfo = get_sig( pm1, "engine.dll", bytes(PatternDict["dwClientState_PlayerInfo"], encoding="raw_unicode_escape"), 0, 2,
                                         False )
dwClientState_PlayerInfo = int( dwClientState_PlayerInfo, 0 )
dwPlayerResource = get_sig( pm1, "client.dll", bytes(PatternDict["dwPlayerResource"], encoding="raw_unicode_escape"), 0, 2 )
dwPlayerResource = int( dwPlayerResource, 0 )
dwClientState_GetLocalPlayer = get_sig( pm1, "engine.dll", bytes(PatternDict["dwClientState_GetLocalPlayer"], encoding="raw_unicode_escape"), 0, 2, False )
dwClientState_GetLocalPlayer = int( dwClientState_GetLocalPlayer, 0 )
dwForceLeft = get_sig( pm1, "client.dll", bytes(PatternDict["dwForceLeft"], encoding="raw_unicode_escape"), 0, 465 )
dwForceLeft = int( dwForceLeft, 0 )
dwForceRight = get_sig( pm1, "client.dll", bytes(PatternDict["dwForceRight"], encoding="raw_unicode_escape"), 0, 512 )
dwForceRight = int( dwForceRight, 0 )

model_ambient = get_sig(pm1, "engine.dll", bytes(PatternDict["model_ambient_min"], encoding="raw_unicode_escape"), 0, 4)
model_ambient = int(model_ambient, 0)

pm1.close_process()



