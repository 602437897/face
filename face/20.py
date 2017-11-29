from VideoCapture import Device

cam = Device()
cam.setResolution(400,400)
cam.saveSnapshot('father.jpg')