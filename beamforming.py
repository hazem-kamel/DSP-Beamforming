# import numpy as np
# from scipy.signal.signaltools import wiener
# from scipy import signal
# def beamsForming(data):
#         print(data,'data is heree')
#         # Calculate the Cross-Correlation
#         print('working cc')
#         first_two=signal.correlate(data[:,0], data[:,1], mode='full', method='auto')
#         second_two=signal.correlate(data[:,2], data[:,3], mode='full', method='auto')
#         third_two=signal.correlate(data[:,4], data[:,5], mode='full', method='auto')
#         # # Calculate the The Time Difference of Arrival between 6 mics
#         first_TDOA=np.argmax(first_two, axis=None, out=None)
#         second_TDOA=np.argmax(second_two, axis=None, out=None)
#         third_TDOA=np.argmax(third_two, axis=None, out=None)
#         print('working tdoa')
#         # Calculate Xi Tao is zero for our reference microphone which is in our direction
#                 # AttenuationFactor*channel(t-tao(i))
#         #  Calculate the Beamforming 
#         # 1/m  summation(xi(t-tao(i)))


#         # Another method in case first method did not work
# # class beamForming:
# #     def __init__(self):
# #         print(self.data[:, 0])
# #         def calculateCrossCorrelation():
# #             # Gain Function
# #             # Get Cross Corellation
# #         def GetDelay():
# #             print()
# #             # Y=1/M*x(i)*(t-(-taw(i)))

# #     # # Calculate azimuth and elevation for 6 mics array Positions of mics (rows for each mic columns for space of mic position)
# #     # # Get the required focus direction in same dimensionality as the space of the microphones


# #     # DirectionSource=np.array([-30, -20], float) # azimuth/elevation steering angle
# #     # speedSound=340
# # #     def getAngle():
# # #         pass
# # # def compute_delays(self):
# # #     for x in range(0, self.array.sizeX):
# # #         for y in range(0, self.array.sizeY):
            
# # #             self.delay[y, x] = (1/self.c *
# # #                                 np.sin(np.pi / 180. * self.steeringAngle[0]) *
# # #                                 (np.cos(np.pi / 180. * self.steeringAngle[1]) * self.array.coordinatesX[y, x] +
# # #                                  np.sin(np.pi / 180. * self.steeringAngle[1]) * self.array.coordinatesY[y, x]))
# # #     def summationFunction():
# # #         pass
# # #     def outputBeamFormed():
# # #         pass

import numpy as np
from scipy.signal.signaltools import wiener
from scipy import signal
import matplotlib.pyplot as plt

