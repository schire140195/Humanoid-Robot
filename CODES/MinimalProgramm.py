#Virtual InMoov will be executed
virtual = True
# Programm to setup InMoov with the basic services
rightPort = "COM8"
leftPort = "COM10"
#create new InMoov
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
    i01.startVinMoov()

# add verbal commands
i01.mouth.speakBlocking(u"Hello world")
i01.ear.addCommand("hello","python","spock")

i01.ear.startListening("yes| no thanks |snowball| bye-bye")
i01.ear.addListener("recognized",python.name,"heard")
i01.ear.addMouth("i01.mouth")

def heard(data):
    data = msg_i01_ear_recognized.data[0]

    if(data == "bye-bye"):
        i01.mouth.speak("see you soon")
    if(data == "snowball" ):
        i01.mouth.speak("catch this")
        snowball()
	if(data == "no thanks"):
		i01.mouth.speak("Brexit was a mistake")


# Movements
def snowball():
    i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
    i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
    i01.moveArm("left",5,90,110,10)
    i01.moveArm("right",5,90,110,10)
    i01.mouth.speak("trowing ball")

def spock():
	i01.mouth.speak("catch this")
	
