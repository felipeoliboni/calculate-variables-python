import numpy as np
import importFile as importFile
import os

class GPEAnalyzer:

    def __init__(self, path, newpath, file):
        self.full = newpath + "\\" + file
        self.file = file
        self.path = path
        self.data = importFile.importFile(self.path, self.file)
        log_freq = np.log10(self.data.frequency)
        log_zi = np.log10( self.data.z_imaginary )
        deriv_log_zi = np.gradient( log_zi , log_freq )
        alpha_eff = np.abs(deriv_log_zi)
        frequency = np.array(self.data.frequency)
        zi = np.array(self.data.z_imaginary)
        Qeff = np.sin(alpha_eff*np.pi/2)/(self.data.z_imaginary*np.power(2*np.pi*frequency, alpha_eff))
        Ceff = 1/(2*np.pi*frequency*zi)
        Cgpe = np.power(Qeff, 1/alpha_eff)*np.power(self.data.z_real, ((1-alpha_eff)/alpha_eff))
        self.data.Alpha = alpha_eff.tolist()
        self.data.Qeff = Qeff.tolist()
        self.data.Ceff = Ceff.tolist()
        self.data.Cgpe = Cgpe.tolist()
        self.exp_data = 'Index\tFrequency (Hz)\tZ` (Ohm)\t-Z`` (Ohm)\t;Z (Ohm)\t-Phase (o)\tTime (s)\tAlpha\tQeff\tCeff (F)\tCgpe (F)\n'
        size_list = len(self.data.index)
        file_object = open( self.full + '_full.dat', "w+" )
        for line in range(size_list):
            self.exp_data = self.exp_data + str(self.data.index[line]) + '\t' + \
                           str(self.data.frequency[line]) + '\t' + \
                           str(self.data.index[line]) + '\t' + \
                           str(self.data.frequency[line]) + '\t' + \
                           str(self.data.z_real[line]) + '\t' + \
                           str(self.data.z_imaginary[line]) + '\t' + \
                           str(self.data.phase[line]) + '\t' + \
                           str(self.data.time[line]) + '\t' + \
                           str(self.data.Alpha[line]) + '\t' + \
                           str(self.data.Qeff[line]) + '\t' + \
                           str(self.data.Ceff[line]) + '\t' + \
                           str(self.data.Cgpe[line]) + '\n'
        file_object.write(self.exp_data)
        file_object.close()