def beamsForming(data,direction):
        fs = 16000
        # Calculate the Cross-Correlation
        #first_two=signal.correlate(data[:,0], data[:,1], mode='full', method='auto')
        #second_two=signal.correlate(data[:,2], data[:,3], mode='full', method='auto')
        #third_two=signal.correlate(data[:,4], data[:,5], mode='full', method='auto')
        # # Calculate the The Time Difference of Arrival between 6 mics
        if(direction == '1'):
                    reference2mic2 = my_fast_conv(data[:,0],    data[:,1])
                    reference2mic3 = my_fast_conv(data[:,0],    data[:,2])
                    reference2mic4 = my_fast_conv(data[:,0],    data[:,3])
                    reference2mic5 = my_fast_conv(data[:,0],    data[:,4])
                    reference2mic6 = my_fast_conv(data[:,0],    data[:,5])
                    ref2mic2_samples = np.where(reference2mic2 == max(reference2mic2))[0]
                    delayed_sample2 = len(data[:,0]) - ref2mic2_samples 
                    tau2 = delayed_sample2/fs
                    #delayed_sample = list(self.delayed_sample)[0] - 1
                    #plt.plot(reference2mic2)
                    #plt.ylabel('some numbers')
                    #plt.show()
                    ref2mic3_samples = np.where(reference2mic3 ==max(reference2mic3))[0]
                    delayed_sample3 = len(data[:,0]) - ref2mic3_samples 
                    ref2mic4_samples = np.where(reference2mic4 ==max(reference2mic4))[0]
                    delayed_sample4 = len(data[:,0]) - ref2mic4_samples 
                    ref2mic5_samples = np.where(reference2mic5 ==max(reference2mic5))[0]
                    delayed_sample5 = len(data[:,0]) - ref2mic5_samples 
                    ref2mic6_samples = np.where(reference2mic6 ==max(reference2mic6))[0]
                    delayed_sample6 = len(data[:,0]) - ref2mic6_samples        
                    tau3 = delayed_sample3/fs
                    tau4 = delayed_sample4/fs
                    tau5 = delayed_sample5/fs
                    tau6 = delayed_sample6/fs
                    data2 = shift_signal_in_frequency_domain(data[:,2],delayed_sample2)
                    data3 = shift_signal_in_frequency_domain(data[:,3],delayed_sample3)
                    data4 = shift_signal_in_frequency_domain(data[:,4],delayed_sample4)
                    data5 = shift_signal_in_frequency_domain(data[:,5],delayed_sample5)
                    data6 = shift_signal_in_frequency_domain(data[:,1],delayed_sample6)
                    yds = data[:,0]+data2+data3+data4+data5+data6
                    yds = yds/6
                    return yds
        elif (direction == '2'):
                    reference2mic2 = my_fast_conv(data[:,1], np.flip(data[:,0]))
                    reference2mic3 = my_fast_conv(data[:,1], np.flip(data[:,2]))
                    reference2mic4 = my_fast_conv(data[:,1], np.flip(data[:,3]))
                    reference2mic5 = my_fast_conv(data[:,1], np.flip(data[:,4]))
                    reference2mic6 = my_fast_conv(data[:,1], np.flip(data[:,5]))
                    ref2mic2_samples = np.where(reference2mic2 == max(reference2mic2))[0]
                    delayed_sample2 = len(data[:,1]) - ref2mic2_samples 
                    tau2 = delayed_sample2/fs
                    ref2mic3_samples = np.where(reference2mic3 ==max(reference2mic3))[0]
                    delayed_sample3 = len(data[:,1]) - ref2mic3_samples 
                    ref2mic4_samples = np.where(reference2mic4 ==max(reference2mic4))[0]
                    delayed_sample4 = len(data[:,1]) - ref2mic4_samples 
                    ref2mic5_samples = np.where(reference2mic5 ==max(reference2mic5))[0]
                    delayed_sample5 = len(data[:,1]) - ref2mic5_samples 
                    ref2mic6_samples = np.where(reference2mic6 ==max(reference2mic6))[0]
                    delayed_sample6 = len(data[:,1]) - ref2mic6_samples        
                    tau3 = delayed_sample3/fs
                    tau4 = delayed_sample4/fs
                    tau5 = delayed_sample5/fs
                    tau6 = delayed_sample6/fs
                    data2 = shift_signal_in_frequency_domain(data[:,2],delayed_sample2)
                    data3 = shift_signal_in_frequency_domain(data[:,3],delayed_sample3)
                    data4 = shift_signal_in_frequency_domain(data[:,4],delayed_sample4)
                    data5 = shift_signal_in_frequency_domain(data[:,5],delayed_sample5)
                    data6 = shift_signal_in_frequency_domain(data[:,0],delayed_sample6)
                    yds = data[:,1]+data2+data3+data4+data5+data6
                    yds = yds/6
                    return yds
        elif (direction == '3'):
                    reference2mic3 = my_fast_conv(data[:,2], np.flip(data[:,0]))
                    reference2mic2 = my_fast_conv(data[:,2], np.flip(data[:,1]))
                    reference2mic4 = my_fast_conv(data[:,2], np.flip(data[:,3]))
                    reference2mic5 = my_fast_conv(data[:,2], np.flip(data[:,4]))
                    reference2mic6 = my_fast_conv(data[:,2], np.flip(data[:,5]))
                    ref2mic2_samples = np.where(reference2mic2 == max(reference2mic2))[0]
                    delayed_sample2 = len(data[:,2]) - ref2mic2_samples 
                    tau2 = delayed_sample2/fs
                    #delayed_sample = list(self.delayed_sample)[0] - 1
                    #plt.plot(reference2mic2)
                    #plt.ylabel('some numbers')
                    #plt.show()
                    ref2mic3_samples = np.where(reference2mic3 ==max(reference2mic3))[0]
                    delayed_sample3 = len(data[:,2]) - ref2mic3_samples 
                    ref2mic4_samples = np.where(reference2mic4 ==max(reference2mic4))[0]
                    delayed_sample4 = len(data[:,2]) - ref2mic4_samples 
                    ref2mic5_samples = np.where(reference2mic5 ==max(reference2mic5))[0]
                    delayed_sample5 = len(data[:,2]) - ref2mic5_samples 
                    ref2mic6_samples = np.where(reference2mic6 ==max(reference2mic6))[0]
                    delayed_sample6 = len(data[:,2]) - ref2mic6_samples        
                    tau3 = delayed_sample3/fs
                    tau4 = delayed_sample4/fs
                    tau5 = delayed_sample5/fs
                    tau6 = delayed_sample6/fs
                    data2 = shift_signal_in_frequency_domain(data[:,1],delayed_sample2)
                    data3 = shift_signal_in_frequency_domain(data[:,3],delayed_sample3)
                    data4 = shift_signal_in_frequency_domain(data[:,4],delayed_sample4)
                    data5 = shift_signal_in_frequency_domain(data[:,5],delayed_sample5)
                    data6 = shift_signal_in_frequency_domain(data[:,0],delayed_sample6)
                    yds = data[:,0]+data2+data3+data4+data5+data6
                    yds = yds/6
                    return yds
        elif (direction == '4'):
                    print('1')
                    reference2mic2 = my_fast_conv(data[:,3], np.flip(data[:,1]))
                    reference2mic3 = my_fast_conv(data[:,3], np.flip(data[:,2]))
                    reference2mic4 = my_fast_conv(data[:,3], np.flip(data[:,0]))
                    reference2mic5 = my_fast_conv(data[:,3], np.flip(data[:,4]))
                    reference2mic6 = my_fast_conv(data[:,3], np.flip(data[:,5]))
                    ref2mic2_samples = np.where(reference2mic2 == max(reference2mic2))[0]
                    delayed_sample2 = len(data[:,0]) - ref2mic2_samples 
                    tau2 = delayed_sample2/fs
                    #delayed_sample = list(self.delayed_sample)[0] - 1
                    #plt.plot(reference2mic2)
                    #plt.ylabel('some numbers')
                    #plt.show()
                    ref2mic3_samples = np.where(reference2mic3 ==max(reference2mic3))[0]
                    delayed_sample3 = len(data[:,3]) - ref2mic3_samples 
                    ref2mic4_samples = np.where(reference2mic4 ==max(reference2mic4))[0]
                    delayed_sample4 = len(data[:,3]) - ref2mic4_samples 
                    ref2mic5_samples = np.where(reference2mic5 ==max(reference2mic5))[0]
                    delayed_sample5 = len(data[:,3]) - ref2mic5_samples 
                    ref2mic6_samples = np.where(reference2mic6 ==max(reference2mic6))[0]
                    delayed_sample6 = len(data[:,3]) - ref2mic6_samples        
                    tau3 = delayed_sample3/fs
                    tau4 = delayed_sample4/fs
                    tau5 = delayed_sample5/fs
                    tau6 = delayed_sample6/fs
                    data2 = shift_signal_in_frequency_domain(data[:,2],delayed_sample2)
                    data3 = shift_signal_in_frequency_domain(data[:,1],delayed_sample3)
                    data4 = shift_signal_in_frequency_domain(data[:,4],delayed_sample4)
                    data5 = shift_signal_in_frequency_domain(data[:,5],delayed_sample5)
                    data6 = shift_signal_in_frequency_domain(data[:,0],delayed_sample6)
                    yds = data[:,3]+data2+data3+data4+data5+data6
                    yds = yds/6
                    return yds
        elif (direction == '5'):
                    print('1')
                    reference2mic2 = my_fast_conv(data[:,4], np.flip(data[:,1]))
                    reference2mic3 = my_fast_conv(data[:,4], np.flip(data[:,2]))
                    reference2mic4 = my_fast_conv(data[:,4], np.flip(data[:,3]))
                    reference2mic5 = my_fast_conv(data[:,4], np.flip(data[:,4]))
                    reference2mic6 = my_fast_conv(data[:,4], np.flip(data[:0]))
                    ref2mic2_samples = np.where(reference2mic2 == max(reference2mic2))[0]
                    delayed_sample2 = len(data[:,4]) - ref2mic2_samples 
                    tau2 = delayed_sample2/fs
                    #delayed_sample = list(self.delayed_sample)[0] - 1
                    #plt.plot(reference2mic2)
                    #plt.ylabel('some numbers')
                    #plt.show()
                    ref2mic3_samples = np.where(reference2mic3 ==max(reference2mic3))[0]
                    delayed_sample3 = len(data[:,4]) - ref2mic3_samples 
                    ref2mic4_samples = np.where(reference2mic4 ==max(reference2mic4))[0]
                    delayed_sample4 = len(data[:,4]) - ref2mic4_samples 
                    ref2mic5_samples = np.where(reference2mic5 ==max(reference2mic5))[0]
                    delayed_sample5 = len(data[:,4]) - ref2mic5_samples 
                    ref2mic6_samples = np.where(reference2mic6 ==max(reference2mic6))[0]
                    delayed_sample6 = len(data[:,4]) - ref2mic6_samples        
                    tau3 = delayed_sample3/fs
                    tau4 = delayed_sample4/fs
                    tau5 = delayed_sample5/fs
                    tau6 = delayed_sample6/fs
                    data2 = shift_signal_in_frequency_domain(data[:,2],delayed_sample2)
                    data3 = shift_signal_in_frequency_domain(data[:,3],delayed_sample3)
                    data4 = shift_signal_in_frequency_domain(data[:,1],delayed_sample4)
                    data5 = shift_signal_in_frequency_domain(data[:,5],delayed_sample5)
                    data6 = shift_signal_in_frequency_domain(data[:,0],delayed_sample6)
                    yds = data[:,4]+data2+data3+data4+data5+data6
                    yds = yds/6
                    return yds
        elif (direction == '6'):
                    reference2mic2 = my_fast_conv(data[:,5], np.flip(data[:,1]))
                    reference2mic3 = my_fast_conv(data[:,5], np.flip(data[:,2]))
                    reference2mic4 = my_fast_conv(data[:,5], np.flip(data[:,3]))
                    reference2mic5 = my_fast_conv(data[:,5], np.flip(data[:,4]))
                    reference2mic6 = my_fast_conv(data[:,5], np.flip(data[:,0]))
                    ref2mic2_samples = np.where(reference2mic2 == max(reference2mic2))[0]
                    delayed_sample2 = len(data[:,5]) - ref2mic2_samples 
                    tau2 = delayed_sample2/fs
                    #delayed_sample = list(self.delayed_sample)[0] - 1
                    #plt.plot(reference2mic2)
                    #plt.ylabel('some numbers')
                    #plt.show()
                    ref2mic3_samples = np.where(reference2mic3 ==max(reference2mic3))[0]
                    delayed_sample3 = len(data[:,5]) - ref2mic3_samples 
                    ref2mic4_samples = np.where(reference2mic4 ==max(reference2mic4))[0]
                    delayed_sample4 = len(data[:,5]) - ref2mic4_samples 
                    ref2mic5_samples = np.where(reference2mic5 ==max(reference2mic5))[0]
                    delayed_sample5 = len(data[:,5]) - ref2mic5_samples 
                    ref2mic6_samples = np.where(reference2mic6 ==max(reference2mic6))[0]
                    delayed_sample6 = len(data[:,5]) - ref2mic6_samples        
                    tau3 = delayed_sample3/fs
                    tau4 = delayed_sample4/fs
                    tau5 = delayed_sample5/fs
                    tau6 = delayed_sample6/fs
                    data2 = shift_signal_in_frequency_domain(data[:,2],delayed_sample2)
                    data3 = shift_signal_in_frequency_domain(data[:,3],delayed_sample3)
                    data4 = shift_signal_in_frequency_domain(data[:,4],delayed_sample4)
                    data5 = shift_signal_in_frequency_domain(data[:,0],delayed_sample5)
                    data6 = shift_signal_in_frequency_domain(data[:,1],delayed_sample6)
                    yds = data[:,5]+data2+data3+data4+data5+data6
                    yds = yds/6
                    return yds
