import numpy as np
import matplotlib.pyplot as plt
import scikits.audiolab as audiolab
import scipy.fftpack as fourier
import csv
idsong =[]
nombre =[]
with open('birdsong_metadata.csv') as File:
    reader = csv.reader(File)
    for row in reader:

        idsong.append("xc"+row[0])
        nombre.append(row[3])

'''print(nombre)
print(idsong)'''

sound=audiolab.sndfile('audio1.wav','read')
data=sound.read_frames(sound.get_samplerate())
print(len(data))
sound.close()

count=0
ejex=[]
for i in data:
	
	ejex.append(count)
	count=count+1

data=data[::-1]

plt.plot(ejex,data)
plt.ylabel('some numbers')
plt.show()
t0=0
tn=0.5 #float(input('rango segundos [0,tn]:'))
n= 1024
dt=(tn-t0)/n
xf=fourier.fft(data)
xf=fourier.fftshift(xf)
# Rango de frecuencia para eje
frq=fourier.fftfreq(n, dt)
frq=fourier.fftshift(frq)
plt.plot(xf)
plt.ylabel('some numbers')
plt.show()
'''spectogram=plt.specgram(data)
plt.show()'''
