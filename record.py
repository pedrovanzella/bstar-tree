import attr
import struct
from rowid import Rowid

def len_less_than_200(instance, attribute, value):
    if type(value) is not str:
        raise TypeError("Description must be a string")
    if len(value) > 200:
        raise ValueError("Description must be less than 200 chars long!")


@attr.s
class Record:
    code = attr.ib(validator=attr.validators.instance_of(int))
    description = attr.ib(validator=len_less_than_200)
    # WARNING: must call attr.validate(description) on EVERY update
    rowid = attr.ib(validator=attr.validators.instance_of(Rowid))

    def pack(self):
        return struct.pack('I%ss' % self.writeble_size(self.description), self.code, self.description.encode())

    def writeble_size(self, str_obj):
        size = len(str_obj)
        for i in range(0,4):
            if((size+i) % 4 == 0):
                return size+i
        return size
