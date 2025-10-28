class Gadget:
    def __init__(self):
       def start(self):
        print("Gadget started")

class Phone(Gadget):
    def start(self):
        print("Phone is starting")

class Laptop(Gadget):
    def start(self):
        print("Laptop is starting")

gadgets =[Phone(), Laptop()]

for gadget in gadgets:
    gadget.start()

class CameraFeature:
    def take_photo(self):
        print("Photo taken")

class WifiEnabled:
    def connect_wifi(self):
        print("Connected to Wifi!")

class Smartphone(Phone,CameraFeature,WifiEnabled):
    def start(self):
        print("Smartphone is starting")

class Smartprinter(Gadget,WifiEnabled):
    def start(self):
        print("Smartprinter is starting")

devices =[Smartphone(), Smartprinter()]
for device in devices:
    device.start()
    if isinstance(device, CameraFeature):
        device.take_photo()
    if isinstance(device, WifiEnabled):
        device.connect_wifi()
        


