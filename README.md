# SS2021

# Digital Signal Processing PT
## BEAMFORMING
<sub>Armin Niedermueller, Ahmet Cihat Bozkurt, Hazem Kamel</sub>

## Introduction

Throw a stone into a pond. You'll see circular waves travelling outwards from the point of impact. Throw two stones, and you'll see an interference pattern forming.
At locations where maxima from the first stone coincide with the minima from the second stone, you'll get extiction, and where maxima meet maxima, you'll get amplification.
Beamforming is about controlling this interference pattern, and, in most cases,
it is about forming a beam-like interference pattern where the amplification occurs predominantly in one distinct direction.
<sup>5</sup>

The following image shows this principle. Two antennas send the same signal, the intersection points of the waves amplifiy the signal in a specific direction. If now a phase shift is introduced in one antenna, the direction where the waves intersect changes.
This can be used to amplify a WiFi signal in the direction where a user device is located and thus improve the connection quality.

<img src="images/beamforming_antennas.jpg" width="800"/>

Another animated image shows the direction change of the beam.

<img src="https://upload.wikimedia.org/wikipedia/commons/1/1e/Phasearray.gif" width="400"/>
<br>
<sub>Image Source: https://upload.wikimedia.org/wikipedia/commons/1/1e/Phasearray.gif </sub>


## Algorithms

## Topic relevance

Give an overview which fields are connected to the topic.

## Fields of Application

Minimum of 10 different applications in devices, algorithms, etc.) with a detailed description of how it is used.
Links to relevant sources (Journals, Youtube videos, Githubsource code, Blogs, Magazine articles, etc.)

### Acoustics I - Noise Source Localization 

Acoustic beamforming is a technique to measure the sound pressure thanks to some microphones arrays and also that is able to locate the sound source, either meaningful or noise by processing the collected sound signals. This technique involved in many academic and industrial applications. 
In daily life, noise sound is one of the main problems of today's world. Every produced vehicle, machine, or tool has to have a sound noise below some certain level according to some standards [13]. Detecting the noise source in a device is a challenging task for engineers. However, using beam forming is one of the most successful noise localization techniques that allows engineers to distinguish each and individual noise sources [14].
Thanks to all development in technology, we are able to build robust microphone arrays that are equipped with more than a hundred microphones which allows us to perform precise noise source localization [13]. One can face the noise source localization problem in automotive, telecommunication, aerospace industry, etc. Noise source localization of airfoil will be explained here as an example.  
Nowadays, environmental issue is one of the most dominant problems in the air transportation system. Airplanes should make as little noise as possible during landing and taking off. Understanding which part causes noise in airplanes requires long-term research and technical infrastructure on its own. Although there are many methods, the beam forming method will be explained.
In the photo below, a scaled aircraft is used to investigate the noise which is caused on the wings by the wind turbine air. In order to find the exact location of the noise, microphone arrays are placed on the ground and the calculated noise powers can be seen in the right of the below image.   

<img align="center" src="images/airfoil.PNG">

<sub>Image Source: [13] </sub>

In another application of airfoil noise localization which is performed in the University of Twente Aeroacoustic Wind Tunnel, the set-up with 112 digital MEMS microphones and FPGA is used for noise source measurement which is given in the image below.

<img align="center" src="images/mic.PNG"  >

<sub>Image Source: [13] </sub>

In this application, the wind is coming from left to right and the placement of the microphones or sensors is optimized to improve the array performance. That's why the placement of the arrays also affects the result of beam forming. 
Delay and Sum technique is already explained before. The area where the noise source is likely to be is divided into grids. Each point of these grids is considered as a noise source and the source pressure levels ​​are obtained by applying the delay-and-sum technique to the signals coming from the points. These values can be presented on a counter map [15].

<img align="center" src="images/beamforming.PNG"  >

<sub>Image Source: [13] </sub>

In the given image above, <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;m" title="m" /> represents the microphones, <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;x" title="x" /> represents the possible noise source in an area and all the signals are captured by the microphones. Output Map is given for only one location which can be calculated with the given formula below [13]. 

<img src="https://latex.codecogs.com/png.image?\dpi{110}&space;L(t,t_{0})&space;=&space;\frac{4\Pi}{M}&space;\sum_{m=1}^{M}p_{m}(x_{0},t&plus;t_{0})|x-x_{0}|&space;" title="L(t,t_{0}) = \frac{4\Pi}{M} \sum_{m=1}^{M}p_{m}(x_{0},t+t_{0})|x-x_{0}| " />