def nextpow2(i):
    '''Find the next power 2 number for FFT'''
    n = 1
    while n < i: n *= 2
    return n
def shift_signal_in_frequency_domain(datin, shift):
    '''
    This is function to shift a signal in frequency domain. 
    The idea is in the frequency domain, 
    we just multiply the signal with the phase shift. 
    '''
    Nin = len(datin) 
    
    # get the next power 2 number for fft
    N = nextpow2(Nin +np.max(np.abs(shift)))
    
    # do the fft
    fdatin = np.fft.fft(datin, N)
    
    # get the phase shift for the signal, shift here is D in the above explaination
    ik = np.array([2j*np.pi*k for k in range(0, N)]) / N 
    fshift = np.exp(-ik*shift)
        
    # multiple the signal with the shift and transform it back to time domain
    datout = np.real(np.fft.ifft(fshift * fdatin))
    
    # only get the data have the same length as the input signal
    datout = datout[0:Nin]
    return datout
def my_fast_conv(x, h):
    fftsize_x = len(x)
    fftsize_h = len(h)
    fftsize = fftsize_x + fftsize_h -1 
    X = np.fft.fft(x,fftsize)
    H = np.fft.fft(h,fftsize)
    Y = X * H
    # Inverse fourier transform
    y = np.fft.ifft(Y,fftsize)
    return abs(y)

