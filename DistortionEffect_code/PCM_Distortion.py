import numpy as np 
import pylab

def distortion(data,threshold):
	for i in range(len(data)):
		if data[i] > threshold:
			data[i] = threshold
		if data[i] < -threshold:
			data[i] = -threshold
	return data		


def amplitude_normalize(data):
	for i in range(len(data)):
		data[i]=2*data[i]
	return data

if __name__ == "__main__":

	filename = "E_Guitar.pcm"
	data = np.memmap(filename, dtype='h', mode='r+')  #h:int 16  r+:read and write
	data = distortion(data,5000)
	data = amplitude_normalize(data)
	pylab.plot(data)
	pylab.show()