Here <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;M" title="M" /> is the total number of microphones, <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;p_{m}" title="p_{m}" /> is the signal measured by each microphone, <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;x_{0}" title="x_{0}" /> is the one possible source position, <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;x" title="x" /> is the microphone position. 
Here the <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;t_{0}" title="t_{0}" /> is important because it represents the delay and intentionally added to the equation. For each node or possible source location, the signal measured by each microphone is delayed according to the behinded time with the given formula below.

<img src="https://latex.codecogs.com/png.image?\dpi{110}&space;t_{0}&space;=&space;\frac{x-x_{0}}{c_{0}}&space;" title="t_{0} = \frac{x-x_{0}}{c_{0}} " />

## Adaptive Beamforming Algorithms
In communication systems, smart antennas system has become the hour of need as they permit for maximal use of frequency band
by delivering service to the maximal/required users. The smart antenna system includes an antenna elements array, 
a powerful processing of signal hardware and software attempting to implement appropriate Direction of Arrival (DOA) and Beam-forming
algorithms.If the angle of arrival (AOA) of the desired signal is the same, the Fixed Beam-forming is used,
but when the AOA varies over time,
an optimization scheme needs to be devised which iteratively changes the weights of the arrival signals. 
Such a concept is known as Adaptive Beam-forming which adapts the weight in time. 
Accordingly, Adaptive Beam-forming is used to separate the desired signal from the interferer signal by adapting the weight
in terms of time though maximize the Signal to Noise Ratio (SNR), array output and reduces error .
##### types:
Most of the beam forming algorithms can be categorized under two classes according to whether the training signal is used or not.
These two classes are non blind adaptive algorithms and blind adaptive algorithms.
Non blind adaptive beam forming algorithms uses a training signal d(t) to update its complex weight vector. 
This training signal is sent by the transmitter to the receiver during the training period.
Beam forming in the receiver uses this information to compute new complex weight. LMS, NLMS, RLS and DMI algorithms are categorized 
as non blind algorithms. Blind algorithms do not require any training sequence to update it's complex vector.
##### LMS Algorithm:
LMS Algorithm comes under the category of non-blind adaptive algorithms and it is gradient basis technique of steepest decent.
The weight vector update involves an iterative technique, resulting in attempting to reduce the mean square error 
among both the desired signal and the array output, just so the array output is almost approximately equivalent to the desired signal.
Based upon the step size (mu), the convergence of LMS Algorithm is estimated. Thus the appropriate step size (mu) has to be selected.
The equations of the LMS Algorithm are as follows:

</br>
Output signal: yLMS(i + 1) = wlms ∗ signal_ns(: , i + 1) </br>

 Error signal: e(i + 1) = signal_x(i + 1) − yLMS(i + 1) </br>
 
Weight:wlms = wlms + mu ∗e(i+1)∗(signal_ns(:,i+1)) </br>

where signal_ns(: , i + 1) = Total received signal. </br>

##### CMA Algorithm: 
CMA Algorithm is a well known blind adaptive algorithm. The algorithm is introduced to
keep in focus the signal's constant complex envelope (amplitude) property. If the signal arriving is of constant amplitude,
this algorithm should maintain and reestablish the desired signal amplitude. CMA Algorithm is used to suppress the undesired signal
but not completely cancel it. Due to slow convergence of CMA Algorithm, tends to put performance limits during which signals shift
gradually and those signals also have to be identified quickly. The equations of the CMA Algorithm are as follows:

</br>
Output signal: yCMA(i + 1) = wCMA ∗ signal_ns(: , i + 1) </br>

Error signal: eCMA(i + 1) =yCMA(i+1) norm(yCMA(i+1))− yCMA(i + 1) </br>

Weight: wCMA = wCMA + mu ∗ eCMA(i + 1) ∗ (signal_ns(: , i + 1))′ </br>

where signal_ns(: , i + 1) = Total received signal.</br>

##### RLS Algorithm: 
One of the non-blind adaptive algorithms, the RLS Algorithm. The LMS algorithm's convergence speed relies upon the array correlation
matrix's Eigen values. With slow speed, the algorithm converges with large Eigen value distribution and this problem is fixed by RLS
algorithm by updating Gradient step size μ at nth iteration with the gain matrix (r−1(n)).
RLS algorithm is performance-wise better over LMS and CMA Algorithm. RLS algorithm shows the high convergence rate and side lobes are
not entirely eliminated. RLS must have narrower beam widths, adequate rejection of Interference and convergence faster.
High computational complexity is becoming a major drawback. The equations of the RLS Algorithm are as follows: 

