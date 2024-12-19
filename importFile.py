class importFile:

    def __init__(self, path, file):
            full = path+"\\"+file
            self.file_object = open( full, 'r' )
            self.words = self.file_object.read().splitlines()
            self.file_object.close()
            # 'Index; Frequency (Hz); Z` (Ω);-Z`` (Ω);Z (Ω);-Phase (°);Time (s)"
            self.index = []
            self.frequency = []
            self.z_real = []
            self.z_imaginary = []
            self.phase = []
            self.time = []
            self.words.pop( 0 )
            with open(full) as fin:
                next(fin)
                next(fin)
                for lines in fin:
	                line = lines.split( "\t" )
	                self.index.append( float( line[0] ) )
	                self.frequency.append( float( line[1] ) )
	                self.z_real.append( float( line[2] ) )
	                self.z_imaginary.append( float( line[3] ) )
	                self.phase.append( float( line[4] ) )
	                self.time.append( float( line[5] ) )