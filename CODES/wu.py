from org.myrobotlab.openni import Skeleton
from org.myrobotlab.openni import OpenNiData

times = 0
returned = False

runtime.createAndStart("openni", "OpenNi")

openni.startUserTracking()
openni.addListener("publishOpenNIData", python.name, "input")

def input(data):
	opennidata = data #msg_openni_publishopennidata.data[0]
	skeleton = opennidata.skeleton
	global UserTracked
	global oldvalue, times, returned


	if skeleton.rightElbow.angleXY == 0:
		pass
	elif skeleton.rightElbow.angleXY > 120 and returned:
		times += 1
		returned = False
	elif skeleton.rightElbow.angleXY < 60:
		returned = True

	if times > 3:
		times = 0

	print(times)
		