</br>
Output signal: y(n) = wt(n) ∗ x(n) </br>

Error signal: e(n) = d(n) − y(n) </br>

Weight: w(n) = r−1(n) ∗ p(n) </br>

where d(n)= desired signal </br>

∑K λK−1x(n)d(n) (input and desired signal correlation).</br>


###### conclusion
The performance improves with the more numbers of antenna elements in the array and large distance between the antennas 
i.e. λ/2 as in simulation results of LMS, CMA and Proposed Algorithm. Compared with both LMS and CMA, RLS Algorithm is better.
RLS Algorithm exhibits higher convergence rate, narrow beam width and lateral lobes are not totally eliminated.
These algorithms are used to steer the beam in desired direction and places a null in the unwanted or interferer direction.
The results of Proposed Algorithm as compared to LMS and CMA Algorithm are better because it places a null towards the interferer
signal and extract desired incoming signal. Thus, the convergence of CMA and LMS is slower than the Proposed Algorithm.
### Biomedicine and Non-Destructive Testing
Ultrasound can be used for diagnostic imaging of internal body structures such as organs, blood vessels, etc.<sup>6</sup>
Inside the transducer (the handpiece which is used to measure) are small piezo-electric elements.
First and alternating voltage is applied to the piezo elements, which then emit ultrasonic sound waves (20 kHz < f < 10 GHz).
The same piezo elements then are used to receive the returning sound waves which bounce of at objects with a higher density (blood <-> organ).

Beamforming in medical ultrasound is applied in two ways:

1. Sending: The spacing between the piezo elements and the delay in their signals can be selected in a way such that an interference
	pattern is created in which the majority of the signal energy all goes out in one angular direction.<sup>5</sup>
2. Receiving: The amplitude and delay of the received signal on each element can be selected such that reception from a chosen
	angular direction is amplified.<sup>5</sup> 

The following animation shows the resulting angular vector created with beamforming.
<br>
<img src="https://upload.wikimedia.org/wikipedia/commons/9/97/Phased_array_imaging_animation.gif" width="400"/>
<br>
<sub>Image Source: https://en.wikipedia.org/wiki/Phased_array_ultrasonics </sub>

Besides medical imaging, the same technique is used in non destructive testing, i.e. detecting cracks, holes or other impurities in materials such as steel.

### Beamforming in Radar Applications

Radars are electromagnetic sensors that are used for the range, angle, or velocity determination of objects. They can be used for detecting motor vehicles, spacecraft, cars, etc. There might be one or more than one transmitter and receiver antennas in radar to detect the mentioned properties of any object. In principle, radars send signals from transmitters and the signals they send come back by hitting an object. The returning signals are picked up by the receivers.

The distance of an object in the coverage area of ​​the radar is calculated by the time it takes the signal to leave and return to the radar. There is a lot of different application of radar in industry and academy [16] however I am going to explain the digital beam forming radars. Besides getting velocity, digital beam-forming radars provide distance and angular information of possible target objects. In general, a good angular resolution which means a large field of view is required for many applications [17]. In order to achieve this high resolution, the number of receivers and transmitters should be increased. For example, eight transmitters and eight receivers on radar can be one option and multiple transceiver and transmitter configuration can be seen in the image below [17].

<img align="center" src="images/radarSensor.PNG" >

<sub>Image Source: [17] </sub>

In one of the applicaiton, two stationary objects are aimed to be detected by the radar. In order to detect them, radar has to calculate the distance of the object by considering the time delay during the propagation and has to calculate the angle where the object is located by considering the frequency domain of the signal. To do this, FFT is used in the receiver part because of the frequency modulation characteristic [17]. Frequency modulated signals have high frequency where the source signal has high amplitude and low frequency where the source signal has low amplitude. 

<img align="center" src="images/fmcw.gif"  >

<sub>Image Source: https://en.wikipedia.org/wiki/Frequency_modulation  </sub>


After getting the angle and distance the location of the objects can be obtained. 
On the left side of the figure below, two corner reflectors are placed with different distances and height in front of the radar. Each corner reflectors have different cross sections. In the radar, frequency-modulated continuous waves are used and the image on the right side of the given image below is obtained after applying the beam forming in which one can see where the relative power is increasing which represents the object in <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;x,y" title="x,y" />. The radar is located at 0,0 and the right side is positive in x coordinate and the left side of the radar is negative.

