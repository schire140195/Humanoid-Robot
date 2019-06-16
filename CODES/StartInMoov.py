
#set used Ports
rightPort = "COM8"
leftPort = "COM4"
i01 = Runtime.start("i01", "InMoov")
# Map the Ports to virtual Ports
if ('virtual' in globals() and virtual):
	leftPortvirtualArduino = Runtime.start("leftPortvirtualArduino", "VirtualArduino")
	leftPortvirtualArduino.connect(leftPort)
	rightPortvirtualArduino = Runtime.start("rightPortvirtualArduino", "VirtualArduino")
	rightPortvirtualArduino.connect(rightPort)

# starting parts
i01.startAll(leftPort,rightPort)
if ('virtual' in globals() and virtual):
	#start Virtual InMoov
	i01.startVinMoov()
	