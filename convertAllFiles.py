import GPEAnalyzer as GPE
import os
from os import walk
import glob


class convertAllFiles:
    def __init__(self, extension, path):
        self.extension = extension
        self.gpe_analyzer = GPE
        self.path = path
        self.newpath = path + "\\" + "full\\" 
        os.mkdir(self.newpath)
        self.list_files(self.path, self.newpath)


    def list_files(self, path, newpath):
        self.f = []
        for (dirpath, dirnames, filenames) in walk( self.path ):
            self.f.extend( filenames )
            break
        for file in self.f:
            if file[-4:] != self.extension:
                self.gpe_analyzer.GPEAnalyzer(path, newpath, file)