<img align="center" src="images/ImagingResults.PNG"  >

<sub>Image Source: [20] </sub>

### Radio Astronomy

Radio Astronomy studies celestial objects at radio frequencies and is a subfield of astronomy<sup>7</sup>
The beamforming, i.e., spatial filtering, aims to suppress signals arriving from undesirable directions while amplifying signals from desired directions.<sup>9</sup>
Beamforming is used deliver sufficient gain and sensitivity for radio observations while maintaining
control over beam pattern sidelobes and system noise.<sup>8</sup>.
An appropriate beamforming can significantly increase the detection range, as well as the detection's certainty.<sup>9</sup>


<img src="images/lofar.jpg" width="500"/>
<br>
<sub>Radio Image of a galaxy captured with LOFAR (Low Frequency Array)<sup>10<sup> </sub>
<br>
<sub>Image Source: https://phys.org/news/2013-03-lofar-giant-galaxy-all-sky-survey.html</sub>
<br>
<img src="images/lofar.png" width="500"/>
<br>
<sub>Radio Image of a galaxy captured with LOFAR (Low Frequency Array)<sup>10<sup> </sub>
<br>
<sub>Image Source: https://64.media.tumblr.com/d77c95cd531e183b8a1c0d598e7d9289/tumblr_pk4tnrdJmC1r4vadxo1_400.jpg</sub>

<br>
<br>

### Satellite Communication
##### Why to sue Beamforming technology in satellite application?
The increasing number of low earth orbit (LEO) and medium earth orbit (MEO) satellite constellations and
a shift toward dedicated ground stations to satellite communications as a service (Starlink project) requires 
Ground terminals to flexibly track multiple satellites.This could be done using digital beamforming technologies to enable
fully steerable active antennas to enhance capacity, control, and flexibility. 

##### Why Digital beamforming not Analog Beamforming?
DBF systems remove the need for analog hardware with the exception of RFFE hardware,
mainly the low noise amplifiers (LNAs), power amplifiers (PAs), limiters/input protection, antenna filters,
impedance matching, circulators/isolators/switches for duplexing, and interconnect.
Moreover, advanced DSP techniques can be implemented with a DBF communications link that can “treat” impairments in the RF hardware
and enhance performance. Such methods may even be able to extend the usable life or reduce maintenance of communication systems 
whose RF hardware is beginning to degrade in performance.

##### Future of Satellites with beamforming technologies
Remote areas, aircraft, and ships at sea are still underserved in the new Internet age.
Communication and data systems for these applications are still limited to tens of megabits-per-second (Mbps) 
with systems that cost hundreds and thousands of dollars a month. 
This is compared to terrestrial data and communications systems that can deliver gigabit-per-second (Gbps) speeds and
cost around one-hundred dollars a month or less.
Seeing an opportunity to reach a large portion of underserved applications, 
there are many companies that have moved to creating next-generation HTS systems in LEO and MEO orbits using
massive satellite constellations. 
These satellites are necessarily designed with much more digital and software configurable hardware than typical satellites, 
are lower cost, more compact, and are deployed in the hundreds, and even thousands.
To reach this economy of scale, automotive, industrial, aerospace, military hardware has been adapted to the 
requirements of these new satellite systems.
However, using non-space grade RF hardware isn’t viable in traditional space 
applications or mission critical satellites meant to operate for over two decades given 
the sensitivity of RF hardware to environmental conditions. To overcome the cost and volume limitations typical of space-grade,
builders of massive satellite constellations are instead self-qualifying electronics, which is a costly and complex process to 
perform upfront. However, this approach can provide substantial benefits to return-on-investment (ROI) when the satellite numbers
reach a large enough volume threshold.
Either way, RF hardware is often contained in heavy and expensive metallic enclosures, often hermetic, using specialized 
and ruggedized materials/designs to ensure the hardware can perform in the harsh environments in space/microgravity. Hence, 
there is a drive toward minimizing the amount of RF hardware in new satellite systems, replacing the RF hardware with digital 
hardware that is more compact and reprogrammable.
Another aspect is the predicted increase in demand for ground station hardware for consumers and devices. More ubiquitous Internet
connectivity and the growing use of data and automated systems to sense, analyze, and control a variety of industrial, robotic,
and machine systems, especially mobile systems, is likely to be extremely reliant on the burgeoning HTS satellite systems. 
This requires ground station hardware that can perform real-time tracking of satellites, even on-the-go. 
Real-time satellite tracking for LEO and MEO satellite constellations is an extreme engineering challenge, 
especially when the goal is to minimize the cost of the user ground station hardware. Hence, 
DBF systems and antenna arrays for ground station hardware enable near instantaneous tracking without the need for large,
expensive, and possibly unreliable mechanical tracking hardware with heavy parabolic antenna dishes. Though the demands on 
ground station hardware generally aren’t as stringent as the space hardware, using DBF systems would still reduce the size, 
weight, and possibly even cost of ground station hardware and provide better user experience.
 
