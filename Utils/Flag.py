import pymem
import datetime
from Utils.Offsets import *
print(dwbSendPackets)
import time
pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name( pm.process_handle, "client.dll" ).lpBaseOfDll
engine = pymem.process.module_from_name( pm.process_handle, "engine.dll" ).lpBaseOfDll
def main():
    print(dwbSendPackets)
    while True:

        if True:
            pm.write_uchar( engine + dwbSendPackets, 0 )
            time.sleep( 0.7 )
        pm.write_uchar(engine + dwbSendPackets, 1)




main()
