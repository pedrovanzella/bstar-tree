import attr
import struct


@attr.s
class Rowid:
    """
    Rowid points to a record in a datablock
    """
    dblock = attr.ib() #endereco datablock ?
    pos = attr.ib(validator=attr.validators.instance_of(int)) #end registro ?

    def get_record(self):
        """
        Returns a Record from the Rowid
        """
        return self.dblock.get_records()[self.pos]

    def pack(self):
        return struct.pack('HH', self.dblock, self.pos)
