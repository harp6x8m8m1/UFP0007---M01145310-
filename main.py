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

class Sensor(Device):
    def __init__(self, device_id, name, location, sensor_type):
        super().__init__(device_id, name, location)
        self.temperature = temperature 

    def check_attention(self):
        if self.temperature > 40:
            return "WARNING: High temperature!"
        return "Temperature is normal"
    