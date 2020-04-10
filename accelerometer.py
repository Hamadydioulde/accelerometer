# accelerometer
#import random
import numpy as np
import pandas as pd
from scipy.io import wavfile
import matplotlib.pyplot as plt
path = "Downloads/test and csv files/AccelerometerWalking.csv"
new_data=pd.read_csv(path, delimiter=",")
#new_data
new_data.columns= ["Time(s)","X", "Y", "Z", "R", "theta", "Phi"]

#new_data
columnlist = list(new_data.X)
#columnlist1=list(new_data.Y)
#columnlist2=list(new_data.Z)
#columnsum=list(new_data.X + new_data.Y + new_data.Z)
arrX=np.array(columnlist)
arrX

#arrX.shape
arrX=np.array(arrX * 100)
arrX.shape
arrX
scale = 5
#upsampled1 = arrX.repeat(scale, axis=0)
len(upsampled1)
upsampled1.shape

from scipy.io import wavfile
arrXtype=upsampled1.astype("int16")
wavfile.write("AccelerometertoSound_int16.wav",44100, arrXtype) 

import sounddevice as sd
arrXtype=upsampled1.astype("int16")
#sd.play(arrXtype, 10000)
#sd.stop()
from IPython.display import Audio
import numpy as np
audio = Audio(data=upsampled1, rate=15000)
audio
