from matplotlib.pyplot import plot, show, setp, xlim, ylim, yticks, scatter, xlabel, title, legend, figure, xticks, ylabel, gca


def plot_IR(file):
	spectrum = open(file,'r')

	xdata = []
	ydata = []

	lines= spectrum.readlines()
	for line in lines:
		x, y = line.split()
		xdata.append(float(x))
		ydata.append(float(y))
	maxim = max(ydata)
	i=0
	for value in ydata:
		ydata[i] = value*0.1
		i+=1

	spectrum.close()

	graph = plot(xdata, ydata, linewidth=0.8)
	setp(graph , color = 'k', zorder=1)
	ax = gca()
	ax.set_facecolor('xkcd:pale blue')
	#ax.set_facecolor((1.0, 0.47, 0.42))
	xlim(4000,400)
	yticks([])
	title("IR Spectrum")
	ylim(min(ydata)-1,max(ydata)+0.5)
	ylabel("% Transmittance")
	xlabel("Frequency 1/cm")
	show()

