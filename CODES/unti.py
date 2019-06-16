from org.myrobotlab.openni import Skeleton

runtime.createAndStart("openni", "OpenNi")

openni.startUserTracking()
openni.addListener("publishOpenNIData", python.name, "input")

def input():
	#skeleton = msg_openni_publish.data[0]
	#print ' head x y z and quality ', skeleton.head.x, skeleton.head.y, skeleton.head.z, skeleton.head.quality
	print 'foo'

