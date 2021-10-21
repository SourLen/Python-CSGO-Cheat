import re
import sys
import json
from typing import Union
from pymem.process import module_from_name
from nets.recv_classes import ClientClass

__all__ = ['NetvarsManager']


class NetvarsManager:
    def __init__(self, pm):
        """Creates a new NetvarManager and dumps the netvars.

        :param csgo_handle: Handle of the csgo.exe process.
        :type csgo_handle: `pymem.Pymem`
        """
        client_handle = module_from_name(
            pm.process_handle, 'client.dll'
        )
        client_bytes = pm.read_bytes(
            client_handle.lpBaseOfDll, client_handle.SizeOfImage
        )
        world_decal = re.search( rb'DT_TEWorldDecal', client_bytes ).start()
        world_decal += client_handle.lpBaseOfDll
        all_classes = pm.read_int( client_bytes.find(
            world_decal.to_bytes( 4, 'little' )
        ) + 0x2B + client_handle.lpBaseOfDll )
        self._client_classes = all_classes
        self._handle = pm
        self._netvars_dict = dict()
        self._dump_netvars_internal()

    def get_netvar(
            self,
            table_name: str,
            prop_name: str
    ) -> Union[int, None]:
        """Returns netvar's offset by the given data. If can't find a netvar
        then returns None.

        :param table_name: Name of the table where is a prop placed in.
        :param prop_name: Name of the prop you want to get.
        :return: Prop's offset.
        """
        return self._netvars_dict.get( table_name, dict() ).get( prop_name )

    def dump_netvars(self, out_file=sys.stdout, json_format=False) -> None:
        """Dumps netvars, in a plain or json format. If you want to save dump
        into a file then you should pass a file-like object to `out_file`
        argument.

        :param out_file: File (or stdout) where we should save the dump.
        :param json_format: If you need to save the dump in a json format.
        """
        if json_format:

            out_file.write( json.dumps( self._netvars_dict, indent=4 ) )
            return
        for table in self._netvars_dict.keys():
            out_file.write( table + '\n' )
            max_name_len = len( sorted(
                self._netvars_dict[table].keys(), reverse=True,
                key=lambda x: len( x )
            )[0] )
            for table_name, prop_offset in self._netvars_dict[table].items():
                out_file.write( '\t{0:<{1}} 0x{2:08x}\n'.format(
                    table_name, max_name_len, prop_offset
                ) )

    def _dump_table(self, table) -> None:
        table_name = table.get_table_name()
        for i in range( table.get_max_props() ):
            prop = table.get_prop( i )
            prop_name = prop.get_name()
            if prop_name.isnumeric():  # Some shitty prop.
                continue
            prop_offest = prop.get_offset()
            table_existed_data = self._netvars_dict.get( table_name, dict() )
            table_existed_data.update( {prop_name: prop_offest} )
            self._netvars_dict.update(
                {table_name: table_existed_data}
            )
            try:
                data_table = prop.get_data_table()
                if not data_table:
                    continue
            except Exception:
                continue
            else:
                try:
                    self._dump_table( data_table )
                except Exception:
                    continue

    def _dump_netvars_internal(self) -> None:
        client_class = ClientClass(
            self._handle.read_int( self._client_classes + 0x10 ),
            self._handle
        )
        while client_class is not None:
            try:
                table = client_class.get_table()
                table_name = table.get_table_name()
                if not table_name:
                    break
            except Exception:
                break
            self._dump_table( table )
            client_class = client_class.get_next_class()