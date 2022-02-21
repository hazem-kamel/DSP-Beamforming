# ------------------------------------------------------
# -------------------- signalplot.py --------------------
# ------------------------------------------------------

import pyaudio
import os
import time
import struct
import numpy as np
from threading import Thread

import matplotlib
matplotlib.use('Qt5Agg')

from tkinter import TclError
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import *



class AudioFocusPlot(QWidget, Thread):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        Thread.__init__(self)
        self.daemon = True
        self.start()

        self.canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        # constants
        self.CHUNK = 1024 * 2  # samples per frame
        self.FORMAT = pyaudio.paInt16  # audio format (bytes per sample?)
        self.CHANNELS = 1  # single channel for microphone
        self.RATE = 44100  # samples per second

        # create matplotlib figure and axes
        self.canvas.ax1 = self.canvas.figure.add_subplot(111)
        #fig, ax1 = plt.subplots(1, figsize=(15, 7))


        self.setLayout(vertical_layout)



    def run(self):

        # pyaudio class instance
        p = pyaudio.PyAudio()

        # get list of availble inputs
        info = p.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')
        for i in range(0, numdevices):
            if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

        # select input
        audio_input = input("\n\nSelect input by Device id: ")

        # stream object to get data from microphone
        self.stream = p.open(
            input_device_index=int(audio_input),
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            output=True,
            frames_per_buffer=self.CHUNK
        )

        # variable for plotting
        x = np.arange(0, 2 * self.CHUNK, 2)

        # create a line object with random data
        line, = self.canvas.ax1.plot(x, np.random.rand(self.CHUNK), '-', lw=2)

        # basic formatting for the ax1es
        self.canvas.ax1.set_title('AUDIO WAVEFORM')
        self.canvas.ax1.set_xlabel('samples')
        self.canvas.ax1.set_ylabel('volume')
        self.canvas.ax1.set_ylim(0, 255)
        self.canvas.ax1.set_xlim(0, self.CHUNK)
        #plt.setp(self.canvas.ax1, xticks=[0, self.CHUNK, 2 * self.CHUNK], yticks=[0, 128, 255])

        # show the plot
        #plt.show(block=False)

        print('stream started')

        # for measuring frame rate
        self.frame_count = 0
        self.start_time = time.time()

        while True:

            # binary data
            data = self.stream.read(self.CHUNK)

            # convert data to integers, make np array, then offset it by 127
            data_int = struct.unpack(str(2 * self.CHUNK) + 'B', data)

            # create np array and offset by 128
            data_np = np.array(data_int, dtype='b')[::2] + 128

            #line.set_ydata(data_np)
            self.canvas.ax1.plot(data_np)

            # update figure canvas
            try:
                self.canvas.draw()
                self.canvas.flush_events()
                self.frame_count += 1

            except TclError:

                # calculate average frame rate
                frame_rate = self.rame_count / (time.time() - self.start_time)

                print('stream stopped')
                print('average frame rate = {:.0f} FPS'.format(frame_rate))
                break


