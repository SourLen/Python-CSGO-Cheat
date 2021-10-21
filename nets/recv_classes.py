import re
import sys
import json
from typing import Union
from pymem.process import module_from_name

__all__ = ['RecvTable', 'RecvProp', 'ClientClass']


class RecvProp:
    def __init__(self, start_addr, handle):
        self._start_addr = start_addr
        self._handle = handle

    def get_name(self) -> str:
        """Returns a name of the prop."""
        name_addr = self._handle.read_int( self._start_addr )
        return self._handle.read_string( name_addr, 128 )

    def get_offset(self) -> int:
        """Returns an offset of the prop."""
        return self._handle.read_int( self._start_addr + 0x2C )

    def get_data_table(self) -> "RecvTable":
        """Returns a data table for the prop."""
        return RecvTable(
            self._handle.read_int( self._start_addr + 0x28 ),
            self._handle
        )


class RecvTable:
    def __init__(self, start_addr, handle):
        self._start_addr = start_addr
        self._handle = handle

    def get_table_name(self) -> str:
        """Returns a table's name."""
        name_addr = self._handle.read_int( self._start_addr + 0xC )
        return self._handle.read_string( name_addr, 128 )

    def get_max_props(self) -> int:
        """Returns prop's count in a table."""
        return self._handle.read_int( self._start_addr + 0x4 )

    def get_prop(self, index):
        """Returns prop by the given index."""
        props_addr = self._handle.read_int( self._start_addr )
        prop_addr = props_addr + 0x3C * index
        if not prop_addr:
            return None
        return RecvProp( prop_addr, self._handle )


class ClientClass:
    def __init__(self, start_addr, handle):
        self._start_addr = start_addr
        self._handle = handle

    def get_next_class(self) -> "ClientClass":
        """Returns next client class."""
        return self.__class__(
            self._handle.read_int( self._start_addr + 0x10 ),
            self._handle
        )

    def get_table(self) -> RecvTable:
        """Returns client class' table."""
        return RecvTable(
            self._handle.read_int( self._start_addr + 0xC ),
            self._handle
        )