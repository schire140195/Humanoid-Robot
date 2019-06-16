import random
from org.myrobotlab.openni import Skeleton
from org.myrobotlab.openni import OpenNiData

times = 0
returned = False
virtual = True
counter = 1
rightPort = "COM8"
leftPort = "COM10"
human = 0
robot = 0
rand = 0
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


WebGui = Runtime.create("WebGui","WebGui")
WebGui.autoStartBrowser(False)
WebGui.startService()

WebGui.startBrowser("http://localhost:8888/#/service/ear")
ear = Runtime.start("ear","WebkitSpeechRecognition")
ear.setLanguage("en")

mouth = Runtime.start("mouth", "MarySpeech")
ear.addMouth(mouth)
runtime.createAndStart("openni", "OpenNi")
ear.setAutoListen(False)
ear.setContinuous(False)


#mouth.speak("setup completed")
#sleep(4)
#mouth.speak("hello my Name is Stephen")
ear.startListening()

def rockPaperScissors():
	mouth.speak("okay let's play")
	sleep(2)
	mouth.speak("3 points to win")
	sleep(2)
	mouth.speak("I will capture yout hand and try to copy your movement")
	openni.startUserTracking()
	sleep(2)
	ready()

def onText(text):
	print (text)
	if (text == "let's play rock-paper-scissors"):
		rockPaperScissors()
	if (text == "play rock-paper-scissors"):
		rockPaperScissors()
	if (text == "rock-paper-scissors"):
		rockPaperScissors()
	if (text == "i have rock"):
		humanRock()
	if (text == "i have paper"):
		humanPaper()
	if (text == "i have scissors"):
		humanScissors()
	if (text == "stop plying" or text == "stop"):
		stopRockPaperScissors()

		
def input(data):
	opennidata = data 
	skeleton = opennidata.skeleton
	global times, returned , counter


	if skeleton.rightElbow.angleXY == 0:
		pass
	elif skeleton.rightElbow.angleXY > 120 and returned:
		times += 1
		returned = False
	elif skeleton.rightElbow.angleXY < 60:
		returned = True

	if times == 1 and counter == 1:
		mouth.speak("Rock")
		counter += 1
	if times == 2 and counter == 2:
		mouth.speak("Paper")
		counter += 1
	if times == 3 and counter == 3:
		mouth.speak("Scissors")
		counter = 1
		times = 0
		rockPaperScissors2()

def rockPaperScissors2():
	global rand
	
  	#i01.copyGesture(False)
	sleep(2)
	x = (random.randint(1, 3))
	rand = x
	if x==1:
		rock()
		mouth.speak("I got Rock")
		sleep(2)
		mouth.speak("what do you have")
	if x==2:
		paper()
		mouth.speak("I got paper")
		sleep(2)
		mouth.speak("what do you have")
	if x==3:
		mouth.speak("I got Scissors")
		sleep(2)
		mouth.speak("what do you have")
	

def humanRock():
	print (rand)
	if rand == 1:
		mouth.speak("oh thats not working")
		print("oh thats not working")
		countPoints("even")
	if rand == 2:
		mouth.speak("my point")
		print("my point")
		countPoints("robot")
	if rand == 3:
		mouth.speak("your point")
		print("your point")
		countPoints("human")

def humanPaper():
	print (rand)
	if rand == 2:
		mouth.speak("oh thats not working")
		print("oh thats not working")
		countPoints("even")
	if rand == 3:
		mouth.speak("my point")
		print("my point")
		countPoints("robot")
	if rand == 1:
		mouth.speak("your point")
		print("your point")
		countPoints("human")


def humanScissors():
	print (rand)
	if rand == 3:
		mouth.speak("oh thats not working")
		print("oh thats not working")
		countPoints("even")
	if rand == 1:
		mouth.speak("my point")
		print("my point")
		countPoints("robot")
	if rand == 2:
		mouth.speak("your point")
		print("your point")
		countPoints("human")

def countPoints(who):
	global human, robot

	if who == "even":
		pass
	if who == "robot":
		robot += 1
	if who == "human":
		human += 1

	if human == 3 or robot == 3:
		if human == 3:
			mouth.speak("well played")
		if robot == 3:
			mouth.speak("I won please don't cry")		
		stopRockPaperScissors()

def ready():
	mouth.speak("ready")
	sleep(2)
	mouth.speak("go")

def stopRockPaperScissors():
	human = 0
	robot = 0
	rand = 0
	openni.stopCapture()
	mouth.speak("was nice playing with you")
	sleep(2)
	mouth.speak("if you want to play on tell me")

def rock():
	i01.moveHead(90,90,80,90,75)
	i01.moveArm("left",49,90,75,10)
	i01.moveArm("right",5,90,30,10)
	i01.moveHand("right",40,171,180,180,180,140)
	i01.moveHand("left",2,2,2,2,2,90)
	sleep(.2)

def paper():
	i01.moveHead(90,90,80,90,75)
	i01.moveArm("left",49,90,75,10)
	i01.moveArm("right",5,90,30,10)
	i01.moveHand("right",0,0,0,0,0,165)
	i01.moveHand("left",2,2,2,2,2,90)
	sleep(.2)

	

def scissors():
	i01.moveHead(90,90,80,90,75)
	i01.moveArm("left",49,90,75,10)
	i01.moveArm("right",5,90,30,10)
	i01.moveHand("right",50,0,0,180,180,90)
	i01.moveHand("left",2,2,2,2,2,90)
	sleep(.2)


ear.addListener("publishText","python","onText")
openni.addListener("publishOpenNIData", python.name, "input")