<img src="images/future-satellites.png" width="700"/>

### Seismology

<img src="https://upload.wikimedia.org/wikipedia/commons/7/79/Seismic_array.png" width="500"/>
<br>
<sub>A wavefront coming from north-east and crossing a seismic array.<sup>12<sup> </sub>
<br>
<sub>Image Source: https://en.wikipedia.org/wiki/Seismic_array</sub>
<br>
<br>

Seismic arrays are used to increase sensitivity to earthquake and explosion detection compared to single sensors.
Beamforming in seismic arrays is used to suppress noises and enhnance the signal-to-noise ration (SNR) by summing the coherent signals from the single array sites<sup>11</sup>.The most important point during the beamforming process is to find the best delay times, with which the single traces must be shifted before summation in order to get the largest amplitudes due to coherent interference of the signals<sup>11</sup>.

### Beamforming In Sonar Applications
Sonar means Sound Navigation and Ranging which is useful for exploring and mapping the oceans by using sound waves. Since the sound speed is constant, it can be used for calculating the distance from Sonar itself. The distance of an object is calculated by measuring the time that takes the sound waves return after having transmitted from the transmitter. Therefore reflected sound signals are used. When the transmitter emitting time and the time that the receiver has the reflected sound signal is known, the distance can be calculated easily.

<img align="center" src="images/sonarReflector.PNG"  >

<sub>Image Source: [19] </sub>

Beamforming is used for detecting fish population density under the water. 

<img align="center" src="images/fish.PNG"  >

<sub>Image Source: [19] </sub>

Sonar is used for 2D or 3D mapping of the seafloor by estimating range in different levels with beam forming methods.

<img align="center" src="images/seafloor.PNG"  >

<sub>Image Source: [19] </sub>

Detection of the object in the seafloor is of growing in importance right now in the current underwater research. Thanks to these researches mines, toxic wastes, or archeological findings can be found which are vitally important for people and nature [18].

### Wireless Communications (5G)
Due to increasing demand of cellular mobile communication services and as number of users growes and users expect higher data rates
, 5G technology to be implemented worldwide in next couple of years
which relies on using higher frequencies currently(cm) will be (mm bands) opening the field for 
- allowing more users per cell
- Higher data rates


This could be possible due to Beamforming technology giving the new technology more abilities as increasing frequencies, increases
power loss to mobile phones as well
 , RF waves travel through the atmosphere the waves will get scattered due to interaction with the constituent molecules present
in the atmosphere or any medium concrete walls for example.
Now the amount of scattering is more for a wave of higher frequency.to compensate this additional attenuations , 
(Transmission beamforming) is to used to direct the signal to mobile phones increasing the signal power to the required receiving mobile phone
and also vice verse from the mobile phone as transmitter to the base station receiving (this is called reception beamforming )

##### Analog beamforming used in 5G
While digital beamforming at the baseband processor is most commonly used today, analog beamforming in the RF 
domain can provide antenna gains that mitigate the lossy nature of 5G millimeter waves
,The signal phases of individual antenna signals are adjusted in RF domain. Analog beamforming impacts the radiation 
pattern and gain of the antenna array, thus improves coverage. Unlike in digital beamforming, only one beam per set of
antenna elements can be formed. The antenna gain boost provided by the analog beamforming overcomes partly the impact of
high pathloss in mm Wave. Therefore analog beamforming is considered mandatory for the mm Wave frequency range 5G NR.
##### Beam steering and beam switching 
Beam steering is achieved by changing the phase of the input signal on all radiating elements. Phase shifting allows the signal
to be targeted at a specific receiver. An antenna can employ radiating elements with a common frequency to steer a single beam 
in a specific direction. Different frequency beams can also be steered in different directions to serve different users.
The direction a signal is sent in is calculated dynamically by the base station as the endpoint moves,
effectively tracking the user. If a beam cannot track a user, the endpoint may switch to a different beam.
<img src="images/5g-beamforming.png" width="700"/>


