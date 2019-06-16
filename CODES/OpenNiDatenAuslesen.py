# importieren der Daten
from org.myrobotlab.openni import Skeleton
from org.myrobotlab.openni import OpenNiData
# Datenroute erstellen 
openni.addListener("publishOpenNIData", python.name, "input")
# Daten abrufen und verarbeiten
def input(data):
	opennidata = data 
	skeleton = opennidata.skeleton
	if skeleton.rightElbow.angleXY == 0:
		pass
	elif skeleton.rightElbow.angleXY > 120:
		print ("angle greater than 120")
	elif skeleton.rightElbow.angleXY < 60:
		print ("angle smaller than  60")





