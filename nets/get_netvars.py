from nets.netvar_manager import NetvarsManager



class get_netvars():
    def __init__(self,pm):


        netvars_manager = NetvarsManager( pm )
        out_file = "./nets/netvars.json"
        if out_file:
            with open( out_file, 'w+' ) as fp:


                netvars_manager.dump_netvars(
                    fp,
                    json_format=out_file.endswith( '.json' )
                )
        else:
            netvars_manager.dump_netvars()



