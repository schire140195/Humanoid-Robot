i01 = Runtime.start("i01", "InMoov")


WebGui = Runtime.create("WebGui","WebGui")
WebGui.autoStartBrowser(True)
WebGui.startService()

WebGui.startBrowser("http://localhost:8888/#/service/ear")
ear = Runtime.start("ear","WebkitSpeechRecognition")
ear.setLanguage("en")

mouth = Runtime.start("mouth", "MarySpeech")
ear.addMouth(mouth)

ear.setAutoListen(True)
ear.setContinuous(False)

def lightOn():
	mouth.speakBlocking("light is on")

def lightOff():
	mouth.speakBlocking("light is off")

def onText(data):
	print data
	if (data == "light on"):
		lightOn()
	if (data == "light off"):
		lightOff()
	if (data == "let's play rock-paper-scissors"):
		mouth.speak("okay let's play")
	if (data == "play rock-paper-scissors"):
		mouth.speak("okay let's play")
	if (data == "rock-paper-scissors"):
		mouth.speak("okay let's play")
ear.addListener("publishText","python","onText")