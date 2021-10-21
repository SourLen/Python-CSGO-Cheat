import re
import io
import os
import psutil
import time
def getSkinIDs():
    # Point the script to your CSGO folder and it will get up to date skin IDs and names and output to item_index.txt
    SteamPath = ""
    for process in psutil.process_iter():
        try:
            if process.name() == "csgo.exe":
                SteamPath = process.cwd()
        except:
            pass
    if SteamPath == "":
        print("csgo.exe couldnt be found, make sure to start your game before running the cheat")
        print("Closing program in 5 seconds")
        time.sleep(4.9)
        quit()


    skindata = {}
    with open( os.path.join( SteamPath, 'csgo/scripts/items/items_game.txt' ), 'r' ) as itemfile:
        start = False
        count = 0
        currnum = None

        for line in itemfile.readlines():
            if start:
                number = False
                tempdata = {}

                if re.match( r'^"\d*"$', line.strip() ):
                    currnum = int( line.strip().replace( '"', '' ) )
                    skindata[currnum] = {}
                    number = True

                if '{' in line:
                    count += 1
                if '}' in line:
                    count -= 1

                if count == 0:
                    start = False
                    continue

                if line.strip() == '{' or line.strip() == '}':
                    continue

                if currnum and not number:
                    try:
                        first, second = line.strip().replace( '"', '' ).split( '\t\t' )
                        skindata[currnum][first] = second
                    except ValueError as e:

                        pass

            if line.strip() == '"paint_kits"':
                start = True

        skindata.pop( 0 )
        skindata.pop( 9001 )

    namedata = {}
    with io.open( os.path.join( SteamPath, 'csgo/resource/csgo_english.txt' ), 'r',
                  encoding='utf-16-le' ) as languagefile:
        # Steam language files are encoded in utf-16LE
        start = False
        count = 0
        currnum = None

        for line in languagefile.readlines():
            if line.strip() == '//Recipes':
                start = False
                break

            if start:
                if line.strip().startswith( '"Paint' ):
                    tag, name = re.split( r'"\s+"', line.strip() )

                    if 'tag' in tag.lower():
                        namedata['#' + tag.replace( '"', '' ).lower()] = name.replace( '"', '' )

            if line.strip() == '// Paint Kits':
                start = True

    with io.open( 'item_index.txt', 'w', encoding="utf-8" ) as outfile:
        for n in sorted( skindata ):
            tag = skindata[n]['description_tag']

            outfile.write( "%s: %s\n" % (n, namedata[tag.lower()]) )

    with open( 'item_index.txt', 'r', encoding="utf-8" ) as f:
        skin_dict = {}
        skin_dict["Original"] = "0"
        skin_list = []

        for line in f:
            id_, skin_name = line.split( ":" )
            skin_name = skin_name.replace( "\n", "" )
            skin_name = skin_name[1:]

            i = 1
            while skin_name in skin_list:
                if "#" in skin_name:
                    skin_name = skin_name.replace( " #", "" )
                    skin_name = skin_name[:-1]

                skin_name = skin_name + " #" + str( i )
                i = i + 1

            skin_list.append( skin_name )
            skin_dict[skin_name] = id_

    os.system( "del item_index.txt" )

    with open("./skins.txt", "w+", encoding= "utf-8") as f:

        for x in sorted(skin_dict.keys()):
            try:
                f.write(x + ": " + skin_dict[x] + "\n")
            except:
                print(x)
    sort_dict = dict()
    for y in sorted(skin_dict.keys()):
        sort_dict[y]  = skin_dict[y]
    skin_list = sorted(skin_list, key=str.lower)
    return sort_dict, ["Original"] + skin_list


