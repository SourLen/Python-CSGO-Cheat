import pymem
import re

def get_sig(pm,modulename, pattern, extra = 0, offset = 0, relative = True): #Get_Sig Function that will let us pattern scan for offsets
    if pattern == rb"\xB3\x01\x8B\x01\x8B\x40\x10\xFF\xD0\x84\xC0\x74\x0F\x80\xBF.....\x0F\x84": #very wierd shit happening with the dwbSendPacketsOffset :)
        module = pymem.process.module_from_name( pm.process_handle, modulename )
        bytes = pm.read_bytes( module.lpBaseOfDll, module.SizeOfImage )
        match = re.search( pattern, bytes ).start()
        res = match + extra
        return res
    module = pymem.process.module_from_name(pm.process_handle, modulename)
    bytes = pm.read_bytes(module.lpBaseOfDll, module.SizeOfImage)
    match = re.search(pattern, bytes).start()
    non_relative = pm.read_int(module.lpBaseOfDll + match + offset) + extra
    yes_relative = pm.read_int(module.lpBaseOfDll + match + offset) + extra - module.lpBaseOfDll
    return "0x{:X}".format(yes_relative) if relative else "0x{:X}".format(non_relative)

def dumpoffsets(pm):
    """todo: is open check"""

    if pm:


        dwbSendPackets = get_sig(pm, "engine.dll", rb"\xB3\x01\x8B\x01\x8B\x40\x10\xFF\xD0\x84\xC0\x74\x0F\x80\xBF.....\x0F\x84", 1)
        print( dwbSendPackets )
        dwbSendPackets = dwbSendPackets.replace("-","")
        dwbSendPackets = "-" + dwbSendPackets

        dwbSendPackets = int(dwbSendPackets, 0)

        print( dwbSendPackets )

pm = pymem.Pymem("csgo.exe")
dumpoffsets(pm)



