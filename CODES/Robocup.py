from org.myrobotlab.openni import Skeleton
from org.myrobotlab.openni import OpenNiData
virtual = False
counter = 1
returned = False
times = 0
spoken = True


#set used Ports
rightPort = "COM8"
leftPort = "COM4"
i01 = Runtime.start("i01", "InMoov")



def holdMicrophone():
	
	i01.moveHand("right",180.0,180.0,180.0,180.0,90.2)
	sleep(4)
	i01.moveHand("right",5.0,5.0,5.0,5.0,90.2)
	sleep(4)
def dance1():
	i01.moveHead(90.2,90.2,80.0,90.0,10.0,90.2)
	i01.moveArm("left",5.0,90.2,31.0,10.0)
	i01.moveHand("left",2.0,2.0,2.0,2.0,90.2)
	i01.moveArm("right",5.2,90.2,30.2,10.2)
	i01.moveHand("right",180.0,180.0,180.0,180.0,90.2)
	i01.moveTorso(104.0,53.0,90.0)
	sleep(5)
	i01.moveHead(90.2,90.2,80.0,90.0,10.0,90.2)
	i01.moveArm("left",5.0,90.2,31.0,10.0)
	i01.moveHand("left",2.0,2.0,2.0,2.0,90.2)
	i01.moveArm("right",5.2,90.2,30.2,10.2)
	i01.moveHand("right",180.0,180.0,180.180,180.0,90.2)
	i01.moveTorso(77.0,145.0,90.0)
	sleep(5)
	i01.moveHead(90.2,90.2,80.0,90.0,10.0,90.2)
	i01.moveArm("left",65.0,90.2,31.0,38.0)
	i01.moveHand("left",2.0,2.0,2.0,2.0,90.2)
	i01.moveArm("right",49.0,90.2,30.2,10.2)
	i01.moveHand("right",2.0,2.0,2.0,2.0,90.2)
	i01.moveTorso(75.0,82.0,90.0)
	sleep(5)


def standart():
	i01.moveHead(90.2,90.2,80.0,90.0,10.0,90.2)
	i01.moveArm("left",5.0,90.2,31.0,10.0)
	i01.moveHand("left",2.0,2.0,2.0,2.0,90.2)
	i01.moveArm("right",5.2,90.2,30.2,10.2)
	i01.moveHand("right",180.0,180.0,180.0,180.0,90.2)
	i01.moveTorso(90.0,90.0,90.0)
	sleep(5)
	
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

WebGui = Runtime.create("WebGui","WebGui")
WebGui.autoStartBrowser(False)
WebGui.startService()

WebGui.startBrowser("http://localhost:8880/#/service/ear")
ear = Runtime.start("ear","WebkitSpeechRecognition")
ear.setLanguage("en")

mouth = Runtime.start("mouth", "MarySpeech")
ear.addMouth(mouth)
ear.setAutoListen(True)
ear.setContinuous(False)
torso = i01.startTorso(leftPort)

mouth.speak("setup completed")
runtime.createAndStart("openni", "OpenNi")
openni.startUserTracking()
ear.startListening()
i01.ear.stopListening()


holdMicrophone()


def input(data):
	opennidata = data #msg_openni_publishopennidata.data[0]
	skeleton = opennidata.skeleton
	global counter,returned,times
	
	if skeleton.rightElbow.angleXY == 0 :
		pass
	elif skeleton.rightElbow.angleXY > 120 and returned:
		times += 1
		returned = False
	elif skeleton.rightElbow.angleXY < 40:
		returned = True
		
	
	if counter == 1 and times == 1:
		startPresentation1()
		counter += 1
	if counter == 2 and times == 2:		
		startPresentation2()
		times=0
		counter = 1	
	
def startPresentation1():
	
	mouth.speak("Hello people, I am professor Inmoov and welcome to the best dancing show on earth. Our Team is Rozhin Heidari, Andrea Windisch, Jeremia Baumgartner, Jakob Schreiner, Benjamin Witzerstorfer. And today we have two wonderful contestants for our show, Jakob and John.")
	

def	startPresentation2():
	global spoken
	if spoken:
		spoken = False
		mouth.speak("That was a great performance and a wonderful dance! Now I would also like to dance a little bit.")
		sleep(5)
		dance1()
		standart()
		mouth.speak("Well that was funny. But every show has to end sometime. Thank you for being such a great audience. This was our great show InMoov where everybody is and was in move.")


	

#ear.addListener("publishText","python","onText")
openni.addListener("publishOpenNIData", python.name, "input")