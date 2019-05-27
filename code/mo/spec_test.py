import seabreeze
seabreeze.use("cseabreeze")
import seabreeze.spectrometers as sb

import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt

#plt.ion()

devices = sb.list_devices()
print("Devices: ", devices)

spec = sb.Spectrometer(devices[0])

wl = spec.wavelengths()
print(wl)

spec.integration_time_micros(50000)

#intens = spec.intensities()
#print("Intensitites: ", intens)

#input("Press a button to acquire white reference")
#int_ref = spec.intensities()

#input("Press a button to start acquisition")
intens = spec.intensities()
fig = plt.figure()
#fig.show()
ax = fig.add_subplot(111)
line1, = ax.plot(wl,intens,"b-")
plt.show(block=False)
axes = fig.gca()
axes.set_ylim(0,5000)
spec.integration_time_micros(100000)
while True:
	#ax.clear()
	intens = spec.intensities()# / int_ref
	line1.set_ydata(intens)
	#ax.draw_artist(ax.patch)
	#ax.draw_artist(line1)
	#fig.canvas.update()
	#fig.canvas.flush_events()
	plt.pause(0.001)