## Demonstration

With a "ReSpeaker 6-Mic Circular Array", different simultaneous noises from different directions are recorded. Those noises overlap and are not easy to understand. We implement a program where the user can choose in which direction the microphone array should focus. This method using beamforming is implemented with Python.

<img src="images/wireframe.jpg" width="700"/>

### Hardware

* Raspberry Pi 3 B+<sup>1</sup>
* ReSpeaker 6-Mic Circular Array<sup>2</sup>
<br>
<img src="images/mic_array.jpg" width="700"/>
<br>
<sub>Image Source: https://files.seeedstudio.com/wiki/ReSpeaker_6-Mics_Circular_Array_kit_for_Raspberry_Pi/img/hardware.jpg </sub>

### Software 
* Raspberry Pi OS<sup>3</sup>
* Audacity<sup>4</sup>

### Implementation

### Sources
1. [Raspberry Pi 3 B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/)
2. [ReSpeaker 6-Mic Circular Array](https://wiki.seeedstudio.com/ReSpeaker_6-Mic_Circular_Array_kit_for_Raspberry_Pi/)
3. [Raspberry Pi OS](https://www.raspberrypi.org/software/)
4. [Audacity](https://www.audacity.de//)
5. [Norwegian university of science and technology](https://www.ntnu.edu/isb/ultrasound/beamforming)
6. [Wikipedia - Medical Ultrasound](https://en.wikipedia.org/wiki/Medical_ultrasound)
7. [Wikipedia - Radio Astronomy](https://en.wikipedia.org/wiki/Radio_astronomy)
8. [Signal Processing for Phased Array Feeds in Radio Astronomical Telescopes](https://safe.nrao.edu/wiki/pub/Beamformer/WebHome/JeffsWarnick_SPASRA_134_2_col.pdf)
9. [Beamforming of LOFAR Radio-Telescope for Passive Radiolocation Purposes](https://www.mdpi.com/2072-4292/13/4/810/pdf)
10. [LOFAR Radiotelescope](https://www.researchgate.net/figure/Aerial-photograph-of-the-Superterp-the-heart-of-the-LOFAR-core-from-August-2011-The_fig14_236834766)
11. [Wikipedia - Seismic array](https://en.wikipedia.org/wiki/Seismic_array)
12. [Bormann, P (2012). New Manual of Seismological Observatory Practice (NMSOP-2). IASPEI. p. Chapter 9.]()
13. [Department Thermal Fluid Engineering University of Twente (n.d.) Fundamentals of Acoustic Beamforming, P.O. Box 217 Enschede, 7500 AE The Netherlands: Leandro de Santana.]()
14. [National Instruments (n.d.) Using Acoustic Beamforming for Pass-By Noise Source Detection, P.O. Box 217 Enschede, 7500 AE The Netherlands: Doug Farrell,Product Manager.]()
15. [(2003) Noise Source Location Techniques – Simple to Advanced Applications, P.O. Box 217 Enschede, 7500 AE The Netherlands: Mehdi Batel and Marc Marroquin, Brüel & Kjær North America, Inc., Norcross, Georgia Jørgen Hald, Jacob J. Christensen, Andreas P. Schuhmacher and Torben G. Nielsen, Brüel & Kjær, Denmark.]()
16. [(20 January 2021) Radar configurations and Types, Available at: https://en.wikipedia.org/wiki/Radar_configurations_and_types]()
17. [Marlene Harter, Andreas Kornbichler, Thomas Zwick (2010) A Modular 24 GHz Radar Sensor for Digital Beamforming on Transmit and Receive]()
18. [(2006) Acoustic Imaging of Underwater Embedded Objects: Signal Simulation for Three-Dimensional Sonar Instrumentation, : Maria Palmese, Member, IEEE, and Andrea Trucco, Senior Member, IEEE.]()
19. [Department of Informatics, University of Oslo (September 2013) Introduction to Sonar INF-GEO4310, : Roy Edgar Hansen.]()
20. [(October 2011) Three-dimensional radar imaging by digital beamforming, : Marlene Harter,Andreas Ziroff,Thomas Zwick.]()