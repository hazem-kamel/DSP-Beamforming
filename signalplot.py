# ------------------------------------------------------
# -------------------- signalplot.py --------------------
# ------------------------------------------------------

from matplotlib.backends.backend_qt5 import SaveFigureQt
from beamforming import beamsForming
from PyQt5.QtWidgets import *
from scipy.io import wavfile
import wave
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import pyaudio
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QSound


# Class that plots our functions
class MatPlotCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        # Plot and its title
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.suptitle('Audio Channels')

        # Format spaces between plots
        fig.subplots_adjust(left=0.1,
                            bottom=0.1,
                            right=0.9,
                            top=0.9,
                            wspace=0.2,
                            hspace=0.6)

        font = {'family': 'DejaVu Sans',
                'weight': 'bold',
                'size': 8}

        matplotlib.rc('font', **font)


        # PLOT 1
        self.ax1 = fig.add_subplot(421, title='Channel 1')
        self.ax1.set_xlabel("Time [s]")
        self.ax1.set_ylabel("Amplitude")
        # self.ax1.set_ylim(-2.0,2.0)

        # PLOT 2
        self.ax2 = fig.add_subplot(423, title='Channel 2')
        self.ax2.set_xlabel("Time [s]")
        self.ax2.set_ylabel("Amplitude")
        # self.ax2.set_ylim(-2.0,2.0)

        # PLOT 3
        self.ax3 = fig.add_subplot(425, title='Channel 3')
        self.ax3.set_xlabel("Time [s]")
        self.ax3.set_ylabel("Amplitude")
        # self.ax3.set_ylim(-200.0,200.0)

        # PLOT 4
        self.ax4 = fig.add_subplot(427, title='Channel 4')
        self.ax4.set_xlabel("Time [s]")
        self.ax4.set_ylabel("Amplitude")
        # self.ax4.set_ylim(-2.0,2.0)

        # PLOT 5
        self.ax5 = fig.add_subplot(422, title='Channel 5')
        self.ax5.set_xlabel("Time [s]")
        self.ax5.set_ylabel("Amplitude")
        # self.ax5.set_ylim(-2.0,2.0)

        # PLOT 6
        self.ax6 = fig.add_subplot(424, title='Channel 6')
        self.ax6.set_xlabel("Time [s]")
        self.ax6.set_ylabel("Amplitude")
        # self.ax6.set_ylim(-2.0,2.0)

        # PLOT 7
        self.ax7 = fig.add_subplot(426, title='Channel 7')
        self.ax7.set_xlabel("Time [s]")
        self.ax7.set_ylabel("Amplitude")
        # self.ax7.set_ylim(-200.0,200.0)

        # PLOT 8
        self.ax8 = fig.add_subplot(428, title='Channel 8')
        self.ax8.set_xlabel("Time [s]")
        self.ax8.set_ylabel("Amplitude")
        # self.ax8.set_ylim(-2.0,2.0)

        super(MatPlotCanvas, self).__init__(fig)


class SignalPlot(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)


        self.canvas = MatPlotCanvas(self, width=5, height=4, dpi=100)


        # create open button
        self.openFileButton = QPushButton('Open Media')
        self.openFileButton.clicked.connect(self.open_file)

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.openFileButton)
        vertical_layout.addWidget(self.canvas)

        self.setLayout(vertical_layout)

    def open_file(self):

        self.filename, _ = QFileDialog.getOpenFileName(self, "Open Media")

        if self.filename != '':
            #self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename)))
            #self.playBtn.setEnabled(True)
            self.samplerate, self.data = wavfile.read(self.filename)
            self.channels = self.data.shape[1]
            self.length = self.data.shape[0] / self.samplerate
            self.time = np.linspace(0., self.length, self.data.shape[0])

            self.updatePlots()


    def updatePlots(self):
        self.canvas.ax1.cla()
        self.canvas.ax2.cla()
        self.canvas.ax3.cla()
        self.canvas.ax4.cla()
        self.canvas.ax5.cla()
        self.canvas.ax6.cla()
        self.canvas.ax7.cla()
        self.canvas.ax8.cla()

        ############# Update Plots ##########
        if self.data.shape[1] >=1:
            self.canvas.ax1.plot(self.time, self.data[:, 0], label="Channel 1")
        if self.data.shape[1] >=2:
            self.canvas.ax2.plot(self.time, self.data[:, 1], label="Channel 2")
        if self.data.shape[1] >=3:
            self.canvas.ax3.plot(self.time, self.data[:, 2], label="Channel 3")
        if self.data.shape[1] >=4:
            self.canvas.ax4.plot(self.time, self.data[:, 3], label="Channel 4")
        if self.data.shape[1] >=5:
            self.canvas.ax5.plot(self.time, self.data[:, 4], label="Channel 5")
        if self.data.shape[1] >=6:
            self.canvas.ax6.plot(self.time, self.data[:, 5], label="Channel 6")
        if self.data.shape[1] >=7:
            self.canvas.ax7.plot(self.time, self.data[:, 6], label="Channel 7")
        if self.data.shape[1] >=8:
            self.canvas.ax8.plot(self.time, self.data[:, 7], label="Channel 8")

        self.canvas.draw()

    def beamdirection(self,angle):
        if(0<angle<45):
            print('mic 5')
            output=beamsForming(self.data,'5')
            print(output,'final data')
            saveFile(output)
        if(45<angle<114):
            print('mic 6')
            output=beamsForming(self.data,'6')
            print(output,'final data')
            saveFile(output)
        if(114<angle<180):
            print('mic 1')
            output=beamsForming(self.data,'1')
            print(output,'final data')
            saveFile(output)
        if(180<angle<247):
            print('mic 2')
            output=beamsForming(self.data,'2')
            print(output,'final data')
            saveFile(output)
        if(247<angle<293):
            output=beamsForming(self.data,'3')
            print(output,'final data')
            saveFile(output)
            print('mic 3')
        if(293<angle<360):
            output=beamsForming(self.data,'4')
            saveFile(output)
            print('mic 4')
            
def saveFile(yds):
    WAVE_OUTPUT_FILENAME='beamformed-direction-30'
    # CHANNELS=6
    # FORMAT = pyaudio.paInt16
    fs = 16000
    # wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    # wf.setnchannels(CHANNELS)
    # wf.setsampwidth(p.get_sample_size(FORMAT))
    # wf.setframerate(RATE)
    # wf.writeframes(b''.join(yds))
    # wf.close()
        # Save channel to a separate file
    # outwav = wave.open(WAVE_OUTPUT_FILENAME, 'w')
    # outwav.setparams(self.filename.getparams())
    # outwav.setnchannels(6)
    # outwav.writeframes(yds.tostring())
    A7_chord = np.array([ yds ]).T
    wavfile.write("A7--4channel.wav", fs, A7_chord)
    # outwav.close()

