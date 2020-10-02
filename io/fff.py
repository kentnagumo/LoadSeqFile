import re
import pickle
import struct
import numpy as np
import sys
import six

from LoadSeqFile.util.raw import raw2temp
from LoadSeqFile.util.exiftool import Exiftool

class Fff:

    def __init__(self, data, height = 512, width = 640, exiftool_path=None):

        self.height = height
        self.width = width
        self.image = None
        self.filename = None

        self.exiftool = Exiftool(exiftool_path)

        # This is a dirty hack to force Python 2 to recognise whether
        # it's a filename or a file. An FFF file is almost always
        # larger than 2kB.
        if isinstance(data, str) and len(data) < 4096:
            with open(data, 'rb') as fff_file:
                self.filename = fff_file
                self.data = fff_file.read()
        elif isinstance(data, bytes):
            self.data = data
        else:
            raise TypeError("Data should be a bytes object or a string filename")

    def write(self, path):
        with open(path, 'wb') as fff_file:
            fff_file.write(self.data)

    def _find_data_offset(self, data):
        d_number_w = self.width-1
        x_number_w = d_number_w.to_bytes(2, byteorder='little').hex()

        d_number_h = self.height-1
        x_number_h = d_number_h.to_bytes(2, byteorder='little').hex()

        search_str = '\\x{}\\x{}\\x00\\x00\\x{}\\x{}'.format(x_number_w[0:2], x_number_w[2:4], x_number_h[0:2], x_number_h[2:4])
        search = search_str.encode()

        valid = re.compile(search)
        res = valid.search(data)

        return res.end()+14
    
    def get_radiometric_image(self, meta):
        image = raw2temp(self.get_image(), meta)

        return image

    def get_image(self):
        
        if self.image is None:
            offset = self._find_data_offset(self.data)
            count = self.height*self.width
            self.image = np.frombuffer(self.data, offset=offset, dtype='uint16', count=count).reshape((self.height, self.width))
        
        return self.image
    
    def get_gps(self):
        valid = re.compile("[0-9]{4}[NS]\x00[EW]\x00".encode())

        res = valid.search(self.data)
        start_pos = res.start()

        s = struct.Struct("<4xcxcx4xddf32xcxcx4xff")

        return s.unpack_from(self.data, start_pos)