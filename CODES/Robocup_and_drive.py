from org.myrobotlab.openni import Skeleton
from org.myrobotlab.openni import OpenNiData
virtual = False
counter = 1
returned = False
times = 0

drive_pin_back_l = 4
drive_pin_back_r = 7
drive_pin_en_l = 2
drive_pin_en_r = 3
drive_pin_speed_l = 5
drive_pin_speed_r = 6

#set used Ports
drive_port = "COM14"  # Replace com, for linux /dev/ttyUSB0
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
torso = i01.startTorso(rightPort)

mouth.speak("setup completed")
openni = Runtime.createAndStart("openni", "OpenNi")
openni.startUserTracking()

drive_arduino = Runtime.createAndStart("arduino","Arduino")

drive_arduino.connect(drive_port)
# give it a second for the serial device to get ready
# sleep(1)
# update the GUI with configuration changes
drive_arduino.broadcastState()
for pin in range(1,8):
    drive_arduino.pinMode(pin, drive_arduino.OUTPUT)

ear.startListening()
i01.ear.stopListening()
holdMicrophone()

def set_backwards(r_on, l_on):
    if r_on > 0:  # rechts
        drive_arduino.digitalWrite(drive_pin_back_r, 1)
    else:
        drive_arduino.digitalWrite(drive_pin_back_r, 0)

    if l_on > 0:  # links
        drive_arduino.digitalWrite(drive_pin_back_l, 1)
    else:
        drive_arduino.digitalWrite(drive_pin_back_l, 0)

def set_enable(r_speed, l_speed):
    if not l_speed:
        drive_arduino.digitalWrite(drive_pin_en_l, 0)
    else:
        drive_arduino.digitalWrite(drive_pin_en_l, 1)

    if not r_speed:
        drive_arduino.digitalWrite(drive_pin_en_r, 0)
    else:
        drive_arduino.digitalWrite(drive_pin_en_r, 1)

def set_speed(r_speed, l_speed):
    set_enable(r_speed, l_speed)
    set_backwards(r_speed, l_speed)

    drive_arduino.analogWrite(drive_pin_speed_l, l_speed)
    drive_arduino.analogWrite(drive_pin_speed_r, r_speed)

"""
from time import sleep
set_speed(31,31)
sleep(1)
set_speed(0,0)
mouth.speak("done")
"""

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
		
	print counter	




def startPresentation1():
	openni.stopCapture()
	mouth.speak("Hello people, I am professor Inmoov and welcome to the best dancing show on earth. Our Team is Rozhin Heidari, Andrea Windisch, Jeremia Baumgartner, Jakob Schreiner, Benjamin Witzersdorfer. And today we have two wonderful contestants for our show, Jakob and John.")
	openni.startUserTracking()

def	startPresentation2():
	openni.stopCapture()
	mouth.speak("That was a great performance and a wonderful dance! Now I would also like to dance a little bit.")
	i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
	i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
	i01.setArmSpeed("left", 20.0, 20.0, 20.0, 20.0)
	i01.setArmSpeed("right", 20.0, 20.0, 20.0, 20.0)
	i01.setHeadSpeed(0.8, 0.8)

	sleep(2)
	i01.moveHead(90.2,90.2,80.0,90.0,10.0,90.2)
	i01.moveArm("left",5.2,90.2,180.0,10.2)
	i01.moveHand("left",2.0,2.0,2.0,2.0,90.2)
	i01.moveArm("right",5.2,98.0,161.0,10.2)
	i01.moveHand("right",2.0,2.0,2.0,2.0,90.2)
	i01.moveTorso(120.0,153.0,89.0)
	sleep(4)
	i01.moveHead(90.2,90.2,80.0,90.0,10.0,90.2)
	i01.moveArm("left",5.2,90.2,180.0,10.2)
	i01.moveHand("left",2.0,2.0,2.0,2.0,90.2)
	i01.moveArm("right",5.2,98.0,161.0,10.2)
	i01.moveHand("right",2.0,2.0,2.0,2.0,90.2)
	i01.moveTorso(60.0,13.0,89.0)
	sleep(4)
	rest()
	mouth.speak("Come on and join me")
	sleep(4)
	openni.startUserTracking()
	mouth.speak("Well that was funny, maybe I will do a Dance course in summer. But every show has to end sometime. Thank you for being such a great audience. This was our great show InMoov where everybody is and was in move.")
	
def holdMicrophone():
	openni.startUserTracking()
	i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
	i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
	i01.setArmSpeed("left", 20.0, 20.0, 20.0, 20.0)
	i01.setArmSpeed("right", 20.0, 20.0, 20.0, 20.0)
	i01.setHeadSpeed(0.8, 0.8)
	i01.moveHead(90.2,90.2,80.0,90.0,10.0,90.2)
	i01.moveArm("left",5.2,40.0,30.2,10.2)
	i01.moveHand("left",2.0,2.0,2.0,2.0,90.2)
	i01.moveArm("right",90.0,53.0,99.0,10.2)
	i01.moveHand("right",180.0,180.0,180.0,180.0,90.2)
	i01.moveTorso(90.2,90.2,90.0)
	

def onText(text):
	print(text)
	if text == "let's go" :
		startPresentation1()
	if text =="hold this":
		holdMicrophone()
	if text == "stop it":
		startPresentation2()

def rest():
  fullspeed()
  if isRightHandActivated:
    i01.rightHand.rest()
  
  if isLeftHandActivated:
    i01.leftHand.rest()
  
  if isRightArmActivated:
    i01.rightArm.rest()
  
  if isLeftArmActivated:
    i01.leftArm.rest()   
  
  if isHeadActivated:
    i01.head.rest()
  
  if isTorsoActivated:
    i01.torso.rest()
    
  if isEyeLidsActivated:
    i01.eyelids.rest()
    

#ear.addListener("publishText","python","onText")
openni.addListener("publishOpenNIData", python.name, "input")