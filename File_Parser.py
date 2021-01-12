import errno
import os

from Input_Stream import Input_Stream

class File_Parser:
    
    def __init__(self,file_name,):
        if os.path.exists(file_name):
            self._file = open(file_name, "r")
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file_name)
        self._list = []
        self._input_stream = Input_Stream()
    
    def read(self):
       #purpose tokenize verline lin in a file
        if self._file. mode == "r":
            content = self._file.readlines()
        
        for line in content :
            if(len(line) > 1):
                line = line[0:len(line)-1]
                self.tokenize(line)
        return self._list
    
    def tokenize(self,line):
        #purpose: tokenize line
        #param[in]      string      line to be tokenize
        self._list.append(self._input_stream.tokenize(line))
    
    def print_list(self):
        #purpose prints lisr
        for l in self._list:
            print(l)