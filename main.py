class Device:
    def __init__(self, device_id, name, location):
        self.device_id = device_id
        self.name = name 
        self.location = location

 def monitor_status(self):
    return "Device is operational"   
 
 def device_info(self):
    print ("Device ID", self.device_id)
    print ("Device Name", self.name)
    print ("Device Location", self.location)