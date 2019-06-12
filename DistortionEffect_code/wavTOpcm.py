import os
import numpy as np
filename = "E_Guitar.wav"
f = open(filename,'r',encoding='latin-1')
f.seek(0)
f.read(44)
data = np.fromfile(f, dtype=np.int16)
data.tofile("E_Guitar.pcm")
