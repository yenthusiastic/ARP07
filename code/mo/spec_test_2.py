import seabreeze
seabreeze.use("cseabreeze")

import seabreeze.spectrometers as sb

import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt

dc_test = 2800 

devices = sb.list_devices()
print("Devices: ", devices)

spec = sb.Spectrometer(devices[0])
spec2 = sb.Spectrometer(devices[1])

wl = spec.wavelengths()
wl2 = spec2.wavelengths()

intens = spec.intensities() - dc_test
intens2 = spec2.intensities() - dc_test

fig = plt.figure()

ax = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax.title.set_text(str(spec))
ax2.title.set_text(str(spec2))

line1, = ax.plot(wl,intens,"b-")
line2, = ax2.plot(wl2,intens2,"b-")

plt.show(block=False)

ax.set_ylim(0,5000)
ax.set_ylim(0,5000)

spec.integration_time_micros(50000)
spec2.integration_time_micros(50000)

while True:
	intens = spec.intensities() - dc_test# / int_ref
	intens2 = spec2.intensities() - dc_test# / int_ref

	line1.set_ydata(intens)
	line2.set_ydata(intens2)

	plt.pause(0.001)
